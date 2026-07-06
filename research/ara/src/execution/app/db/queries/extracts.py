# Grounding: transcribed from oshima/api/app/db/queries/extracts.py
#!/usr/bin/env python3
"""
Extracts CRUD operations.

Centralized database operations for extracted claims, evidence, and processing results.
Handles batch operations for pipeline efficiency and claim-evidence relationships.
Migrated from app.db.repositories.extracts_repo with working implementations.
"""

import logging
from typing import Any, Dict, List, Optional, Tuple
from uuid import UUID

from supabase import Client

from app.db.errors import handle_supabase_error
from app.models.db_models import BulkExtractResult, Extract, ExtractIn, ExtractionRun

logger = logging.getLogger(__name__)


def bulk_insert(
    sb: Client, paper_id: UUID, run_id: UUID, items: List[ExtractIn]
) -> BulkExtractResult:
    """
    Bulk insert extracts for a paper and extraction run

    Args:
        sb: Supabase client (service role for background jobs)
        paper_id: Paper UUID
        run_id: Extraction run UUID
        items: List of extract data to insert

    Returns:
        BulkExtractResult: Result with counts and any errors

    Raises:
        DBError: On database operation failure
    """
    try:
        insert_data = []

        for item in items:
            data = item.model_dump()
            data["paper_id"] = str(paper_id)
            data["run_id"] = str(run_id)
            insert_data.append(data)

        response = sb.table("extracts").insert(insert_data).execute()

        return BulkExtractResult(
            inserted_count=len(response.data) if response.data else 0,
            failed_count=0,
            errors=[],
        )

    except Exception as e:
        handle_supabase_error(e)


def bulk_insert_with_relationships(
    sb: Client,
    paper_id: UUID,
    run_id: UUID,
    claims: List[ExtractIn],
    evidence_groups: List[Dict],
    claim_id_mapping: Dict[str, str],
    attribution_map: Optional[Dict[str, Any]] = None,
) -> BulkExtractResult:
    """
    Bulk insert extracts with evidence-claim relationships

    Args:
        sb: Supabase client (service role for background jobs)
        paper_id: Paper UUID
        run_id: Extraction run UUID
        claims: List of claim extracts to insert
        evidence_groups: List of evidence groups with claim_id references
        claim_id_mapping: Mapping from LLM claim_id (e.g., "C1") to canonical IDs
        attribution_map: Optional mapping from item_id to attribution data for source locations

    Returns:
        BulkExtractResult: Result with counts and any errors

    Raises:
        DBError: On database operation failure
    """
    try:
        all_extracts = []
        evidence_claim_relationships = []

        # 1. Prepare claim data
        for claim in claims:
            data = claim.model_dump()
            data["paper_id"] = str(paper_id)
            data["run_id"] = str(run_id)
            all_extracts.append(data)

        # 1.5. Build claim text mapping for duplicate detection
        claim_text_mapping = {}
        for claim in claims:
            # Find the corresponding claim_id from the original claims data
            # We'll need to match by content since we don't have the original IDs here
            claim_text_mapping[claim.content_text.strip().lower()] = claim.content_text

        # 2. Prepare evidence data and collect relationships
        for evidence_group in evidence_groups:
            claim_id = evidence_group.get("claim_id")
            evidence_list = evidence_group.get("evidence_list", [])

            for evidence_item in evidence_list:
                # Skip evidence with empty content
                content = evidence_item.get("statement", "") or evidence_item.get(
                    "evidence", ""
                )
                if not content.strip():
                    continue

                # Skip evidence that has identical text to any claim (case-insensitive)
                content_normalized = content.strip().lower()
                if content_normalized in claim_text_mapping:
                    logger.info(
                        f"🔄 Skipping duplicate evidence that matches claim text: {content[:50]}..."
                    )
                    continue

                # Get source location from attribution data if available
                source_location = None
                evidence_id = evidence_item.get("evidence_id")
                if attribution_map and evidence_id and evidence_id in attribution_map:
                    match_data = attribution_map[evidence_id]
                    from app.models.db_models import BoundingBox, SourceLocation

                    # Check if match_data is already a SourceLocation object
                    if isinstance(match_data, SourceLocation):
                        source_location = match_data
                    else:
                        # match_data is a dictionary, create SourceLocation from it
                        # Create bounding box if available
                        bounding_box = None
                        if match_data.get("bounding_box"):
                            bbox_data = match_data["bounding_box"]
                            bounding_box = BoundingBox(
                                x=bbox_data.get("x", 0),
                                y=bbox_data.get("y", 0),
                                w=bbox_data.get("width", 0),
                                h=bbox_data.get("height", 0),
                            )

                        source_location = SourceLocation(
                            page=match_data.get("page", 0), bbox=bounding_box
                        )
                    logger.debug(f"✅ Added source location for evidence {evidence_id}")

                # Validate extract type and content
                if not content.strip():
                    logger.warning(f"🚫 Skipping evidence with empty content")
                    continue

                # Create ExtractIn for evidence with all critical fields
                evidence_extract = ExtractIn(
                    kind="evidence",  # Ensure valid extract type
                    content_text=content.strip(),  # Critical: content field
                    source_location=source_location,  # Critical: source attribution
                    confidence=evidence_item.get(
                        "confidence", 1.0
                    ),  # Default confidence
                    fol_json=None,  # Evidence typically doesn't have FOL data
                    extract_data={
                        "dspy_raw": evidence_item.get("_dspy_raw"),
                        "evidence_id": evidence_item.get("evidence_id"),
                        "explanation": evidence_item.get("explanation"),
                        "direction": evidence_item.get("direction"),
                        "claim_id": claim_id,  # LLM claim ID (will map to UUID later)
                    },
                )

                evidence_data = evidence_extract.model_dump()
                evidence_data["paper_id"] = str(paper_id)
                evidence_data["run_id"] = str(run_id)
                all_extracts.append(evidence_data)

                # Store relationship info (will resolve UUIDs after insert)
                if claim_id and claim_id in claim_id_mapping:
                    evidence_claim_relationships.append(
                        {
                            "evidence_llm_id": evidence_item.get("evidence_id"),
                            "claim_llm_id": claim_id,
                        }
                    )
                elif claim_id:
                    logger.warning(
                        f"[DEBUG] Evidence has claim_id {claim_id} but it's not in claim_id_mapping (keys: {list(claim_id_mapping.keys())[:5]})"
                    )

        # 3. Insert all extracts at once
        response = sb.table("extracts").insert(all_extracts).execute()
        inserted_extracts = response.data

        if not inserted_extracts:
            return BulkExtractResult(inserted_count=0, failed_count=0, errors=[])

        # 4. Create UUID mappings from the inserted extracts
        evidence_uuid_mapping = {}  # LLM evidence_id -> database UUID

        claim_idx = 0
        evidence_idx = 0

        # Check if we're inserting claims in this batch
        has_claims_in_batch = any(e["kind"] == "claim" for e in inserted_extracts)

        if has_claims_in_batch:
            # Build claim UUID mapping from this batch
            claim_uuid_mapping = {}
        else:
            # No claims in this batch - use the passed-in mapping (from previous write)
            claim_uuid_mapping = claim_id_mapping.copy() if claim_id_mapping else {}
            logger.info(
                f"[DEBUG] Using passed-in claim_id_mapping with {len(claim_uuid_mapping)} entries (no claims in current batch)"
            )

        for extract in inserted_extracts:
            if extract["kind"] == "claim":
                # Map LLM claim ID to database UUID
                llm_claim_id = list(claim_id_mapping.keys())[claim_idx]
                claim_uuid_mapping[llm_claim_id] = extract["id"]
                claim_idx += 1
            elif extract["kind"] == "evidence":
                # Map LLM evidence ID to database UUID
                if evidence_idx < len(evidence_claim_relationships):
                    llm_evidence_id = evidence_claim_relationships[evidence_idx][
                        "evidence_llm_id"
                    ]
                    evidence_uuid_mapping[llm_evidence_id] = extract["id"]
                else:
                    logger.warning(
                        f"[DEBUG] Evidence extract at idx {evidence_idx} has no corresponding relationship entry"
                    )
                evidence_idx += 1

        logger.info(
            f"[DEBUG] Built {len(claim_uuid_mapping)} claim UUID mappings and {len(evidence_uuid_mapping)} evidence UUID mappings"
        )

        # 5. Insert evidence-claim relationships
        relationship_data = []
        for rel in evidence_claim_relationships:
            evidence_llm_id = rel["evidence_llm_id"]
            claim_llm_id = rel["claim_llm_id"]

            if (
                evidence_llm_id in evidence_uuid_mapping
                and claim_llm_id in claim_uuid_mapping
            ):
                relationship_data.append(
                    {
                        "evidence_id": evidence_uuid_mapping[evidence_llm_id],
                        "claim_id": claim_uuid_mapping[claim_llm_id],
                    }
                )

        if relationship_data:
            sb.table("evidence_claims").insert(relationship_data).execute()

        result = BulkExtractResult(
            inserted_count=len(inserted_extracts),
            failed_count=0,
            errors=[],
        )

        # NEW: Attach UUID mappings to result for downstream stages
        result.claim_uuid_mapping = claim_uuid_mapping
        result.evidence_uuid_mapping = evidence_uuid_mapping

        return result

    except Exception as e:
        handle_supabase_error(e)


def list_by_paper_and_kind(sb: Client, paper_id: UUID, kind: str) -> List[Extract]:
    """
    List extracts by paper ID and kind (e.g., 'claim', 'evidence')

    Args:
        sb: Supabase client
        paper_id: Paper UUID
        kind: Extract kind/type

    Returns:
        List[Extract]: List of extracts matching criteria

    Raises:
        DBError: On database operation failure
    """
    try:
        response = (
            sb.table("extracts")
            .select("*")
            .eq("paper_id", str(paper_id))
            .eq("kind", kind)
            .order("created_at")
            .execute()
        )

        return [Extract(**item) for item in response.data]

    except Exception as e:
        handle_supabase_error(e)


def list_by_paper(sb: Client, paper_id: UUID) -> List[Extract]:
    """
    List all extracts for a paper

    Args:
        sb: Supabase client
        paper_id: Paper UUID

    Returns:
        List[Extract]: List of all extracts for the paper

    Raises:
        DBError: On database operation failure
    """
    try:
        response = (
            sb.table("extracts")
            .select("*")
            .eq("paper_id", str(paper_id))
            .order("created_at")
            .execute()
        )

        return [Extract(**item) for item in response.data]

    except Exception as e:
        handle_supabase_error(e)


def get_latest_extracts_for_papers(
    sb: Client, paper_ids: List[UUID], kind: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get extracts from the latest extraction_run for each paper.

    This prevents returning duplicate/stale extracts when papers
    have been reprocessed multiple times.

    Args:
        sb: Supabase client
        paper_ids: List of paper UUIDs
        kind: Optional filter by extract kind ("claim" or "evidence")

    Returns:
        List of extract dicts from latest runs only

    Raises:
        DBError: On database operation failure

    Implementation:
        Uses two-query approach:
        1. Get latest run_id for each paper (MAX(created_at))
        2. Fetch extracts only from those run_ids
    """
    try:
        if not paper_ids:
            return []

        logger.info(
            f"🔍 [get_latest_extracts_for_papers] Getting latest extracts for {len(paper_ids)} papers"
        )

        # Step 1: Get latest run_id per paper
        latest_runs = {}
        for paper_id in paper_ids:
            run_response = (
                sb.table("extraction_runs")
                .select("id, created_at")
                .eq("paper_id", str(paper_id))
                .eq(
                    "job_type", "paper_extraction"
                )  # Only paper extraction runs, not theme extraction
                .order("created_at", desc=True)
                .limit(1)
                .execute()
            )
            if run_response.data:
                run_id = run_response.data[0]["id"]
                created_at = run_response.data[0]["created_at"]
                latest_runs[str(paper_id)] = run_id
                logger.debug(
                    f"  📄 Paper {paper_id}: Latest run_id={run_id} (created_at={created_at})"
                )

        logger.info(
            f"📊 [get_latest_extracts_for_papers] Found latest runs for {len(latest_runs)}/{len(paper_ids)} papers"
        )
        if latest_runs:
            logger.info(
                f"   Latest run_ids being used: {list(latest_runs.values())[:5]}{'...' if len(latest_runs) > 5 else ''}"
            )

        # Step 2: Get extracts only from latest runs
        if not latest_runs:
            logger.warning("⚠️ No extraction runs found for any papers")
            return []

        query = (
            sb.table("extracts")
            .select(
                "id, paper_id, run_id, kind, content_text, confidence, "
                "source_location, extract_data, created_at"
            )
            .in_("run_id", list(latest_runs.values()))
        )

        if kind:
            query = query.eq("kind", kind)

        response = query.execute()
        logger.info(
            f"✅ [get_latest_extracts_for_papers] Retrieved {len(response.data)} extracts from latest runs"
        )

        # Debug: Show breakdown by kind
        if response.data:
            kind_counts = {}
            for extract in response.data:
                kind = extract.get("kind", "unknown")
                kind_counts[kind] = kind_counts.get(kind, 0) + 1
            logger.info(f"   Breakdown by kind: {kind_counts}")

        return response.data

    except Exception as e:
        logger.error(f"❌ Failed to get latest extracts: {e}")
        handle_supabase_error(e)


def get_evidence_for_claims(
    sb: Client, claim_ids: List[UUID]
) -> Dict[UUID, List[Extract]]:
    """
    Get evidence extracts linked to specific claims

    Args:
        sb: Supabase client
        claim_ids: List of claim UUIDs

    Returns:
        Dict mapping claim UUID to list of linked evidence extracts
    """
    try:
        # Query the junction table with joined extract data
        response = (
            sb.table("evidence_claims")
            .select(
                """
                claim_id,
                evidence:evidence_id (
                    id,
                    paper_id,
                    run_id,
                    kind,
                    content_text,
                    fol_json,
                    source_location,
                    confidence,
                    created_at
                )
            """
            )
            .in_("claim_id", [str(cid) for cid in claim_ids])
            .execute()
        )

        # Group evidence by claim
        result = {}
        for row in response.data:
            claim_id = UUID(row["claim_id"])
            evidence_data = row["evidence"]

            if claim_id not in result:
                result[claim_id] = []

            if evidence_data:
                result[claim_id].append(Extract(**evidence_data))

        return result

    except Exception as e:
        handle_supabase_error(e)


def get_claims_for_evidence(
    sb: Client, evidence_ids: List[UUID]
) -> Dict[UUID, List[Extract]]:
    """
    Get claim extracts linked to specific evidence

    Args:
        sb: Supabase client
        evidence_ids: List of evidence UUIDs

    Returns:
        Dict mapping evidence UUID to list of linked claim extracts
    """
    try:
        # Query the junction table with joined extract data
        response = (
            sb.table("evidence_claims")
            .select(
                """
                evidence_id,
                claim:claim_id (
                    id,
                    paper_id,
                    run_id,
                    kind,
                    content_text,
                    fol_json,
                    source_location,
                    confidence,
                    created_at
                )
            """
            )
            .in_("evidence_id", [str(eid) for eid in evidence_ids])
            .execute()
        )

        # Group claims by evidence
        result = {}
        for row in response.data:
            evidence_id = UUID(row["evidence_id"])
            claim_data = row["claim"]

            if evidence_id not in result:
                result[evidence_id] = []

            if claim_data:
                result[evidence_id].append(Extract(**claim_data))

        return result

    except Exception as e:
        handle_supabase_error(e)


def bulk_insert_evidence_claim_relationships(
    sb: Client, relationships: List[Dict[str, str]]
) -> int:
    """
    Insert evidence-claim relationships into the junction table.

    Args:
        sb: Supabase client
        relationships: List of dicts with 'evidence_id' and 'claim_id' (both UUIDs as strings)

    Returns:
        int: Number of relationships inserted

    Example:
        relationships = [
            {"evidence_id": "uuid1", "claim_id": "uuid2"},
            {"evidence_id": "uuid3", "claim_id": "uuid4"},
        ]
    """
    try:
        if not relationships:
            logger.warning("[DEBUG] No relationships to insert")
            return 0

        logger.info(
            f"[DEBUG] Inserting {len(relationships)} evidence-claim relationships"
        )

        response = sb.table("evidence_claims").insert(relationships).execute()

        inserted_count = len(response.data) if response.data else 0
        logger.info(
            f"[DEBUG] ✅ Inserted {inserted_count} relationships into evidence_claims table"
        )

        return inserted_count

    except Exception as e:
        logger.error(f"[DEBUG] ❌ Failed to insert relationships: {e}")
        handle_supabase_error(e)


def get_evidence_claims_map(sb: Client, extract_ids: List[str]) -> Dict[str, List[str]]:
    """
    Get evidence-claim relationships for a batch of extracts.

    Optimized for bulk queries - returns simple ID mappings without full extract data.
    Batches queries to avoid 414 Request-URI Too Large errors.

    Args:
        sb: Supabase client
        extract_ids: List of extract UUIDs (evidence IDs)

    Returns:
        Dict mapping evidence_id (str) to list of claim_ids (str)
    """
    try:
        logger.info(
            f"[DEBUG] 🔍 Querying evidence_claims table for {len(extract_ids)} extract IDs"
        )

        # Batch queries to avoid 414 errors (Cloudflare URL limit ~8KB)
        # Each UUID is ~36 chars, so batch size of 100 = ~3.6KB URL, safe margin
        BATCH_SIZE = 100
        result = {}

        for i in range(0, len(extract_ids), BATCH_SIZE):
            batch = extract_ids[i : i + BATCH_SIZE]
            logger.debug(
                f"[DEBUG] Querying batch {i//BATCH_SIZE + 1}/{(len(extract_ids) + BATCH_SIZE - 1)//BATCH_SIZE} ({len(batch)} IDs)"
            )

            response = (
                sb.table("evidence_claims")
                .select("evidence_id, claim_id")
                .in_("evidence_id", batch)
                .execute()
            )

            # Build evidence_id -> [claim_ids] map
            for row in response.data:
                evidence_id = row["evidence_id"]
                claim_id = row["claim_id"]

                if evidence_id not in result:
                    result[evidence_id] = []
                result[evidence_id].append(claim_id)

        logger.info(
            f"[DEBUG] 🔗 Built map with {len(result)} evidence IDs pointing to claims"
        )
        if result:
            # Show sample evidence and how many claims it points to
            sample_evidence_id = list(result.keys())[0]
            logger.debug(
                f"[DEBUG] Sample: evidence {sample_evidence_id} -> {len(result[sample_evidence_id])} claims"
            )

        return result

    except Exception as e:
        logger.error(f"[DEBUG] ❌ Error querying evidence_claims: {e}")
        handle_supabase_error(e)


# ---- Extraction Runs Operations (from extraction_runs_repo) ----


def upsert_extraction_run_by_job_id(
    sb: Client,
    paper_id: UUID,
    job_id: Optional[str],
    status: str,
    params: Optional[Dict[str, Any]] = None,
) -> Tuple[UUID, str]:
    """
    Create or update extraction run by job_id (idempotent operation)

    Args:
        sb: Supabase client (service role for background jobs)
        paper_id: Paper UUID
        job_id: Optional job ID for idempotency
        status: Run status ('queued', 'running', 'completed', 'failed')
        params: Optional parameters for the extraction

    Returns:
        Tuple[UUID, str]: (run_id, outcome) where outcome is "created" or "updated"

    Raises:
        DBError: On database operation failure
    """
    try:
        # If job_id is provided, try to find existing run
        if job_id:
            response = (
                sb.table("extraction_runs")
                .select("id, status")
                .eq("job_id", job_id)
                .single()
                .execute()
            )

            if response.data:
                # Update existing run
                run_id = UUID(response.data["id"])
                update_data = {"status": status}
                if params is not None:
                    update_data["params"] = params

                sb.table("extraction_runs").update(update_data).eq(
                    "id", str(run_id)
                ).execute()
                return run_id, "updated"

    except Exception as e:
        # If not found (single() throws when no results), continue to insert
        if "No rows" not in str(e):
            handle_supabase_error(e)

    # Insert new run
    try:
        insert_data = {"paper_id": str(paper_id), "status": status}

        if job_id:
            insert_data["job_id"] = job_id

        if params is not None:
            insert_data["params"] = params

        response = sb.table("extraction_runs").insert(insert_data).execute()

        if not response.data:
            raise Exception("Insert returned no data")

        return UUID(response.data[0]["id"]), "created"

    except Exception as e:
        # Handle race condition - another process may have inserted the same job_id
        if job_id and "duplicate key" in str(e).lower() and "job_id" in str(e).lower():
            # Try to fetch the run again
            response = (
                sb.table("extraction_runs")
                .select("id")
                .eq("job_id", job_id)
                .single()
                .execute()
            )
            if response.data:
                return UUID(response.data["id"]), "updated"

        handle_supabase_error(e)


def create_extraction_run(
    sb: Client, paper_id: UUID, status: str, params: Optional[Dict[str, Any]] = None
) -> UUID:
    """
    Create a new extraction run

    Args:
        sb: Supabase client (service role for background jobs)
        paper_id: Paper UUID
        status: Run status ('queued', 'running', 'completed', 'failed')
        params: Optional parameters for the extraction

    Returns:
        UUID: Created extraction run ID

    Raises:
        DBError: On database operation failure
    """
    try:
        # Start with basic required columns
        insert_data = {"paper_id": str(paper_id), "status": status}

        # Try to include params if the column exists
        if params is not None:
            try:
                insert_data["params"] = params
                response = sb.table("extraction_runs").insert(insert_data).execute()
            except Exception as e:
                # If params column doesn't exist, retry without it
                if "params" in str(e) and "PGRST204" in str(e):
                    print(f"  ℹ️  params column not found, creating run without params")
                    insert_data.pop("params", None)
                    response = sb.table("extraction_runs").insert(insert_data).execute()
                else:
                    raise
        else:
            response = sb.table("extraction_runs").insert(insert_data).execute()

        if not response.data:
            raise Exception("Insert returned no data")

        return UUID(response.data[0]["id"])

    except Exception as e:
        handle_supabase_error(e)


def mark_extraction_run_done(sb: Client, run_id: UUID) -> None:
    """
    Mark an extraction run as completed

    Args:
        sb: Supabase client (service role for background jobs)
        run_id: Extraction run UUID

    Raises:
        DBError: On database operation failure
    """
    try:
        update_data = {"status": "completed", "completed_at": "now()"}

        sb.table("extraction_runs").update(update_data).eq("id", str(run_id)).execute()

    except Exception as e:
        handle_supabase_error(e)


def mark_extraction_run_failed(sb: Client, run_id: UUID, error_message: str) -> None:
    """
    Mark an extraction run as failed

    Args:
        sb: Supabase client (service role for background jobs)
        run_id: Extraction run UUID
        error_message: Error description

    Raises:
        DBError: On database operation failure
    """
    try:
        update_data = {
            "status": "failed",
            "error_message": error_message,
            "completed_at": "now()",
        }

        sb.table("extraction_runs").update(update_data).eq("id", str(run_id)).execute()

    except Exception as e:
        handle_supabase_error(e)


def get_latest_extraction_run_by_paper_id(
    sb: Client, paper_id: UUID
) -> Optional[ExtractionRun]:
    """
    Get the latest extraction run for a paper (alias for endpoint compatibility)

    Args:
        sb: Supabase client
        paper_id: Paper UUID

    Returns:
        Optional[ExtractionRun]: Latest run if found, None otherwise

    Raises:
        DBError: On database operation failure
    """
    return get_latest_extraction_run_for_paper(sb, paper_id)


def get_latest_extraction_run_for_paper(
    sb: Client, paper_id: UUID
) -> Optional[ExtractionRun]:
    """
    Get the latest extraction run for a paper

    Args:
        sb: Supabase client
        paper_id: Paper UUID

    Returns:
        Optional[ExtractionRun]: Latest run if found, None otherwise

    Raises:
        DBError: On database operation failure
    """
    try:
        response = (
            sb.table("extraction_runs")
            .select("*")
            .eq("paper_id", str(paper_id))
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )

        if not response.data:
            return None

        return ExtractionRun(**response.data[0])

    except Exception as e:
        handle_supabase_error(e)


# ---- Missing Individual Extract Operations - TODO implement ----


def get_extract_by_id(sb: Client, extract_id: UUID) -> Extract:
    """
    Get extract by ID

    # TODO implement
    Args:
        sb: Supabase client
        extract_id: Extract UUID

    Returns:
        Extract: Extract data

    Raises:
        NotFound: If extract not found
        DBError: On database operation failure
    """
    pass


def update_extract(sb: Client, extract_id: UUID, updates: dict) -> Extract:
    """
    Update extract content, confidence, or metadata

    Args:
        sb: Supabase client
        extract_id: Extract UUID
        updates: Dict of fields to update

    Returns:
        Extract: Updated extract record

    Raises:
        NotFound: If extract not found
        DBError: On database operation failure
    """
    try:
        response = (
            sb.table("extracts").update(updates).eq("id", str(extract_id)).execute()
        )
        if not response.data:
            from app.db.errors import NotFound

            raise NotFound(f"Extract {extract_id} not found")
        return Extract(**response.data[0])
    except Exception as e:
        handle_supabase_error(e)


def bulk_update_extracts(sb: Client, updates_list: List[Dict[str, Any]]) -> int:
    """
    Bulk update multiple extracts with different updates for each

    Args:
        sb: Supabase client
        updates_list: List of dicts with 'id' and update fields
            Example: [{'id': uuid1, 'source_location': {...}}, ...]

    Returns:
        int: Number of extracts successfully updated

    Raises:
        DBError: On database operation failure
    """
    try:
        updated_count = 0
        for update_item in updates_list:
            extract_id = update_item.pop("id")
            if update_item:  # Only update if there are fields to update
                response = (
                    sb.table("extracts")
                    .update(update_item)
                    .eq("id", str(extract_id))
                    .execute()
                )
                if response.data:
                    updated_count += len(response.data)

        return updated_count

    except Exception as e:
        handle_supabase_error(e)


def delete_extract(sb: Client, extract_id: UUID) -> bool:
    """
    Delete extract and its relationships

    # TODO implement - Should cascade delete evidence_claims relationships
    Args:
        sb: Supabase client
        extract_id: Extract UUID

    Returns:
        bool: True if deleted successfully

    Raises:
        NotFound: If extract not found
        DBError: On database operation failure
    """
    pass


def bulk_delete_extracts(sb: Client, extract_ids: List[UUID]) -> int:
    """
    Bulk delete multiple extracts

    # TODO implement
    Args:
        sb: Supabase client
        extract_ids: List of extract UUIDs to delete

    Returns:
        int: Number of extracts successfully deleted

    Raises:
        DBError: On database operation failure
    """
    pass


def search_extracts(
    sb: Client, query: str, kind: Optional[str] = None, limit: int = 20
) -> List[Extract]:
    """
    Search extracts by content text (full-text search)

    # TODO implement - Could use Supabase full-text search on content_text
    Args:
        sb: Supabase client
        query: Search query string
        kind: Optional extract kind filter (claim/evidence)
        limit: Maximum results

    Returns:
        List[Extract]: Matching extracts

    Raises:
        DBError: On database operation failure
    """
    pass


def get_extracts_by_confidence_range(
    sb: Client, min_confidence: float, max_confidence: float = 1.0, limit: int = 50
) -> List[Extract]:
    """
    Get extracts within confidence score range

    # TODO implement
    Args:
        sb: Supabase client
        min_confidence: Minimum confidence score
        max_confidence: Maximum confidence score
        limit: Maximum results

    Returns:
        List[Extract]: Extracts within confidence range

    Raises:
        DBError: On database operation failure
    """
    pass


def get_extracts_by_date_range(
    sb: Client, start_date: str, end_date: str, limit: int = 50
) -> List[Extract]:
    """
    Get extracts created within date range

    # TODO implement
    Args:
        sb: Supabase client
        start_date: Start date (ISO format)
        end_date: End date (ISO format)
        limit: Maximum results

    Returns:
        List[Extract]: Extracts within date range

    Raises:
        DBError: On database operation failure
    """
    pass


def get_orphaned_extracts(sb: Client) -> List[Extract]:
    """
    Get extracts that have no evidence-claim relationships

    # TODO implement
    Args:
        sb: Supabase client

    Returns:
        List[Extract]: Extracts without relationships

    Raises:
        DBError: On database operation failure
    """
    pass


def get_extract_count_by_paper(sb: Client, paper_id: UUID) -> dict:
    """
    Get extract counts by kind for a paper

    # TODO implement
    Args:
        sb: Supabase client
        paper_id: Paper UUID

    Returns:
        dict: Counts by extract kind (claims: N, evidence: N, total: N)

    Raises:
        DBError: On database operation failure
    """
    pass


def get_extract_statistics(sb: Client) -> dict:
    """
    Get global extract statistics

    # TODO implement
    Args:
        sb: Supabase client

    Returns:
        dict: Statistics (total_extracts, claims_count, evidence_count, avg_confidence, etc.)

    Raises:
        DBError: On database operation failure
    """
    pass


# ---- Extraction Run Management - TODO implement ----


def get_extraction_run_by_id(sb: Client, run_id: UUID) -> ExtractionRun:
    """
    Get extraction run by ID

    # TODO implement
    Args:
        sb: Supabase client
        run_id: Extraction run UUID

    Returns:
        ExtractionRun: Run data

    Raises:
        NotFound: If run not found
        DBError: On database operation failure
    """
    pass


def list_extraction_runs_for_paper(
    sb: Client, paper_id: UUID, limit: int = 10
) -> List[ExtractionRun]:
    """
    List all extraction runs for a paper

    # TODO implement
    Args:
        sb: Supabase client
        paper_id: Paper UUID
        limit: Maximum results

    Returns:
        List[ExtractionRun]: Runs ordered by created_at desc

    Raises:
        DBError: On database operation failure
    """
    pass


def get_failed_extraction_runs(sb: Client, limit: int = 20) -> List[ExtractionRun]:
    """
    Get failed extraction runs for debugging

    # TODO implement
    Args:
        sb: Supabase client
        limit: Maximum results

    Returns:
        List[ExtractionRun]: Failed runs with error messages

    Raises:
        DBError: On database operation failure
    """
    pass


def delete_extraction_run(sb: Client, run_id: UUID) -> bool:
    """
    Delete extraction run and its extracts

    # TODO implement - Should cascade delete all related extracts
    Args:
        sb: Supabase client
        run_id: Extraction run UUID

    Returns:
        bool: True if deleted successfully

    Raises:
        NotFound: If run not found
        DBError: On database operation failure
    """
    pass


def get_extraction_run_statistics(sb: Client, run_id: UUID) -> dict:
    """
    Get statistics for a specific extraction run

    # TODO implement
    Args:
        sb: Supabase client
        run_id: Extraction run UUID

    Returns:
        dict: Statistics (extracts_count, claims_count, evidence_count, duration, etc.)

    Raises:
        DBError: On database operation failure
    """
    pass


# ---- Final Consolidation Results - TODO implement ----


def store_consolidation_result(sb: Client, run_id: UUID, result_data: dict) -> UUID:
    """
    Store final consolidation results for an extraction run

    # TODO implement - replaces final_consolidator.py filesystem writes
    Args:
        sb: Supabase client (service role for background jobs)
        run_id: Extraction run UUID
        result_data: Complete consolidation results JSON

    Returns:
        UUID: Consolidation result ID

    Raises:
        DBError: On database operation failure
    """
    pass


def get_consolidation_results(sb: Client, run_id: UUID) -> Optional[dict]:
    """
    Get stored consolidation results for an extraction run

    # TODO implement
    Args:
        sb: Supabase client
        run_id: Extraction run UUID

    Returns:
        Optional[dict]: Consolidation results if available, None otherwise

    Raises:
        DBError: On database operation failure
    """
    pass


def list_consolidation_results(
    sb: Client, paper_id: Optional[UUID] = None, limit: int = 50
) -> List[dict]:
    """
    List consolidation results, optionally filtered by paper

    # TODO implement
    Args:
        sb: Supabase client
        paper_id: Optional paper UUID filter
        limit: Maximum results

    Returns:
        List[dict]: Consolidation results with metadata

    Raises:
        DBError: On database operation failure
    """
    pass


def get_latest_consolidation_for_paper(sb: Client, paper_id: UUID) -> Optional[dict]:
    """
    Get the latest consolidation result for a paper

    # TODO implement
    Args:
        sb: Supabase client
        paper_id: Paper UUID

    Returns:
        Optional[dict]: Latest consolidation result if available

    Raises:
        DBError: On database operation failure
    """
    pass


def delete_consolidation_result(sb: Client, run_id: UUID) -> bool:
    """
    Delete consolidation results for an extraction run

    # TODO implement
    Args:
        sb: Supabase client
        run_id: Extraction run UUID

    Returns:
        bool: True if deleted successfully

    Raises:
        DBError: On database operation failure
    """
    pass
