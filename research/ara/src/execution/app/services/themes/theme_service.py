# Grounding: transcribed from oshima/api/app/services/themes/theme_service.py
#!/usr/bin/env python3
"""
Theme Service - Library theme extraction and management

Handles:
1. Extracting themes from library claims (uses dspy_theme_extractor.py)
2. Incremental theme updates (add/remove papers)
3. Theme versioning
"""

import json
import logging
from typing import Dict, List, Optional
from uuid import UUID

import dspy

from app.db.supabase_client import service_client
from app.services.extract.dspy_themes_extractor import LibraryThemeExtractor

logger = logging.getLogger(__name__)


class ThemeServiceError(Exception):
    """Base exception for theme service"""

    pass


async def extract_library_themes(library_id: UUID, job_params: Dict = None) -> Dict:
    """
    Extract themes from all claims in library.

    Flow:
    1. Get all claims from library papers
    2. Check if library has existing themes (unless force flag set)
    3. If yes: incremental update (theme_extender)
    4. If no: full extraction (theme_creator)
    5. Write themes to library_themes table

    Args:
        library_id: Library UUID
        job_params: Optional job parameters (includes force_full_extraction flag)

    Returns:
        Dict with extraction results
    """
    logger.info(f"🎨 Starting theme extraction for library {library_id}")

    job_params = job_params or {}
    force_full = job_params.get("force_full_extraction", False)

    sb = service_client()

    # Step 1: Get all claims from library papers
    claims = await get_library_claims(library_id)
    logger.info(f"Found {len(claims)} claims in library {library_id}")

    if not claims:
        logger.info("No claims found, skipping theme extraction")
        return {"status": "skipped", "reason": "no_claims"}

    # Step 2: Check for existing themes (unless force flag set)
    if force_full:
        logger.info(
            "🔥 FORCE FLAG SET - Skipping existing themes check, doing full extraction"
        )
        existing_themes = []
    else:
        existing_themes = await get_existing_themes(library_id)

    # Step 3: Create theme extractor (uses global DSPy config from startup)
    extractor = LibraryThemeExtractor()

    # Step 4: Extract or update themes
    if existing_themes:
        logger.info(
            f"Found {len(existing_themes)} existing themes, doing incremental update"
        )

        # Get claims already themed
        themed_claim_ids = get_themed_claim_ids(existing_themes)

        # Filter to unthemed claims
        unthemed_claims = [c for c in claims if c["extract_id"] not in themed_claim_ids]

        if not unthemed_claims:
            logger.info("All claims already themed, skipping")
            return {"status": "skipped", "reason": "all_claims_themed"}

        logger.info(f"Extending themes with {len(unthemed_claims)} new claims")

        # Call incremental updater with flat themes (no reconstruction needed)
        themes = extractor.add_claims_to_existing_themes(
            existing_themes, unthemed_claims
        )
        version = max(t.get("version", 1) for t in existing_themes) + 1
    else:
        if force_full:
            logger.info(
                "No existing themes check (forced full extraction), creating new theme hierarchy"
            )
            # Get the highest version number if themes exist, otherwise start at 1
            all_existing = await get_existing_themes(library_id)
            version = (
                max(t.get("version", 0) for t in all_existing) + 1
                if all_existing
                else 1
            )
        else:
            logger.info("No existing themes, creating new theme hierarchy")
            version = 1

        themes = extractor.extract_themes(claims)

    # Step 5: Write themes to database
    await write_themes_to_db(library_id, themes, version)

    logger.info(
        f"✅ Theme extraction complete: {len(themes)} themes, version {version}"
    )

    return {
        "status": "completed",
        "library_id": str(library_id),
        "themes_count": len(themes),
        "version": version,
    }


async def get_library_claims(library_id: UUID) -> List[Dict]:
    """Get claims from latest extraction runs for papers in library."""
    sb = service_client()

    # Get paper IDs in this library
    result = (
        sb.table("library_papers")
        .select("paper_id")
        .eq("library_id", str(library_id))
        .execute()
    )

    paper_ids = [UUID(row["paper_id"]) for row in result.data]

    if not paper_ids:
        return []

    # Get only claims from latest extraction runs (prevents duplicates after reprocessing)
    from app.db.queries.extracts import get_latest_extracts_for_papers

    claims_data = get_latest_extracts_for_papers(
        sb=sb, paper_ids=paper_ids, kind="claim"  # Only claims for theme extraction
    )

    # Format for theme extractor
    claims = []
    for extract in claims_data:
        claims.append(
            {
                "extract_id": extract["id"],
                "text": extract["content_text"],
                "paper_id": extract["paper_id"],
                "source_location": extract.get("source_location"),
                "confidence": extract.get("confidence", 1.0),
            }
        )

    return claims


async def get_existing_themes(library_id: UUID) -> List[Dict]:
    """Get existing themes for library (latest version) as flat list of rows."""
    sb = service_client()

    # Get latest version
    version_result = (
        sb.table("library_themes")
        .select("version")
        .eq("library_id", str(library_id))
        .order("version", desc=True)
        .limit(1)
        .execute()
    )

    if not version_result.data:
        return []

    latest_version = version_result.data[0]["version"]

    # Get all theme rows for latest version
    themes_result = (
        sb.table("library_themes")
        .select("*")
        .eq("library_id", str(library_id))
        .eq("version", latest_version)
        .execute()
    )

    # Return flat list with version attached
    themes = []
    for row in themes_result.data:
        theme_data = {
            "theme_id": row["theme_id"],
            "parent_theme_id": row["parent_theme_id"],
            "name": row["name"],
            "description": row["description"],
            "level": row["level"],
            "claim_ids": row["claim_ids"],
            "key_concepts": row["key_concepts"],
            "confidence": row["confidence"],
            "version": row["version"],
        }
        themes.append(theme_data)

    return themes


def reconstruct_theme_hierarchy(flat_themes: List[Dict]) -> List[Dict]:
    """
    Reconstruct nested theme hierarchy from flat DB rows.
    Needed for incremental theme updates.

    Args:
        flat_themes: Flat list of theme dicts from DB

    Returns:
        List of root themes with nested subthemes
    """
    # Build theme map
    theme_map = {t["theme_id"]: {**t, "subthemes": []} for t in flat_themes}

    # Build tree
    roots = []
    for theme in flat_themes:
        if theme["parent_theme_id"] is None:
            roots.append(theme_map[theme["theme_id"]])
        else:
            parent = theme_map.get(theme["parent_theme_id"])
            if parent:
                parent["subthemes"].append(theme_map[theme["theme_id"]])

    return roots


def get_themed_claim_ids(flat_themes: List[Dict]) -> set:
    """Extract all claim IDs from flat theme list."""
    claim_ids = set()
    for theme in flat_themes:
        claim_ids.update(theme.get("claim_ids", []))
    return claim_ids


async def write_themes_to_db(library_id: UUID, themes: List[Dict], version: int):
    """
    Write flat theme list to library_themes table.
    Accepts flat list with parent_theme_id already set.
    """
    sb = service_client()

    # Build parent -> children map to calculate levels
    children_map = {}
    for theme in themes:
        parent_id = theme.get("parent_theme_id")
        if parent_id:
            if parent_id not in children_map:
                children_map[parent_id] = []
            children_map[parent_id].append(theme["theme_id"])

    # Calculate level for each theme (BFS from roots)
    theme_levels = {}
    roots = [t for t in themes if not t.get("parent_theme_id")]

    # Initialize roots at level 1
    queue = [(t["theme_id"], 1) for t in roots]

    while queue:
        theme_id, level = queue.pop(0)
        theme_levels[theme_id] = level

        # Add children to queue
        for child_id in children_map.get(theme_id, []):
            queue.append((child_id, level + 1))

    # Create rows from flat list
    all_rows = []
    for theme in themes:
        row = {
            "library_id": str(library_id),
            "version": version,
            "theme_id": theme["theme_id"],
            "parent_theme_id": theme.get("parent_theme_id"),
            "level": theme_levels.get(theme["theme_id"], 1),
            "name": theme["name"],
            "description": theme["description"],
            "claim_ids": theme.get("claim_ids", []),
            "key_concepts": theme.get("key_concepts", []),
            "confidence": theme.get("confidence", 1.0),
            "extraction_model": "anthropic/claude-opus-4-1-20250805",
        }
        all_rows.append(row)

    # Batch insert
    if all_rows:
        sb.table("library_themes").insert(all_rows).execute()
        logger.info(f"Wrote {len(all_rows)} theme rows to database")
