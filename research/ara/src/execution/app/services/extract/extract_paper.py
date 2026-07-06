# Grounding: transcribed from oshima/api/app/services/extract/extract_paper.py
#!/usr/bin/env python3
"""
Paper Extraction Script

This script extracts claims and evidence from research papers using OpenAI API
and the v5 prompt system. It takes extraction type and paper metadata as input.

Usage:
    python extract_paper.py --type claims --field "machine learning" --topic "neural networks" --title "Paper Title" --content "Paper content..."

    or for both:
    python extract_paper.py --type both --field "psychiatry" --topic "bipolar disorder" --title "Paper Title" --content "Paper content..."
"""

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.models.extract import Claims, EvidenceList

# Import our prompt building system and schemas
from app.services.extract.build_prompt import (
    build_claim_prompts,
    build_evidence_prompts,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Constants for chunking (updated for GPT-5-mini: 272K tokens input window)
MAX_CHUNK_SIZE = (
    400000  # ~100K tokens (reduced for better claim coverage across paper sections)
)
OVERLAP_SIZE = 10000  # Larger overlap for better context preservation
MIN_CHUNK_SIZE = 100000  # Only chunk very large documents (>100K chars)


class PaperExtractor:
    """Extracts claims and evidence from research papers using OpenAI API."""

    def __init__(self, model: str = "gpt-5-mini-2025-08-07", rate_limiter=None):
        """
        Initialize the extractor.

        Args:
            model: OpenAI model to use for extraction
            rate_limiter: Rate limiter for LLM API calls (optional)
        """
        self.client = AsyncOpenAI()
        self.model = model
        self.rate_limiter = rate_limiter
        self.timing_data = {
            "total_extraction_time": 0.0,
            "api_calls": [],
            "total_api_time": 0.0,
        }
        logger.info(f"Initialized PaperExtractor with model: {model}")

        # NEW: Initialize DSPy (configuration done at app startup in main.py)
        self.use_dspy = os.getenv("USE_DSPY_EXTRACTION", "false").lower() == "true"
        if self.use_dspy:
            from app.services.extract.dspy_claims_extractor import DspyClaimsExtractor
            from app.services.extract.dspy_evidence_extractor import DspyEvidenceExtractor
            self.dspy_claims_extractor = DspyClaimsExtractor()
            self.dspy_evidence_extractor = DspyEvidenceExtractor()
            logger.info("DSPy extraction enabled (claims + evidence)")
        else:
            self.dspy_claims_extractor = None
            self.dspy_evidence_extractor = None

    async def _timed_api_call(
        self, call_type: str, chunk_info: str, messages: list, response_format
    ) -> tuple[Any, float]:
        """
        Make a timed API call and record timing data.

        Args:
            call_type: Type of extraction ("claims" or "evidence")
            chunk_info: Information about the chunk being processed
            messages: Messages to send to the API
            response_format: Pydantic model for response format

        Returns:
            Tuple of (response, duration_seconds)
        """
        start_time = time.time()

        # Apply rate limiting if available
        if self.rate_limiter:
            async with self.rate_limiter.limit_request_async():
                response = await self.client.beta.chat.completions.parse(
                    model=self.model,
                    messages=messages,
                    response_format=response_format,
                )
        else:
            response = await self.client.beta.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=response_format,
            )

        end_time = time.time()
        duration = end_time - start_time

        # Record timing data
        call_data = {
            "type": call_type,
            "chunk": chunk_info,
            "duration_seconds": round(duration, 3),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
        }
        self.timing_data["api_calls"].append(call_data)
        self.timing_data["total_api_time"] += duration

        logger.info(f"API call ({call_type}, {chunk_info}): {duration:.3f}s")

        return response, duration

    def _extract_title_and_abstract(self, content: str) -> tuple[str, str]:
        """
        Extract title and abstract from content for use in all chunks.

        Args:
            content: Full paper content

        Returns:
            Tuple of (title_section, abstract_section)
        """
        lines = content.split("\n")
        title_section = ""
        abstract_section = ""

        # Look for title in first few non-empty lines
        for i, line in enumerate(lines[:10]):
            line = line.strip()
            if line and len(line) > 10 and len(line) < 300:
                title_section = line
                break

        # Look for abstract section
        content_lower = content.lower()
        abstract_patterns = [
            r"abstract\s*[:\-]?\s*(.*?)(?=\n\s*(?:introduction|keywords|background|1\.|method))",
            r"summary\s*[:\-]?\s*(.*?)(?=\n\s*(?:introduction|keywords|background|1\.|method))",
        ]

        for pattern in abstract_patterns:
            match = re.search(pattern, content_lower, re.DOTALL | re.IGNORECASE)
            if match:
                abstract_section = match.group(0).strip()
                break

        # Fallback: use first 2000 characters as "abstract"
        if not abstract_section:
            abstract_section = content[:2000].strip()

        return title_section, abstract_section

    def _extract_section_headers(self, content: str) -> List[str]:
        """
        Extract main section headers from the document.

        Args:
            content: Full paper content

        Returns:
            List of section headers found in the document
        """
        header_patterns = [
            r"\n\s*(?:Abstract|Introduction|Background|Methods?|Methodology|Results?|Discussion|Conclusion|References|Acknowledgments)\s*[:\-]?",
            r"\n\s*\d+\.\s+[A-Z][A-Za-z\s]{5,50}",  # Numbered sections like "1. Introduction"
            r"\n\s*[A-Z][A-Z\s]{10,50}\s*\n",  # ALL CAPS headers
        ]

        headers = []
        for pattern in header_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                header = match.group(0).strip()
                if header and len(header) < 100:  # Reasonable header length
                    headers.append(header)

        # Remove duplicates while preserving order
        seen = set()
        unique_headers = []
        for header in headers:
            if header.lower() not in seen:
                seen.add(header.lower())
                unique_headers.append(header)

        return unique_headers[:20]  # Limit to first 20 headers

    def _create_chunks(self, content: str, title: str) -> List[Dict[str, Any]]:
        """
        Split content into intelligent chunks if needed.

        Args:
            content: Full paper content
            title: Paper title

        Returns:
            List of chunk dictionaries with metadata
        """
        if len(content) <= MIN_CHUNK_SIZE:
            logger.info("Content is short enough, using single chunk")
            return [
                {
                    "content": content,
                    "chunk_id": 1,
                    "total_chunks": 1,
                    "section": "full_document",
                    "char_start": 0,
                    "char_end": len(content),
                }
            ]

        logger.info(f"Content length {len(content)} exceeds minimum, creating chunks")

        # Extract title, abstract, and section headers for context
        title_section, abstract_section = self._extract_title_and_abstract(content)
        all_headers = self._extract_section_headers(content)

        # Find logical break points (section headers, paragraphs)
        break_patterns = [
            r"\n\s*(?:Abstract|Introduction|Methods?|Results?|Discussion|Conclusion|References|Acknowledgments|Figure|Table)\s*[:\-]?",
            r"\n\s*\d+\.\s+[A-Z]",  # Numbered sections
            r"\n\s*[A-Z][A-Z\s]{10,}\s*\n",  # ALL CAPS headers
            r"\n\n\s*\n",  # Paragraph breaks
        ]

        # Find all potential break points
        break_points = [0]
        for pattern in break_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                break_points.append(match.start())

        break_points.append(len(content))
        break_points = sorted(set(break_points))

        # Create chunks with intelligent splitting
        chunks = []
        chunk_start = 0
        chunk_id = 1

        while chunk_start < len(content):
            # Find optimal end point
            target_end = chunk_start + MAX_CHUNK_SIZE

            if target_end >= len(content):
                # Last chunk
                chunk_end = len(content)
            else:
                # Find best break point before target_end
                best_break = target_end
                for bp in break_points:
                    if chunk_start < bp <= target_end:
                        best_break = bp

                chunk_end = best_break

            # Extract chunk content
            chunk_content = content[chunk_start:chunk_end]

            # Determine section type
            section_type = "middle"
            if chunk_start == 0:
                section_type = "beginning"
            elif chunk_end == len(content):
                section_type = "end"

            # Determine which headers are in this chunk
            chunk_headers = []
            for header in all_headers:
                if header.lower() in chunk_content.lower():
                    chunk_headers.append(header)

            # Calculate approximate page range (assuming ~3000 chars per page)
            start_page = max(1, chunk_start // 3000 + 1)
            end_page = min(len(content) // 3000 + 1, chunk_end // 3000 + 1)
            total_pages = len(content) // 3000 + 1

            # Create enhanced chunk with comprehensive context
            context_parts = [
                f"=== DOCUMENT CONTEXT ===",
                f"Title: {title}",
                f"Abstract: {abstract_section}",
                f"",
                f"=== DOCUMENT STRUCTURE ===",
                f"All document sections: {', '.join(all_headers) if all_headers else 'No clear section headers detected'}",
                f"",
                f"=== CURRENT CHUNK INFO ===",
                f"Chunk {chunk_id} (estimated pages {start_page}-{end_page} of ~{total_pages})",
                f"Sections in this chunk: {', '.join(chunk_headers) if chunk_headers else 'No major section headers'}",
                f"",
                f"=== CHUNK CONTENT ===",
                chunk_content,
            ]

            full_chunk_content = "\n".join(context_parts)

            chunks.append(
                {
                    "content": full_chunk_content,
                    "chunk_id": chunk_id,
                    "total_chunks": None,  # Will be set after all chunks are created
                    "section": section_type,
                    "char_start": chunk_start,
                    "char_end": chunk_end,
                    "original_content": chunk_content,
                }
            )

            # Move to next chunk with overlap
            if chunk_end < len(content):
                chunk_start = max(chunk_start + 1, chunk_end - OVERLAP_SIZE)
            else:
                break

            chunk_id += 1

        # Update total_chunks count
        for chunk in chunks:
            chunk["total_chunks"] = len(chunks)

        logger.info(f"Created {len(chunks)} chunks")
        return chunks

    def _merge_extraction_results(
        self, chunk_results: List[Dict], extraction_type: str
    ) -> Dict:
        """
        Merge results from multiple chunks into a single result.

        Args:
            chunk_results: List of extraction results from each chunk
            extraction_type: Type of extraction performed

        Returns:
            Merged extraction result
        """
        if not chunk_results:
            return {}

        if len(chunk_results) == 1:
            return chunk_results[0]

        logger.info(f"Merging {len(chunk_results)} chunk results")

        merged_claims = []
        merged_evidence_groups = {}  # claim_id -> list[Evidence]
        merged_acronyms = {}
        claim_id_counter = 1
        evidence_id_counter = 1

        # Process each chunk result
        for chunk_idx, result in enumerate(chunk_results):
            if extraction_type in ["claims", "both"]:
                claims_data = (
                    result.get("claims", {}) if extraction_type == "both" else result
                )
                for claim in claims_data.get("claims", []):
                    # Update claim ID to be globally unique
                    claim["claim_id"] = f"C{claim_id_counter}"
                    claim["source_chunk"] = chunk_idx + 1
                    merged_claims.append(claim)
                    claim_id_counter += 1

                # Merge acronyms
                chunk_acronyms = claims_data.get("acronyms", {})
                merged_acronyms.update(chunk_acronyms)

            if extraction_type in ["evidence", "both"]:
                evidence_data = (
                    result.get("evidence", {}) if extraction_type == "both" else result
                )
                # Evidence is now in evidence_groups format
                for group in evidence_data.get("evidence_groups", []):
                    claim_id = group.get("claim_id")
                    evidence_list = group.get("evidence_list", [])

                    if claim_id not in merged_evidence_groups:
                        merged_evidence_groups[claim_id] = []

                    for evidence in evidence_list:
                        # Update evidence ID to be globally unique
                        evidence["evidence_id"] = f"E{evidence_id_counter}"
                        evidence["source_chunk"] = chunk_idx + 1
                        merged_evidence_groups[claim_id].append(evidence)
                        evidence_id_counter += 1

                # Merge acronyms
                chunk_acronyms = evidence_data.get("acronyms", {})
                merged_acronyms.update(chunk_acronyms)

        # Build final result with new evidence_groups format
        if extraction_type == "claims":
            return {"claims": merged_claims, "acronyms": merged_acronyms}
        elif extraction_type == "evidence":
            # Convert back to evidence_groups format
            evidence_groups = []
            for claim_id, evidence_list in merged_evidence_groups.items():
                evidence_groups.append(
                    {"claim_id": claim_id, "evidence_list": evidence_list}
                )
            return {"evidence_groups": evidence_groups, "acronyms": merged_acronyms}
        else:  # both
            # Convert back to evidence_groups format
            evidence_groups = []
            for claim_id, evidence_list in merged_evidence_groups.items():
                evidence_groups.append(
                    {"claim_id": claim_id, "evidence_list": evidence_list}
                )
            return {
                "claims": {"claims": merged_claims, "acronyms": merged_acronyms},
                "evidence": {
                    "evidence_groups": evidence_groups,
                    "acronyms": merged_acronyms,
                },
            }

    def _adapt_dspy_claims_to_openai_format(self, dspy_result: dict) -> dict:
        """
        Convert DSPy claims format to OpenAI format for compatibility.

        DSPy returns: {verbatim_statement, rephrased_statement, original, confidence, centrality_percentage}
        OpenAI expects: {claim, explanation, claim_id}

        This allows rest of pipeline to work unchanged.
        """
        openai_claims = []

        for idx, claim in enumerate(dspy_result.get("claims", [])):
            openai_claims.append({
                "claim": claim.get("rephrased_statement", ""),  # Use rephrased as main text
                "explanation": f"Confidence: {claim.get('confidence', 0):.2f}, "
                              f"Centrality: {claim.get('centrality_percentage', 0):.1f}%",
                "claim_id": f"C{idx + 1}",  # Will be reassigned by merge logic anyway
                "_dspy_raw": claim  # Preserve original DSPy data for later use
            })

        return {
            "claims": openai_claims,
            "acronyms": {}  # DSPy doesn't extract acronyms yet
        }

    def _adapt_dspy_evidence_to_openai_format(self, dspy_result: dict) -> dict:
        """
        Convert DSPy evidence format to OpenAI format for compatibility.

        DSPy returns: {evidence_groups: [{claim_id, evidence_list: [{verbatim_statement, rephrased_statement, original, direction, explanation}]}]}
        OpenAI expects: {evidence_groups: [{claim_id, evidence_list: [{evidence, explanation, evidence_id, direction}]}]}

        This allows rest of pipeline to work unchanged.
        """
        openai_evidence_groups = []

        for group_idx, group in enumerate(dspy_result.get("evidence_groups", [])):
            evidence_list = []
            for ev_idx, evidence in enumerate(group.get("evidence_list", [])):
                evidence_list.append({
                    "evidence": evidence.get("rephrased_statement", ""),  # Use rephrased as main text
                    "evidence_id": f"E{group_idx + 1}_{ev_idx + 1}",  # Will be reassigned by merge logic
                    "direction": evidence.get("direction", "contextual"),
                    "_dspy_raw": evidence  # Preserve original DSPy data for later use
                })

            openai_evidence_groups.append({
                "claim_id": group.get("claim_id", ""),
                "evidence_list": evidence_list
            })

        return {
            "evidence_groups": openai_evidence_groups,
            "acronyms": {}  # DSPy doesn't extract acronyms yet
        }

    async def extract_claims(
        self,
        *,
        field: str,
        topic: str,
        title: str,
        content: str,
        input_json: Optional[str] = None,
        input_label: Optional[str] = None,
        input_tag: Optional[str] = None,
    ) -> dict:
        """
        Extract claims from a research paper with intelligent chunking.

        Args:
            field: Research field (e.g., "machine learning")
            topic: Specific topic (e.g., "neural networks")
            title: Paper title
            content: Paper content
            input_json: Optional previous extraction results
            input_label: Label for input block
            input_tag: XML tag for input block

        Returns:
            Dictionary containing extracted claims and acronyms
        """
        logger.info("Extracting claims...")

        # Create chunks if content is too long
        chunks = self._create_chunks(content, title)

        if len(chunks) == 1:
            if self.use_dspy:
                # NEW: Use DSPy extraction
                start_time = time.time()
                result = self.dspy_claims_extractor.extract_claims_with_context(
                    document=content,
                    title=title,
                    field=field,
                    topic=topic
                )
                duration = time.time() - start_time

                # Convert DSPy format -> OpenAI format for compatibility
                result = self._adapt_dspy_claims_to_openai_format(result)

                # Record timing
                self.timing_data["api_calls"].append({
                    "type": "claims",
                    "chunk": "single chunk",
                    "duration_seconds": round(duration, 3),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                })
                self.timing_data["total_api_time"] += duration

                logger.info(f"DSPy extraction took {duration:.3f}s")
                logger.info(f"Extracted {len(result.get('claims', []))} claims")
                return result
            else:
                # EXISTING: OpenAI extraction (unchanged)
                sys_prompt, user_prompt = build_claim_prompts(
                    field=field,
                    topic=topic,
                    title=title,
                    content=content,
                    input_json=input_json,
                    input_label=input_label,
                    input_tag=input_tag,
                )

                response, duration = await self._timed_api_call(
                    call_type="claims",
                    chunk_info="single chunk",
                    messages=[
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    response_format=Claims,
                )

                result = response.choices[0].message.parsed.model_dump()
                logger.info(f"Extracted {len(result.get('claims', []))} claims")
                return result

        # Multiple chunks - process in parallel
        logger.info(f"Processing {len(chunks)} chunks in parallel")

        async def process_chunk(chunk):
            if self.use_dspy:
                # NEW: Use DSPy extraction
                loop = asyncio.get_event_loop()
                chunk_result = await loop.run_in_executor(
                    None,
                    self.dspy_claims_extractor.extract_claims_with_context,
                    chunk["content"],  # document
                    title,             # title
                    field,             # field
                    topic              # topic
                )

                # Convert DSPy format -> OpenAI format
                chunk_result = self._adapt_dspy_claims_to_openai_format(chunk_result)

                logger.info(
                    f"Chunk {chunk['chunk_id']}/{chunk['total_chunks']}: {len(chunk_result.get('claims', []))} claims"
                )
                return chunk_result
            else:
                # EXISTING: OpenAI extraction (unchanged)
                chunk_sys_prompt, chunk_user_prompt = build_claim_prompts(
                    field=field,
                    topic=topic,
                    title=title,
                    content=chunk["content"],
                    input_json=input_json,
                    input_label=input_label,
                    input_tag=input_tag,
                )

                response, duration = await self._timed_api_call(
                    call_type="claims",
                    chunk_info=f"chunk {chunk['chunk_id']}/{chunk['total_chunks']}",
                    messages=[
                    {"role": "system", "content": chunk_sys_prompt},
                    {"role": "user", "content": chunk_user_prompt},
                ],
                response_format=Claims,
            )

            chunk_result = response.choices[0].message.parsed.model_dump()
            logger.info(
                f"Chunk {chunk['chunk_id']}/{chunk['total_chunks']}: {len(chunk_result.get('claims', []))} claims"
            )
            return chunk_result

        # Process all chunks in parallel
        chunk_results = await asyncio.gather(
            *[process_chunk(chunk) for chunk in chunks]
        )

        # Merge results
        merged_result = self._merge_extraction_results(chunk_results, "claims")
        logger.info(
            f"Total extracted: {len(merged_result.get('claims', []))} claims from {len(chunks)} chunks"
        )

        return merged_result

    async def extract_evidence(
        self,
        *,
        field: str,
        topic: str,
        title: str,
        content: str,
        claims_json: Optional[str] = None,
    ) -> dict:
        """
        Extract evidence from a research paper with intelligent chunking.

        Args:
            field: Research field (e.g., "machine learning")
            topic: Specific topic (e.g., "neural networks")
            title: Paper title
            content: Paper content
            claims_json: JSON string of previously extracted claims

        Returns:
            Dictionary containing extracted evidence and acronyms
        """
        logger.info("Extracting evidence with DSPY...")

        # Create chunks if content is too long
        chunks = self._create_chunks(content, title)

        if len(chunks) == 1:
            if self.use_dspy:
                # NEW: Use DSPy extraction
                start_time = time.time()
                result = self.dspy_evidence_extractor.extract_evidence_with_context(
                    document=content,
                    claims_json=claims_json or "[]",
                    title=title,
                    field=field,
                    topic=topic
                )
                duration = time.time() - start_time

                # Convert DSPy format -> OpenAI format for compatibility
                result = self._adapt_dspy_evidence_to_openai_format(result)

                # Record timing
                self.timing_data["api_calls"].append({
                    "type": "evidence",
                    "chunk": "single chunk",
                    "duration_seconds": round(duration, 3),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                })
                self.timing_data["total_api_time"] += duration

                total_evidence = sum(
                    len(group.get("evidence_list", []))
                    for group in result.get("evidence_groups", [])
                )
                logger.info(f"DSPy extraction took {duration:.3f}s")
                logger.info(f"Extracted {total_evidence} evidence statements")
                return result
            else:
                # EXISTING: OpenAI extraction (unchanged)
                sys_prompt, user_prompt = build_evidence_prompts(
                    field=field,
                    topic=topic,
                    title=title,
                    content=content,
                    input_json=claims_json,
                    input_label="Claims" if claims_json else None,
                    input_tag="claims" if claims_json else None,
                )

                response, duration = await self._timed_api_call(
                    call_type="evidence",
                    chunk_info="single chunk",
                    messages=[
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    response_format=EvidenceList,
                )

                result = response.choices[0].message.parsed.model_dump()
                # Count evidence across all claim groups
                total_evidence = sum(
                    len(group.get("evidence_list", []))
                    for group in result.get("evidence_groups", [])
                )
                logger.info(f"Extracted {total_evidence} evidence statements")
                return result

        # Multiple chunks - process in parallel
        logger.info(f"Processing {len(chunks)} chunks in parallel")

        async def process_chunk(chunk):
            if self.use_dspy:
                # NEW: Use DSPy extraction
                loop = asyncio.get_event_loop()
                chunk_result = await loop.run_in_executor(
                    None,
                    self.dspy_evidence_extractor.extract_evidence_with_context,
                    chunk["content"],      # document
                    claims_json or "[]",   # claims_json
                    title,                 # title
                    field,                 # field
                    topic                  # topic
                )

                # Convert DSPy format -> OpenAI format
                chunk_result = self._adapt_dspy_evidence_to_openai_format(chunk_result)

                chunk_evidence_count = sum(
                    len(group.get("evidence_list", []))
                    for group in chunk_result.get("evidence_groups", [])
                )
                logger.info(
                    f"Chunk {chunk['chunk_id']}/{chunk['total_chunks']}: {chunk_evidence_count} evidence"
                )
                return chunk_result
            else:
                # EXISTING: OpenAI extraction (unchanged)
                chunk_sys_prompt, chunk_user_prompt = build_evidence_prompts(
                    field=field,
                    topic=topic,
                    title=title,
                    content=chunk["content"],
                    input_json=claims_json,
                    input_label="Claims" if claims_json else None,
                    input_tag="claims" if claims_json else None,
                )

                response, duration = await self._timed_api_call(
                    call_type="evidence",
                    chunk_info=f"chunk {chunk['chunk_id']}/{chunk['total_chunks']}",
                    messages=[
                        {"role": "system", "content": chunk_sys_prompt},
                        {"role": "user", "content": chunk_user_prompt},
                    ],
                    response_format=EvidenceList,
                )

                chunk_result = response.choices[0].message.parsed.model_dump()
                # Count evidence across all claim groups in this chunk
                chunk_evidence_count = sum(
                    len(group.get("evidence_list", []))
                    for group in chunk_result.get("evidence_groups", [])
                )
                logger.info(
                    f"Chunk {chunk['chunk_id']}/{chunk['total_chunks']}: {chunk_evidence_count} evidence"
                )
                return chunk_result

        # Process all chunks in parallel
        chunk_results = await asyncio.gather(
            *[process_chunk(chunk) for chunk in chunks]
        )

        # Merge results
        merged_result = self._merge_extraction_results(chunk_results, "evidence")
        # Count evidence across all claim groups
        total_evidence = sum(
            len(group.get("evidence_list", []))
            for group in merged_result.get("evidence_groups", [])
        )
        logger.info(
            f"Total extracted: {total_evidence} evidence from {len(chunks)} chunks"
        )

        return merged_result

    async def _write_extracts_to_database(
        self,
        claims_result: dict,
        evidence_result: dict,
        paper_id: str,
        extraction_run_id: str
    ) -> dict:
        """
        Write claims and evidence to database using existing bulk insert.

        Args:
            claims_result: Claims extraction output
            evidence_result: Evidence extraction output
            paper_id: Paper UUID
            extraction_run_id: Extraction run UUID

        Returns:
            dict: Mapping of LLM IDs to database UUIDs
        """
        from uuid import UUID
        from app.db.queries import extracts as extracts_queries
        from app.db.supabase_client import service_client
        from app.models.db_models import ExtractIn

        sb = service_client()

        # Prepare claim ExtractIn objects
        claims_extracts = []
        for claim in claims_result.get("claims", []):
            # Get DSPy raw data if available
            dspy_raw = claim.get("_dspy_raw")

            extract_in = ExtractIn(
                kind="claim",
                content_text=claim.get("claim", ""),  # Rephrased statement
                confidence=dspy_raw.get("confidence") if isinstance(dspy_raw, dict) else None,
                extract_data={
                    # Store complete raw extraction output
                    "dspy_raw": dspy_raw,
                    "source_chunk": claim.get("source_chunk"),
                    "original_claim_id": claim.get("claim_id")
                } if dspy_raw is not None else None,
                fol_json=None  # Will be populated by NLP2FOL stage
            )
            claims_extracts.append(extract_in)

        # Build claim ID mapping
        claim_id_mapping = {
            c["claim_id"]: c["claim_id"]
            for c in claims_result.get("claims", [])
        }
        logger.info(f"[DEBUG] Built claim_id_mapping with {len(claim_id_mapping)} entries: {list(claim_id_mapping.keys())[:5]}")

        # Use existing bulk insert function!
        result = extracts_queries.bulk_insert_with_relationships(
            sb=sb,
            paper_id=UUID(paper_id),
            run_id=UUID(extraction_run_id),
            claims=claims_extracts,
            evidence_groups=evidence_result.get("evidence_groups", []),
            claim_id_mapping=claim_id_mapping,
            attribution_map=None  # Will be added in attribution stage
        )

        logger.info(f"Bulk insert complete: {result.inserted_count} extracts")
        logger.info(f"[DEBUG] Returned claim_uuid_mapping has {len(result.claim_uuid_mapping or {})} entries")
        logger.info(f"[DEBUG] Returned evidence_uuid_mapping has {len(result.evidence_uuid_mapping or {})} entries")
        if result.claim_uuid_mapping:
            logger.info(f"[DEBUG] Sample claim mapping: {dict(list(result.claim_uuid_mapping.items())[:3])}")
        if result.evidence_uuid_mapping:
            logger.info(f"[DEBUG] Sample evidence mapping: {dict(list(result.evidence_uuid_mapping.items())[:3])}")

        return {
            "result": result,
            "inserted_count": result.inserted_count,
            # NEW: Return UUID mappings for downstream stages
            "claim_uuid_mapping": result.claim_uuid_mapping or {},
            "evidence_uuid_mapping": result.evidence_uuid_mapping or {}
        }

    async def extract_both(
        self,
        *,
        field: str,
        topic: str,
        title: str,
        content: str,
        paper_id: Optional[str] = None,
        extraction_run_id: Optional[str] = None,  # NEW: Required parameter for DB writes
    ) -> dict:
        """
        Extract both claims and evidence from a research paper with intelligent chunking.

        Args:
            field: Research field (e.g., "machine learning")
            topic: Specific topic (e.g., "neural networks")
            title: Paper title
            content: Paper content
            paper_id: Optional paper identifier
            extraction_run_id: Extraction run ID for database writes (optional)

        Returns:
            Dictionary containing both claims and evidence extractions
        """
        logger.info("Extracting both claims and evidence...")

        # Start total timing
        total_start_time = time.time()

        # Reset timing data for this extraction
        self.timing_data = {
            "total_extraction_time": 0.0,
            "api_calls": [],
            "total_api_time": 0.0,
        }

        # Create chunks once for both extractions
        chunks = self._create_chunks(content, title)
        logger.info(f"Using {len(chunks)} chunks for both extractions")

        # Extract claims from all chunks
        claims_result = await self.extract_claims(
            field=field,
            topic=topic,
            title=title,
            content=content,
        )

        # NEW: Write claims to database immediately after extraction
        claims_extract_ids = {}
        if extraction_run_id and paper_id:
            logger.info(f"[DEBUG] Writing {len(claims_result.get('claims', []))} claims to DB")
            claims_extract_ids = await self._write_extracts_to_database(
                claims_result=claims_result,
                evidence_result={"evidence_groups": []},  # No evidence yet
                paper_id=paper_id,
                extraction_run_id=extraction_run_id
            )
            logger.info(f"✅ Written {claims_extract_ids.get('inserted_count', 0)} claims to database")
            logger.info(f"[DEBUG] Claims write returned {len(claims_extract_ids.get('claim_uuid_mapping', {}))} claim UUID mappings")

        # Extract evidence from all chunks, providing claims as context
        claims_json = json.dumps(claims_result)
        evidence_result = await self.extract_evidence(
            field=field,
            topic=topic,
            title=title,
            content=content,
            claims_json=claims_json,
        )

        # NEW: Write evidence to database immediately after extraction
        evidence_extract_ids = {}
        if extraction_run_id and paper_id:
            from uuid import UUID
            from app.db.queries import extracts as extracts_queries
            from app.db.supabase_client import service_client

            total_evidence = sum(len(g.get("evidence_list", [])) for g in evidence_result.get("evidence_groups", []))
            logger.info(f"[DEBUG] Writing {total_evidence} evidence items to DB (across {len(evidence_result.get('evidence_groups', []))} groups)")

            # Get the claim UUID mapping from the first write
            claim_uuid_mapping = claims_extract_ids.get('claim_uuid_mapping', {})
            logger.info(f"[DEBUG] Using claim_uuid_mapping with {len(claim_uuid_mapping)} entries from first write")

            sb = service_client()

            # Call bulk_insert_with_relationships directly with the claim UUID mapping
            result = extracts_queries.bulk_insert_with_relationships(
                sb=sb,
                paper_id=UUID(paper_id),
                run_id=UUID(extraction_run_id),
                claims=[],  # No new claims to insert
                evidence_groups=evidence_result.get("evidence_groups", []),
                claim_id_mapping=claim_uuid_mapping,  # Pass the UUID mapping from first write!
                attribution_map=None
            )

            evidence_extract_ids = {
                "result": result,
                "inserted_count": result.inserted_count,
                "claim_uuid_mapping": result.claim_uuid_mapping or {},
                "evidence_uuid_mapping": result.evidence_uuid_mapping or {}
            }

            logger.info(f"✅ Written {evidence_extract_ids.get('inserted_count', 0)} evidence to database")
            logger.info(f"[DEBUG] Evidence write returned {len(evidence_extract_ids.get('evidence_uuid_mapping', {}))} evidence UUID mappings")
            logger.info(f"[DEBUG] Relationships were created automatically by bulk_insert_with_relationships")

        # Combine extract IDs
        extract_ids = {
            "inserted_count": claims_extract_ids.get('inserted_count', 0) + evidence_extract_ids.get('inserted_count', 0),
            "claim_uuid_mapping": claims_extract_ids.get('claim_uuid_mapping', {}),
            "evidence_uuid_mapping": evidence_extract_ids.get('evidence_uuid_mapping', {})
        }

        # Calculate total time
        total_end_time = time.time()
        total_duration = total_end_time - total_start_time
        self.timing_data["total_extraction_time"] = round(total_duration, 3)

        # Combine results with chunking and timing metadata
        result = {
            "id": paper_id or "unknown",
            "title": title,
            "claims": claims_result,
            "evidence": evidence_result,
            "extract_ids": extract_ids,  # NEW: Track DB UUIDs
            "processing_info": {
                "chunks_used": len(chunks),
                "content_length": len(content),
                "chunking_enabled": len(chunks) > 1,
            },
            "timing_info": self.timing_data,
        }

        logger.info(
            f"Extraction complete - Total time: {total_duration:.3f}s, API time: {self.timing_data['total_api_time']:.3f}s"
        )
        return result


async def main():
    """Command line interface for paper extraction."""
    parser = argparse.ArgumentParser(
        description="Extract claims and evidence from research papers"
    )

    parser.add_argument(
        "--type",
        choices=["claims", "evidence", "claims_evidence"],
        required=True,
        help="Type of extraction to perform ('claims_evidence' extracts both)",
    )
    parser.add_argument(
        "--field", required=True, help="Research field (e.g., 'machine learning')"
    )
    parser.add_argument(
        "--topic", required=True, help="Specific topic (e.g., 'neural networks')"
    )
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--content", help="Paper content (or use --content-file)")
    parser.add_argument("--content-file", help="Path to file containing paper content")
    parser.add_argument("--paper-id", help="Optional paper identifier")
    parser.add_argument("--output", help="Output file path (defaults to stdout)")
    parser.add_argument(
        "--model", default="o3-mini-2025-01-31", help="OpenAI model to use"
    )
    parser.add_argument(
        "--claims-input", help="Path to claims JSON file (for evidence extraction)"
    )

    args = parser.parse_args()

    # Get content and derive paper_id if not provided
    if args.content_file:
        content_file_path = Path(args.content_file)
        with open(content_file_path, "r") as f:
            content = f.read()
        # Use filename as paper_id if not explicitly provided
        if not args.paper_id and args.type == "claims_evidence":
            args.paper_id = content_file_path.stem
    elif args.content:
        content = args.content
    else:
        parser.error("Either --content or --content-file must be provided")

    # Initialize extractor
    extractor = PaperExtractor(model=args.model)

    try:
        # Perform extraction based on type
        if args.type == "claims":
            result = await extractor.extract_claims(
                field=args.field,
                topic=args.topic,
                title=args.title,
                content=content,
            )
        elif args.type == "evidence":
            claims_json = None
            if args.claims_input:
                with open(args.claims_input, "r") as f:
                    claims_json = f.read()

            result = await extractor.extract_evidence(
                field=args.field,
                topic=args.topic,
                title=args.title,
                content=content,
                claims_json=claims_json,
            )
        elif args.type == "claims_evidence":
            result = await extractor.extract_both(
                field=args.field,
                topic=args.topic,
                title=args.title,
                content=content,
                paper_id=args.paper_id,
            )

        # Output result
        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
            logger.info(f"Results saved to {args.output}")
        else:
            print(json.dumps(result, indent=2))

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
