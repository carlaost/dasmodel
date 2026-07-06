# Grounding: transcribed from oshima/api/app/models/db_models.py
#!/usr/bin/env python3
"""
Pydantic models for database operations (input/output types)
"""

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


# Paper models
class PaperIn(BaseModel):
    """Input model for creating/updating papers"""

    title: str
    storage_path: str
    fingerprint: str  # Used for deduplication (e.g., SHA256 of content)
    sha256: Optional[str] = None
    size_bytes: Optional[int] = None
    original_filename: Optional[str] = None
    doi: Optional[str] = None
    num_pages: Optional[int] = None


class Paper(BaseModel):
    """Output model for papers"""

    id: UUID
    title: str
    storage_path: str
    fingerprint: str
    sha256: Optional[str] = None
    size_bytes: Optional[int] = None
    original_filename: Optional[str] = None
    doi: Optional[str] = None
    num_pages: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


# Library models
class Library(BaseModel):
    """Output model for libraries"""

    id: UUID
    owner_user_id: Optional[UUID] = None  # NULL for system/admin libraries
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None


# Source location models
class BoundingBox(BaseModel):
    """Bounding box coordinates"""

    x: float
    y: float
    w: float  # width
    h: float  # height


class TextSpan(BaseModel):
    """Text span markers"""

    start: int
    end: int


class SourceLocation(BaseModel):
    """Source location within a document"""

    page: int
    bbox: Optional[BoundingBox] = None
    span: Optional[TextSpan] = None


# Extract models
class ExtractIn(BaseModel):
    """Input model for creating extracts"""

    kind: str  # 'claim', 'evidence', etc.
    content_text: str
    extract_data: Optional[Dict[str, Any]] = None  # Raw extraction output (DSPy, OpenAI, etc.)
    fol_json: Optional[Dict[str, Any]] = None  # First-Order Logic data (from NLP2FOL stage)
    source_location: Optional[SourceLocation] = None
    confidence: Optional[float] = None


class Extract(BaseModel):
    """Output model for extracts"""

    id: UUID
    paper_id: UUID
    run_id: UUID
    kind: str
    content_text: str
    extract_data: Optional[Dict[str, Any]] = None  # Raw extraction output (DSPy, OpenAI, etc.)
    fol_json: Optional[Dict[str, Any]] = None  # First-Order Logic data (from NLP2FOL stage)
    source_location: Optional[SourceLocation] = None
    confidence: Optional[float] = None
    created_at: datetime


# Extraction run models
class ExtractionRun(BaseModel):
    """Output model for extraction runs"""

    id: UUID
    paper_id: UUID
    status: str  # 'queued', 'running', 'completed', 'failed'
    params: Optional[Dict[str, Any]] = None
    params_json: Optional[str] = None  # Legacy field
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None  # Changed from completed_at
    created_at: Optional[datetime] = None  # Made optional since it might not exist
    updated_at: Optional[datetime] = None  # Made optional since it might not exist


# Bulk operations
class BulkExtractResult(BaseModel):
    """Result of bulk extract insertion"""

    inserted_count: int
    failed_count: int = 0
    errors: List[str] = Field(default_factory=list)
    # NEW: UUID mappings for downstream stages (attribution, NLP2FOL)
    claim_uuid_mapping: Optional[Dict[str, str]] = None  # LLM claim_id -> DB UUID
    evidence_uuid_mapping: Optional[Dict[str, str]] = None  # LLM evidence_id -> DB UUID
