# Grounding: transcribed from oshima/api/app/services/pipeline/storage_pipeline.py
#!/usr/bin/env python3
"""
Storage-Aware PDF Processing Pipeline

Adapts the existing ingest-to-FOL pipeline to work with the new storage architecture,
job manifests, and artifact management system.
"""

import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

# Add app directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from services.consolidation.final_consolidator import FinalConsolidator
from services.extract.attribution import SourceAttributor
from services.extract.extract_paper import PaperExtractor
from services.ingest.ingest_pdf import PDFExtractor
from services.nlp2fol.complete_pipeline_processor import CompletePipelineProcessor
from services.nlp2fol.duplicate_analyzer import LogicalDuplicateAnalyzer
from services.nlp2fol.extract_adapter import ExtractAdapter
from services.nlp2fol.ontologies.sumo.s0_resources import ensure_corenlp_running

from app.models.job_manifest import JobManifest, StageStatus
from app.services.manifests.db_manifest_manager import DatabaseManifestManager
from app.services.storage.storage_client import get_pdf_download_url

logger = logging.getLogger(__name__)


def _sanitize_for_database(data: Any) -> Any:
    """
    Sanitize data to remove null bytes and other problematic characters
    that PostgreSQL/Supabase cannot handle in JSON storage
    """
    if isinstance(data, str):
        # Remove null bytes and other problematic Unicode characters
        return re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", data)
    elif isinstance(data, dict):
        return {k: _sanitize_for_database(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [_sanitize_for_database(item) for item in data]
    else:
        return data


class StoragePipeline:
    """
    Storage-aware pipeline that processes documents through all 6 stages:
    1. Ingest - PDF → Structured JSON (Adobe API)
    2. Extract - Structured data → Claims/Evidence (LLM)
    3. Attribution - Link claims/evidence to source locations
    4. NLP2FOL - Convert to First-Order Logic representations
    5. Deduplication - Remove logical duplicates
    6. Consolidation - Create single final output file

    Maintains artifacts and updates job manifests throughout processing.
    """

    def __init__(
        self,
        manifest_manager: Optional[DatabaseManifestManager] = None,
        model: str = "gpt-5-mini-2025-08-07",
        auto_start_corenlp: bool = True,
        corenlp_client=None,
        rate_limiter=None,
    ):
        """Initialize pipeline with database-based storage integration"""
        self.manifest_manager = manifest_manager or DatabaseManifestManager()
        self.model = model
        self.auto_start_corenlp = auto_start_corenlp

        # External service clients for parallel processing
        self.corenlp_client = corenlp_client
        self.rate_limiter = rate_limiter

        # Initialize stage processors lazily to avoid startup overhead
        self._pdf_extractor = None
        self._paper_extractor = None
        self._attributor = None
        self._adapter = None
        self._dedup_analyzer = None
        self._complete_processor = None
        self._consolidator = None

        logger.info(f"StoragePipeline initialized with model: {model}")

    def _get_pdf_path_from_manifest(self, manifest: JobManifest) -> str:
        """Get PDF download URL from Supabase storage using manifest info"""
        try:
            # Get PDF URL from Supabase using the paper_id (files are stored as paper_id.pdf)
            if not manifest.paper_id:
                raise ValueError(
                    f"No paper_id found in manifest for doc_id: {manifest.doc_id}"
                )

            # Debug log to see what IDs we have
            logger.info(
                f"🔍 PDF Retrieval - doc_id: {manifest.doc_id}, paper_id: {manifest.paper_id}"
            )
            storage_filename = f"{manifest.paper_id}.pdf"
            pdf_url = get_pdf_download_url(storage_filename)

            if not pdf_url:
                raise ValueError(
                    f"Failed to generate signed URL for {storage_filename}"
                )

            logger.info(f"📁 Retrieved PDF URL for paper_id: {manifest.paper_id}")
            return pdf_url
        except Exception as e:
            logger.error(
                f"Failed to get PDF URL for paper_id {manifest.paper_id} (doc_id: {manifest.doc_id}): {e}"
            )
            raise ValueError(f"Could not retrieve PDF for processing: {e}")

    def _extract_and_save_title(
        self, doc_id: str, structured_data: dict, manifest: JobManifest
    ) -> None:
        """
        Extract title from structured data and save it to the paper record.

        Parses the structured_data JSON to find elements with Type='Title',
        extracts the text, and updates the papers table.

        Args:
            doc_id: Document/extraction run ID
            structured_data: Adobe/Azure structured data (contains elements array)
            manifest: Job manifest with paper_id
        """
        try:
            if not manifest.paper_id:
                logger.warning(f"No paper_id in manifest for {doc_id}, skipping title extraction")
                return

            # Find title element in structured data
            # Format: {"Type": "Title", "Text": "Paper Title Here", ...}
            title = None
            elements = structured_data.get("elements", [])

            for element in elements:
                if element.get("Type") == "Title" or element.get("Type") == "title":
                    title = element.get("Text", "").strip()
                    if title:
                        break

            if not title:
                logger.info(f"📄 No title found in structured data for {doc_id}, keeping existing title")
                return

            # Update paper record with extracted title
            from app.db.supabase_client import service_client

            sb = service_client()
            result = (
                sb.table("papers")
                .update({"title": title})
                .eq("id", manifest.paper_id)
                .execute()
            )

            if result.data:
                logger.info(f"📝 Updated paper title: {title[:60]}{'...' if len(title) > 60 else ''}")
            else:
                logger.warning(f"⚠️  Failed to update title for paper {manifest.paper_id}")

        except Exception as e:
            # Non-fatal - log error but don't fail the pipeline
            logger.error(f"❌ Error extracting title for {doc_id}: {e}")
            logger.error("   Pipeline will continue with existing title")

    def _store_artifact_in_database(
        self, doc_id: str, stage: str, artifact_name: str, content: dict
    ) -> None:
        """Store artifact using job_artifacts table via job_service"""
        try:
            from app.services.jobs.job_service import get_job_service

            job_service = get_job_service()

            # Sanitize content to remove null bytes and problematic Unicode chars
            sanitized_content = _sanitize_for_database(content)

            success = job_service.store_artifact(
                doc_id, stage, artifact_name, sanitized_content
            )
            if not success:
                raise ValueError(f"Failed to store artifact {artifact_name}")

            logger.debug(
                f"Stored artifact {stage}/{artifact_name} in job_artifacts table"
            )

        except Exception as e:
            logger.error(f"Failed to store artifact {stage}/{artifact_name}: {e}")
            raise

    def _get_artifact_from_database(
        self, doc_id: str, stage: str, artifact_name: str
    ) -> dict:
        """Get artifact using job_artifacts table via job_service"""
        try:
            from app.services.jobs.job_service import get_job_service

            job_service = get_job_service()

            artifact_data = job_service.get_artifact(doc_id, stage, artifact_name)
            if not artifact_data:
                raise ValueError(f"Artifact {artifact_name} not found")

            return artifact_data

        except Exception as e:
            logger.error(f"Failed to get artifact {stage}/{artifact_name}: {e}")
            raise

    @property
    def pdf_extractor(self) -> PDFExtractor:
        """Lazy initialization of PDF extractor"""
        if self._pdf_extractor is None:
            self._pdf_extractor = PDFExtractor()
        return self._pdf_extractor

    @property
    def paper_extractor(self) -> PaperExtractor:
        """Lazy initialization of paper extractor"""
        if self._paper_extractor is None:
            self._paper_extractor = PaperExtractor(
                model=self.model, rate_limiter=self.rate_limiter
            )
        return self._paper_extractor

    @property
    def attributor(self) -> SourceAttributor:
        """Lazy initialization of source attributor"""
        if self._attributor is None:
            self._attributor = SourceAttributor()
        return self._attributor

    @property
    def adapter(self) -> ExtractAdapter:
        """Lazy initialization of extract adapter"""
        if self._adapter is None:
            self._adapter = ExtractAdapter()
        return self._adapter

    @property
    def dedup_analyzer(self) -> LogicalDuplicateAnalyzer:
        """Lazy initialization of deduplication analyzer"""
        if self._dedup_analyzer is None:
            self._dedup_analyzer = LogicalDuplicateAnalyzer()
        return self._dedup_analyzer

    @property
    def complete_processor(self) -> CompletePipelineProcessor:
        """Lazy initialization of complete pipeline processor"""
        if self._complete_processor is None:
            self._complete_processor = CompletePipelineProcessor()
        return self._complete_processor

    @property
    def consolidator(self) -> FinalConsolidator:
        """Lazy initialization of final consolidator"""
        if self._consolidator is None:
            # Use database-based consolidator with optional storage_root
            self._consolidator = FinalConsolidator()
        return self._consolidator

    def _transform_extraction_to_attribution_format(self, extraction_data):
        """
        Transform extraction output to the format expected by SourceAttributor.

        Args:
            extraction_data: JSON from extract pipeline

        Returns:
            Tuple of (claims_list, evidence_list) in SourceAttributor format
        """
        claims_list = []
        evidence_list = []

        # Use extraction data directly (new format)
        results = extraction_data

        # Transform claims
        if "claims" in results and "claims" in results["claims"]:
            for claim in results["claims"]["claims"]:
                # Use verbatim_statement from _dspy_raw if available (for better attribution matching)
                text = claim.get("_dspy_raw", {}).get(
                    "verbatim_statement"
                ) or claim.get("claim", "")
                claims_list.append(
                    {
                        "id": claim["claim_id"],
                        "text": text,
                        "hints": {},  # No page hints available from extraction
                    }
                )

        # Transform evidence
        if "evidence" in results and "evidence_groups" in results["evidence"]:
            for group in results["evidence"]["evidence_groups"]:
                for evidence in group.get("evidence_list", []):
                    # Use verbatim_statement from _dspy_raw if available (for better attribution matching)
                    text = evidence.get("_dspy_raw", {}).get(
                        "verbatim_statement"
                    ) or evidence.get("evidence", "")
                    evidence_list.append(
                        {
                            "id": evidence["evidence_id"],
                            "text": text,
                            "hints": {},  # No page hints available from extraction
                        }
                    )

        return claims_list, evidence_list

    def _update_extracts_with_attribution(
        self,
        doc_id: str,
        attribution_result: Dict[str, Any],
        extract_ids_data: Dict[str, Any],
    ):
        """
        Update existing extract records with source_location from attribution

        Args:
            doc_id: Document identifier
            attribution_result: Attribution result with matches
            extract_ids_data: Extract IDs data from extract stage metadata
        """
        from app.db.queries import extracts as extracts_queries
        from app.db.supabase_client import service_client
        from app.models.db_models import BoundingBox, SourceLocation

        logger.info("📍 Updating extracts with source locations...")

        claim_uuid_mapping = extract_ids_data.get("claim_uuid_mapping", {})
        evidence_uuid_mapping = extract_ids_data.get("evidence_uuid_mapping", {})

        # Build updates list
        updates_list = []

        # Process attributions array (new format from SourceAttributor)
        attributions = attribution_result.get("attributions", [])
        for attribution in attributions:
            target = attribution.get("target", {})
            match = attribution.get("match", {})

            target_id = target.get("id")
            target_type = target.get("type")

            if not target_id or not match:
                continue

            # Map to UUID based on type
            uuid_mapping = (
                claim_uuid_mapping if target_type == "claim" else evidence_uuid_mapping
            )
            if target_id not in uuid_mapping:
                continue

            extract_uuid = uuid_mapping[target_id]

            # Build source location from match data
            if "page" in match:
                bbox = None
                if match.get("bounding_box"):
                    bbox_data = match["bounding_box"]
                    bbox = BoundingBox(
                        x=bbox_data.get("x", 0),
                        y=bbox_data.get("y", 0),
                        w=bbox_data.get("width", bbox_data.get("w", 0)),
                        h=bbox_data.get("height", bbox_data.get("h", 0)),
                    )
                source_location = SourceLocation(page=match["page"], bbox=bbox)

                updates_list.append(
                    {
                        "id": extract_uuid,
                        "source_location": source_location.model_dump(),
                    }
                )

        # Perform bulk update
        if updates_list:
            sb = service_client()
            updated_count = extracts_queries.bulk_update_extracts(sb, updates_list)
            logger.info(f"✅ Updated {updated_count} extracts with source locations")
        else:
            logger.info("ℹ️  No source locations to update")

    def _update_extracts_with_fol(
        self, doc_id: str, fol_result: Dict[str, Any], extract_ids_data: Dict[str, Any]
    ):
        """
        Update existing extract records with fol_json from NLP2FOL

        Args:
            doc_id: Document identifier
            fol_result: NLP2FOL result with logical representations
            extract_ids_data: Extract IDs data from extract stage metadata
        """
        from app.db.queries import extracts as extracts_queries
        from app.db.supabase_client import service_client

        logger.info("🧠 Updating extracts with FOL data...")

        claim_uuid_mapping = extract_ids_data.get("claim_uuid_mapping", {})

        # Build updates list
        updates_list = []

        # Process FOL results for claims
        nlp2fol_results = fol_result.get("nlp2fol_results", [])
        for fol_item in nlp2fol_results:
            element_id = fol_item.get("element_id")  # This is the LLM claim ID
            logical_ast = fol_item.get("logical_ast")

            if element_id in claim_uuid_mapping and logical_ast:
                extract_uuid = claim_uuid_mapping[element_id]

                # Merge FOL data with existing fol_json (preserves DSPy data if present)
                updates_list.append(
                    {
                        "id": extract_uuid,
                        "fol_json": {
                            "logical_ast": logical_ast,
                            "status": fol_item.get("status"),
                            "nlp2fol_metadata": {
                                "completion_summary": fol_result.get(
                                    "pipeline_completion_summary", {}
                                ),
                                "element_id": element_id,
                            },
                        },
                    }
                )

        # Perform bulk update
        if updates_list:
            sb = service_client()
            updated_count = extracts_queries.bulk_update_extracts(sb, updates_list)
            logger.info(f"✅ Updated {updated_count} extracts with FOL data")
        else:
            logger.info("ℹ️  No FOL data to update")

    async def process_document(
        self, doc_id: str, skip_stages: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Process a document through all pipeline stages

        Args:
            doc_id: Document identifier
            skip_stages: List of stages to skip (for testing/debugging)

        Returns:
            Processing results summary
        """
        skip_stages = skip_stages or []

        # Load job manifest from database
        manifest = self.manifest_manager.load_job_manifest(doc_id)
        if not manifest:
            raise ValueError(f"Manifest not found for doc_id: {doc_id}")

        logger.info(f"🚀 Starting pipeline processing for {doc_id}")
        logger.info(f"   File: {manifest.file_info.original_filename}")
        logger.info(f"   Field: {manifest.field or 'Not specified'}")
        logger.info(f"   Topic: {manifest.topic or 'Not specified'}")

        results = {
            "doc_id": doc_id,
            "stages_completed": [],
            "stage_results": {},
            "total_duration": 0.0,
            "errors": [],
        }

        pipeline_start = datetime.utcnow()

        try:
            # Stage 1: Ingest (PDF → Structured Data)
            if "ingest" not in skip_stages:
                results["stage_results"]["ingest"] = await self._run_ingest_stage(
                    doc_id, manifest
                )
                results["stages_completed"].append("ingest")

            # Stage 2: Extract (Structured Data → Claims/Evidence)
            if "extract" not in skip_stages:
                # Reload manifest to get updated artifact paths
                manifest = self.manifest_manager.load_job_manifest(doc_id)
                results["stage_results"]["extract"] = await self._run_extract_stage(
                    doc_id, manifest
                )
                results["stages_completed"].append("extract")

            # Stage 3: Attribution (Link Claims/Evidence to Source)
            if "attribution" not in skip_stages:
                # Reload manifest to get updated artifact paths
                manifest = self.manifest_manager.load_job_manifest(doc_id)
                results["stage_results"]["attribution"] = self._run_attribution_stage(
                    doc_id, manifest
                )
                results["stages_completed"].append("attribution")

            # Stage 4: NLP2FOL (Convert to First-Order Logic)
            if "nlp2fol" not in skip_stages:
                # Reload manifest to get updated artifact paths
                manifest = self.manifest_manager.load_job_manifest(doc_id)
                results["stage_results"]["nlp2fol"] = self._run_nlp2fol_stage(
                    doc_id, manifest
                )
                results["stages_completed"].append("nlp2fol")

            # Stage 5: Deduplication (Remove Logical Duplicates)
            if "deduplication" not in skip_stages:
                # Reload manifest to get updated artifact paths
                manifest = self.manifest_manager.load_job_manifest(doc_id)
                results["stage_results"]["deduplication"] = (
                    self._run_deduplication_stage(doc_id, manifest)
                )
                results["stages_completed"].append("deduplication")

            # Stage 6: Consolidation (Create Final Output)
            if "consolidation" not in skip_stages:
                # Reload manifest to get updated artifact paths
                manifest = self.manifest_manager.load_job_manifest(doc_id)
                results["stage_results"]["consolidation"] = (
                    self._run_consolidation_stage(doc_id, manifest)
                )
                results["stages_completed"].append("consolidation")

            # Calculate total duration
            pipeline_end = datetime.utcnow()
            results["total_duration"] = (pipeline_end - pipeline_start).total_seconds()

            # Update job status to completed
            updated_manifest = self.manifest_manager.load_job_manifest(doc_id)
            if updated_manifest and updated_manifest.status.value != "failed":
                updated_manifest.total_duration_seconds = results["total_duration"]
                self.manifest_manager.save_job_manifest(updated_manifest)

            logger.info(
                f"🎉 Pipeline completed for {doc_id} in {results['total_duration']:.2f}s"
            )

        except Exception as e:
            logger.error(f"❌ Pipeline failed for {doc_id}: {e}")
            results["errors"].append(str(e))

            # Mark job as failed
            try:
                self.manifest_manager.update_stage_status(
                    doc_id,
                    "pipeline",
                    StageStatus.FAILED,
                    error_message=str(e),
                    finished_at=datetime.utcnow(),
                )
            except Exception as update_error:
                logger.error(f"Failed to update error status: {update_error}")

            raise

        return results

    async def _run_ingest_stage(
        self, doc_id: str, manifest: JobManifest
    ) -> Dict[str, Any]:
        """Run the ingest stage (PDF → Structured Data) - DATABASE ONLY"""
        from app.core.config import settings

        # Get provider with fallback to adobe
        provider = getattr(settings, "INGEST_PROVIDER", "adobe").lower()
        if provider not in ["adobe", "azure"]:
            logger.warning(
                f"Invalid INGEST_PROVIDER '{provider}', falling back to 'adobe'"
            )
            provider = "adobe"

        logger.info(f"📄 Stage 1: PDF Ingest (Provider: {provider})")

        # Update stage status
        self.manifest_manager.update_stage_status(
            doc_id, "ingest", StageStatus.RUNNING, started_at=datetime.utcnow()
        )

        try:
            # Get PDF URL from Supabase storage using manifest info
            pdf_url = self._get_pdf_path_from_manifest(manifest)

            # Download PDF content
            import requests

            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code != 200:
                raise ValueError(f"Failed to download PDF from {pdf_url}")

            pdf_content = pdf_response.content

            # Branch based on provider
            if provider == "azure":
                # Azure path - async call, no temp files needed
                structured_data = await self._run_azure_ingest(
                    pdf_content, doc_id, manifest.file_info.original_filename
                )
            else:
                # Adobe path - keep existing logic
                structured_data = self._run_adobe_ingest(
                    pdf_content, manifest.file_info.original_filename
                )

            # Store structured data directly in database (same for both providers)
            self._store_artifact_in_database(
                doc_id, "ingest", "structured_data", structured_data
            )

            # Extract and save title from structured data to paper record
            self._extract_and_save_title(doc_id, structured_data, manifest)

            # Update stage as completed
            self.manifest_manager.update_stage_status(
                doc_id,
                "ingest",
                StageStatus.COMPLETED,
                finished_at=datetime.utcnow(),
                metadata={
                    "provider": provider,
                    "output_data": "stored_in_database",
                },
            )

            logger.info(f"✅ Ingest completed with {provider.upper()}")

            return {
                "status": "completed",
                "structured_data": "stored_in_database",
                "provider": provider,
            }

        except Exception as e:
            logger.error(f"Ingest stage failed: {e}")
            self.manifest_manager.update_stage_status(
                doc_id,
                "ingest",
                StageStatus.FAILED,
                finished_at=datetime.utcnow(),
                error_message=str(e),
            )
            raise

    def _run_adobe_ingest(self, pdf_content: bytes, filename: str) -> dict:
        """Run Adobe PDF Services ingestion."""
        # Save PDF content to temporary file for Adobe API
        import json
        import os
        import tempfile

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            temp_pdf.write(pdf_content)
            temp_pdf_path = temp_pdf.name

        try:
            # Process PDF using Adobe API
            logger.info(f"Processing PDF with Adobe API: {filename}")
            structured_json_path = self.pdf_extractor.extract_pdf(temp_pdf_path)

            # Load the structured data
            with open(structured_json_path, "r") as f:
                structured_data = json.load(f)

            # Clean up temporary files
            os.unlink(temp_pdf_path)
            os.unlink(structured_json_path)

            return structured_data

        except Exception as e:
            # Clean up temp file on error
            if os.path.exists(temp_pdf_path):
                os.unlink(temp_pdf_path)
            raise e

    async def _run_azure_ingest(
        self, pdf_content: bytes, doc_id: str, filename: str
    ) -> dict:
        """Run Azure Document Intelligence ingestion."""
        from app.services.ingest.adapters.azure_to_adobe import convert_azure_to_adobe
        from app.services.ingest.azure_layout_client import AzureLayoutClient

        try:
            logger.info(f"Processing PDF with Azure Document Intelligence: {filename}")

            # Step 1: Call Azure Layout API
            client = AzureLayoutClient()
            azure_response = await client.analyze_document(pdf_content, filename)

            # Step 2: Store raw Azure response as azure_raw artifact
            # DISABLED: Large responses cause DB timeout, we only need the converted format
            # self._store_artifact_in_database(
            #     doc_id, "ingest", "azure_raw", azure_response
            # )
            # logger.debug(f"Stored raw Azure response for {doc_id}")

            # Step 3: Convert to Adobe-compatible format
            adobe_compatible_data = convert_azure_to_adobe(azure_response)

            logger.info(
                f"✅ Azure Document Intelligence processing completed for {filename}"
            )
            logger.info(
                f"   Elements extracted: {len(adobe_compatible_data.get('elements', []))}"
            )
            logger.info(
                f"   Pages processed: {len(adobe_compatible_data.get('pages', []))}"
            )

            return adobe_compatible_data

        except Exception as e:
            logger.error(
                f"❌ Azure Document Intelligence processing failed for {filename}: {e}"
            )
            raise

    async def _run_extract_stage(
        self, doc_id: str, manifest: JobManifest
    ) -> Dict[str, Any]:
        """Run the extract stage (Structured Data → Claims/Evidence)"""
        logger.info("🔍 Stage 2: Claims/Evidence Extraction")

        # Update stage status
        self.manifest_manager.update_stage_status(
            doc_id, "extract", StageStatus.RUNNING, started_at=datetime.utcnow()
        )

        try:
            # Get ingest output from database manifest
            ingest_artifact_data = self._get_artifact_from_database(
                doc_id, "ingest", "structured_data"
            )
            if not ingest_artifact_data:
                raise ValueError("Ingest artifact not found")

            # Determine paper ID and context
            paper_id = manifest.paper_id
            field = manifest.field or "general"
            topic = manifest.topic or "research"

            # Use ingest data directly from database
            ingest_data = ingest_artifact_data

            # Extract content from Adobe structure
            content = ""
            if "elements" in ingest_data:
                for element in ingest_data["elements"]:
                    if element.get("Text"):
                        content += element["Text"] + "\n"

            # Run extraction WITH extraction_run_id for database writes
            logger.debug(f"Extracting from: {paper_id} (ingest data loaded)")
            extract_result = await self.paper_extractor.extract_both(
                field=field,
                topic=topic,
                title=f"Paper: {paper_id}",
                content=content,
                paper_id=paper_id,
                extraction_run_id=doc_id,  # NEW: Pass doc_id for DB writes
            )

            # Store extraction result directly in database
            self._store_artifact_in_database(
                doc_id, "extract", "claims_evidence", extract_result
            )

            # Update stage as completed
            claims_count = len(extract_result.get("claims", {}).get("claims", []))
            evidence_count = len(
                extract_result.get("evidence", {}).get("evidence_groups", [])
            )

            # Extract extract_ids for tracking
            extract_ids = extract_result.get("extract_ids", {})

            self.manifest_manager.update_stage_status(
                doc_id,
                "extract",
                StageStatus.COMPLETED,
                finished_at=datetime.utcnow(),
                metadata={
                    "model": self.model,
                    "claims_count": claims_count,
                    "evidence_count": evidence_count,
                    "field": field,
                    "topic": topic,
                    "extract_ids": extract_ids,  # NEW: Store extract UUIDs
                },
            )

            logger.info(
                f"✅ Extraction completed: {claims_count} claims, {evidence_count} evidence groups"
            )

            return {
                "status": "completed",
                "extract_data": "stored_in_database",
                "claims_count": claims_count,
                "evidence_count": evidence_count,
            }

        except Exception as e:
            logger.error(f"Extract stage failed: {e}")
            self.manifest_manager.update_stage_status(
                doc_id,
                "extract",
                StageStatus.FAILED,
                finished_at=datetime.utcnow(),
                error_message=str(e),
            )
            raise

    def _run_attribution_stage(
        self, doc_id: str, manifest: JobManifest
    ) -> Dict[str, Any]:
        """Run the attribution stage (Link Claims/Evidence to Source)"""
        logger.info("📍 Stage 3: Source Attribution")

        # Update stage status
        self.manifest_manager.update_stage_status(
            doc_id, "attribution", StageStatus.RUNNING, started_at=datetime.utcnow()
        )

        try:
            # Get input artifacts from database manifest
            ingest_artifact_data = self._get_artifact_from_database(
                doc_id, "ingest", "structured_data"
            )
            extract_artifact_data = self._get_artifact_from_database(
                doc_id, "extract", "claims_evidence"
            )

            if not ingest_artifact_data or not extract_artifact_data:
                raise ValueError("Required artifacts not found for attribution")

            # Use extraction data directly from database
            extraction_data = extract_artifact_data

            # Transform extraction data to attribution format
            claims_list, evidence_list = (
                self._transform_extraction_to_attribution_format(extraction_data)
            )

            # Use Adobe JSON directly from database
            adobe_json = ingest_artifact_data

            # Run attribution
            paper_id = manifest.file_info.original_filename.rsplit(".", 1)[0]
            source_file = manifest.file_info.original_filename

            attribution_result = self.attributor.run(
                adobe_json,
                claims_list,
                evidences=evidence_list,
                paper_id=paper_id,
                source_file=source_file,
            )

            # Store attribution result directly in database
            self._store_artifact_in_database(
                doc_id, "attribution", "links", attribution_result
            )

            # NEW: Update extract records with source_location data
            extract_metadata = self.manifest_manager.get_stage_metadata(
                doc_id, "extract"
            )
            if extract_metadata and "extract_ids" in extract_metadata:
                self._update_extracts_with_attribution(
                    doc_id=doc_id,
                    attribution_result=attribution_result,
                    extract_ids_data=extract_metadata["extract_ids"],
                )

            # Extract metrics
            metadata = attribution_result.get("metadata", {})

            self.manifest_manager.update_stage_status(
                doc_id,
                "attribution",
                StageStatus.COMPLETED,
                finished_at=datetime.utcnow(),
                metadata={
                    "total_items": metadata.get("total_items", 0),
                    "matched": metadata.get("matched", 0),
                    "match_rate": metadata.get("match_rate", 0.0),
                },
            )

            logger.info(
                f"✅ Attribution completed: {metadata.get('match_rate', 0):.1%} match rate"
            )

            return {
                "status": "completed",
                "attribution_data": "stored_in_database",
                "match_rate": metadata.get("match_rate", 0.0),
            }

        except Exception as e:
            logger.error(f"Attribution stage failed: {e}")
            self.manifest_manager.update_stage_status(
                doc_id,
                "attribution",
                StageStatus.FAILED,
                finished_at=datetime.utcnow(),
                error_message=str(e),
            )
            raise

    def _run_nlp2fol_stage(self, doc_id: str, manifest: JobManifest) -> Dict[str, Any]:
        """Run the NLP2FOL stage (Convert to First-Order Logic)"""
        logger.info("🧠 Stage 4: NLP2FOL Processing")

        # Update stage status
        self.manifest_manager.update_stage_status(
            doc_id, "nlp2fol", StageStatus.RUNNING, started_at=datetime.utcnow()
        )

        try:
            # Ensure CoreNLP is running for complete logical pipeline
            if self.auto_start_corenlp:
                try:
                    ensure_corenlp_running()
                    logger.info("✅ CoreNLP server is available")
                except Exception as e:
                    logger.warning(f"⚠️  CoreNLP server check failed: {e}")
                    logger.warning(
                        "Pipeline will continue but may use fallback processing"
                    )

            # Get extract artifact from database manifest
            extract_artifact_data = self._get_artifact_from_database(
                doc_id, "extract", "claims_evidence"
            )
            if not extract_artifact_data:
                raise ValueError("Extract artifact not found for NLP2FOL")

            # Use extract data directly from database
            extract_data = extract_artifact_data

            # Run COMPLETE NLP2FOL processing (not just adapter)
            logger.debug(f"Processing complete FOL pipeline from database artifact")

            # Step 1: Convert extract to nlp2fol input format
            nlp2fol_input = self.adapter.process_extract_output(extract_data)

            # Step 2: Run through complete logical pipeline
            fol_result = self.complete_processor.process_claims_and_evidence(
                nlp2fol_input
            )

            # Store FOL result directly in database
            self._store_artifact_in_database(
                doc_id, "nlp2fol", "fol_results", fol_result
            )

            # NEW: Update extract records with FOL data
            extract_metadata = self.manifest_manager.get_stage_metadata(
                doc_id, "extract"
            )
            if extract_metadata and "extract_ids" in extract_metadata:
                self._update_extracts_with_fol(
                    doc_id=doc_id,
                    fol_result=fol_result,
                    extract_ids_data=extract_metadata["extract_ids"],
                )

            # Extract metrics from complete pipeline
            completion_summary = fol_result.get("pipeline_completion_summary", {})
            nlp2fol_results = fol_result.get("nlp2fol_results", [])

            # Count items with logical AST
            items_with_ast = sum(
                1
                for item in nlp2fol_results
                if "logical_ast" in item and item.get("status") == "completed"
            )
            total_items = len(nlp2fol_results)
            failed_items = completion_summary.get("failed", 0)

            # Calculate logical complexity metrics
            total_features = completion_summary.get("total_logical_features", 0)
            total_operations = completion_summary.get("total_logic_operations", 0)
            total_variables = completion_summary.get("total_bound_variables", 0)

            self.manifest_manager.update_stage_status(
                doc_id,
                "nlp2fol",
                StageStatus.COMPLETED,
                finished_at=datetime.utcnow(),
                metadata={
                    "total_items": total_items,
                    "items_with_logical_ast": items_with_ast,
                    "failed_items": failed_items,
                    "completion_rate": completion_summary.get("completion_rate", 0.0),
                    "logical_features_detected": total_features,
                    "logic_operations": total_operations,
                    "bound_variables": total_variables,
                    "fallback_usage": completion_summary.get("fallback_usage", 0),
                    "corenlp_version": "4.5.10",
                    "pipeline_components_added": ", ".join(
                        completion_summary.get("pipeline_components_added", [])
                    ),
                },
            )

            logger.info(
                f"✅ Complete NLP2FOL pipeline completed: {items_with_ast}/{total_items} items with logical AST"
            )
            logger.info(
                f"   Logical features: {total_features}, Operations: {total_operations}, Variables: {total_variables}"
            )
            if failed_items > 0:
                logger.warning(
                    f"   ⚠️  {failed_items} items failed, check results for details"
                )

            return {
                "status": "completed",
                "fol_data": "stored_in_database",
                "total_items": total_items,
                "items_with_logical_ast": items_with_ast,
                "failed_items": failed_items,
                "completion_rate": completion_summary.get("completion_rate", 0.0),
                "logical_features": total_features,
                "logic_operations": total_operations,
                "bound_variables": total_variables,
            }

        except Exception as e:
            logger.error(f"NLP2FOL stage failed: {e}")
            self.manifest_manager.update_stage_status(
                doc_id,
                "nlp2fol",
                StageStatus.FAILED,
                finished_at=datetime.utcnow(),
                error_message=str(e),
            )
            raise

    # def _run_deduplication_stage(
    #     self, doc_id: str, manifest: JobManifest
    # ) -> Dict[str, Any]:
    #     """Run the deduplication stage (Remove Logical Duplicates)"""
    #     logger.info("🔄 Stage 5: Logical Deduplication")

    #     # Update stage status
    #     self.manifest_manager.update_stage_status(
    #         doc_id, "deduplication", StageStatus.RUNNING, started_at=datetime.utcnow()
    #     )

    #     try:
    #         # Get NLP2FOL artifact from database manifest
    #         nlp2fol_artifact_data = self._get_artifact_from_database(
    #             doc_id, "nlp2fol", "fol_results"
    #         )
    #         if not nlp2fol_artifact_data:
    #             raise ValueError("NLP2FOL artifact not found for deduplication")

    #         # Use NLP2FOL data directly from database
    #         nlp2fol_data = nlp2fol_artifact_data

    #         # Run duplicate analysis
    #         logger.debug(f"Analyzing duplicates from database artifact")
    #         duplicate_analysis = self.dedup_analyzer.analyze_results(nlp2fol_data)

    #         # Create deduplicated dataset
    #         deduplicated_dataset = self.dedup_analyzer.create_deduplicated_dataset(
    #             duplicate_analysis
    #         )

    #         logger.info(f"Dedup output keys: {deduplicated_dataset.keys()}")
    #         logger.info(f"Logical statements count: {len(deduplicated_dataset.get('logical_statements', []))}")

    #         # Store both analysis and deduplicated dataset directly in database
    #         self._store_artifact_in_database(
    #             doc_id, "deduplication", "analysis", duplicate_analysis
    #         )
    #         self._store_artifact_in_database(
    #             doc_id, "deduplication", "deduplicated_dataset", deduplicated_dataset
    #         )

    #         # Extract metrics
    #         stats = duplicate_analysis.get("stats", {})
    #         dedup_stats = deduplicated_dataset.get("deduplication_stats", {})

    #         self.manifest_manager.update_stage_status(
    #             doc_id,
    #             "deduplication",
    #             StageStatus.COMPLETED,
    #             finished_at=datetime.utcnow(),
    #             metadata={
    #                 "duplicate_groups": stats.get("duplicate_groups", 0),
    #                 "total_duplicates": stats.get("total_duplicates", 0),
    #                 "compression_achieved": dedup_stats.get(
    #                     "compression_achieved", 0.0
    #                 ),
    #                 "logical_statements": dedup_stats.get("logical_statements", 0),
    #             },
    #         )

    #         logger.info(
    #             f"✅ Deduplication completed: {stats.get('duplicate_groups', 0)} duplicate groups found"
    #         )
    #         logger.info(
    #             f"   Compression: {dedup_stats.get('compression_achieved', 0):.1%}"
    #         )

    #         return {
    #             "status": "completed",
    #             "analysis_data": "stored_in_database",
    #             "dataset_data": "stored_in_database",
    #             "duplicate_groups": stats.get("duplicate_groups", 0),
    #             "compression_achieved": dedup_stats.get("compression_achieved", 0.0),
    #         }

    #     except Exception as e:
    #         logger.error(f"Deduplication stage failed: {e}")
    #         self.manifest_manager.update_stage_status(
    #             doc_id,
    #             "deduplication",
    #             StageStatus.FAILED,
    #             finished_at=datetime.utcnow(),
    #             error_message=str(e),
    #         )
    #         raise

    def _run_deduplication_stage(
        self, doc_id: str, manifest: JobManifest
    ) -> Dict[str, Any]:
        """Run the deduplication stage (Remove Logical Duplicates)"""
        logger.info("🔄 Stage 5: Logical Deduplication")

        # QUICK FIX: Skip deduplication, pass through NLP2FOL results
        nlp2fol_artifact_data = self._get_artifact_from_database(
            doc_id, "nlp2fol", "fol_results"
        )

        # Create passthrough deduplicated dataset from NLP2FOL
        passthrough_dataset = {
            "document_info": nlp2fol_artifact_data.get("document_info", {}),
            "deduplication_stats": {
                "original_statements": len(
                    nlp2fol_artifact_data.get("nlp2fol_results", [])
                ),
                "logical_statements": len(
                    nlp2fol_artifact_data.get("nlp2fol_results", [])
                ),
                "compression_achieved": 0.0,
                "duplicate_groups": 0,
            },
            "acronyms": nlp2fol_artifact_data.get("acronyms", {}),
            # Convert nlp2fol_results to logical_statements format
            "logical_statements": [
                {
                    "logical_id": f"LS_{item['id']}",
                    "primary_id": item["id"],
                    "primary_type": item["type"],
                    "primary_text": item.get("original_text", ""),
                    "logical_form": {},  # Empty for now
                    "duplicate_count": 1,
                    "types_involved": [item["type"]],
                }
                for item in nlp2fol_artifact_data.get("nlp2fol_results", [])
                if item.get("status") == "completed"
            ],
        }

        # Store the passthrough dataset
        self._store_artifact_in_database(
            doc_id, "deduplication", "deduplicated_dataset", passthrough_dataset
        )

        # Update stage as completed
        self.manifest_manager.update_stage_status(
            doc_id,
            "deduplication",
            StageStatus.COMPLETED,
            finished_at=datetime.utcnow(),
            metadata={
                "skipped": True,
                "reason": "Deduplication bypassed - using NLP2FOL results directly",
                "logical_statements": len(passthrough_dataset["logical_statements"]),
            },
        )

        logger.info(
            f"✅ Deduplication bypassed - passing through {len(passthrough_dataset['logical_statements'])} statements"
        )

        return {
            "status": "completed",
            "dataset_data": "stored_in_database",
            "logical_statements": len(passthrough_dataset["logical_statements"]),
        }

    def _run_consolidation_stage(
        self, doc_id: str, manifest: JobManifest
    ) -> Dict[str, Any]:
        """Run the consolidation stage (Create Final Output)"""
        logger.info("📦 Stage 6: Final Output Consolidation")

        # Update stage status
        self.manifest_manager.update_stage_status(
            doc_id, "consolidation", StageStatus.RUNNING, started_at=datetime.utcnow()
        )

        try:
            # Create consolidated final output - this writes to database (extracts table)
            final_output = self.consolidator.consolidate_job_results(doc_id, manifest)

            # Skip JSON artifact storage - we only need database writes for extracts/evidence_claims

            # Extract metrics
            stats = final_output.processing_stats
            doc_metadata = final_output.document

            self.manifest_manager.update_stage_status(
                doc_id,
                "consolidation",
                StageStatus.COMPLETED,
                finished_at=datetime.utcnow(),
                metadata={
                    "total_statements": len(final_output.logical_statements),
                    "claims": len(final_output.get_claims()),
                    "evidence": len(final_output.get_evidence()),
                    "statements_with_logic": len(
                        final_output.get_statements_with_logic()
                    ),
                    "schema_version": final_output.schema_version,
                    "compression_achieved": stats.compression_achieved,
                    "final_data_stored": "in_database",
                },
            )

            logger.info(
                f"✅ Consolidation completed: {len(final_output.logical_statements)} statements in final output"
            )
            logger.info(
                f"   Claims: {len(final_output.get_claims())}, Evidence: {len(final_output.get_evidence())}"
            )
            logger.info(f"   Data stored in database manifest")

            return {
                "status": "completed",
                "final_data": "stored_in_database",
                "total_statements": len(final_output.logical_statements),
                "claims": (
                    len(final_output.get_claims())
                    if hasattr(final_output, "get_claims")
                    else 0
                ),
                "evidence": (
                    len(final_output.get_evidence())
                    if hasattr(final_output, "get_evidence")
                    else 0
                ),
                "statements_with_logic": (
                    len(final_output.get_statements_with_logic())
                    if hasattr(final_output, "get_statements_with_logic")
                    else 0
                ),
                "schema_version": (
                    final_output.schema_version
                    if hasattr(final_output, "schema_version")
                    else "1.0"
                ),
            }

        except Exception as e:
            logger.error(f"Consolidation stage failed: {e}")
            self.manifest_manager.update_stage_status(
                doc_id,
                "consolidation",
                StageStatus.FAILED,
                finished_at=datetime.utcnow(),
                error_message=str(e),
            )
            raise
