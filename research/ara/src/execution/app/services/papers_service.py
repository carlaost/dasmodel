# Grounding: transcribed from oshima/api/app/services/papers_service.py
#!/usr/bin/env python3
"""
Papers Service - Single entry point for paper upload and management

Handles the complete upload flow:
1. File validation (size, mime type, SHA256)
2. Idempotent paper creation by SHA256
3. Storage upload to pdf-papers bucket
4. Storage metadata attachment
5. Extraction run creation for processing pipeline
"""

import hashlib
import logging
from io import BytesIO
from typing import Dict, Optional, Tuple, Union
from uuid import UUID, uuid4

import requests

# Try to import python-magic, fall back to basic detection if not available
try:
    import magic

    HAS_MAGIC = True
except ImportError:
    HAS_MAGIC = False

from app.core.config import settings
from app.db.queries.extracts import upsert_extraction_run_by_job_id
from app.db.queries.papers import delete_paper as delete_paper_db
from app.db.queries.papers import (
    update_storage_fields,
    upsert_by_sha256,
)
from app.db.supabase_client import service_client, user_client
from app.services.service_utils import (
    ServiceError,
    ServiceErrorType,
    ServiceMetrics,
    handle_service_error,
)
from app.services.storage.storage_client import store_pdf_in_supabase

logger = logging.getLogger(__name__)

# Constants
MAX_FILE_SIZE = 40 * 1024 * 1024  # 40MB
STORAGE_BUCKET = "pdf-papers"
STORAGE_QUOTA_BYTES = 1024 * 1024 * 1024  # 1GB


class PapersServiceError(Exception):
    """Base exception for papers service"""

    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(message)


class ValidationError(PapersServiceError):
    """Validation errors (file too large, invalid PDF, etc.)"""

    pass


class StorageError(PapersServiceError):
    """Storage-related errors (quota exceeded, upload failed)"""

    pass


def compute_file_hash(file_content: bytes) -> str:
    """Compute SHA256 hash of file content"""
    return hashlib.sha256(file_content).hexdigest()


def validate_pdf_file(file_content: bytes, filename: str) -> Dict[str, Union[str, int]]:
    """
    Validate PDF file and return metadata

    Args:
        file_content: File content as bytes
        filename: Original filename

    Returns:
        Dict with file metadata: {
            "size_bytes": int,
            "mime_type": str,
            "sha256": str,
            "filename": str
        }

    Raises:
        ValidationError: If file is invalid
    """
    # Check file size
    file_size = len(file_content)
    if file_size > MAX_FILE_SIZE:
        raise ValidationError(
            f"File too large: {file_size} bytes (max: {MAX_FILE_SIZE} bytes)",
            error_code="FILE_TOO_LARGE",
        )

    if file_size == 0:
        raise ValidationError("Empty file", error_code="EMPTY_FILE")

    # Detect MIME type using python-magic if available
    if HAS_MAGIC:
        try:
            mime_type = magic.from_buffer(file_content, mime=True)
        except Exception as e:
            logger.warning(f"Failed to detect MIME type with magic: {e}")
            mime_type = "application/pdf"  # Assume PDF since we'll validate below
    else:
        # Fallback: assume PDF if it starts with PDF header
        mime_type = "application/pdf"

    # Check if it looks like a PDF
    if not (mime_type == "application/pdf" or file_content.startswith(b"%PDF")):
        raise ValidationError(
            f"Invalid PDF file: detected MIME type '{mime_type}'",
            error_code="INVALID_PDF",
        )

    # Compute SHA256
    sha256 = compute_file_hash(file_content)

    logger.info(
        f"📄 File validation passed: {filename} "
        f"({file_size} bytes, {mime_type}, {sha256[:16]}...)"
    )

    return {
        "size_bytes": file_size,
        "mime_type": mime_type,
        "sha256": sha256,
        "filename": filename,
    }


def get_bucket_usage() -> Optional[Dict[str, int]]:
    """
    Get current bucket usage stats using Supabase admin API

    Returns:
        Dict with usage info or None if unavailable: {
            "used_bytes": int,
            "quota_bytes": int,
            "remaining_bytes": int
        }
    """
    try:
        sb = service_client()

        # Use Supabase admin API for bucket usage (much more efficient)
        # GET https://<project>.supabase.co/storage/v1/admin/buckets/pdf-papers/usage

        # Extract base URL and headers from the service client
        base_url = sb.supabase_url
        headers = {
            "Authorization": f"Bearer {sb.supabase_key}",
            "Content-Type": "application/json",
        }

        usage_url = f"{base_url}/storage/v1/admin/buckets/{STORAGE_BUCKET}/usage"
        response = requests.get(usage_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data.get("file_size_bytes") is not None:
                used_bytes = int(data["file_size_bytes"])
                return {
                    "used_bytes": used_bytes,
                    "quota_bytes": STORAGE_QUOTA_BYTES,
                    "remaining_bytes": STORAGE_QUOTA_BYTES - used_bytes,
                }
            else:
                logger.warning(f"Unexpected bucket usage response format: {data}")
                return None
        else:
            logger.warning(
                f"Bucket usage API returned {response.status_code}: {response.text}"
            )
            return None

    except Exception as e:
        logger.warning(f"Failed to get bucket usage from admin API: {e}")
        return None


def check_storage_capacity(file_size: int) -> None:
    """
    Check if there's enough storage space for the file

    Args:
        file_size: Size of file to upload

    Raises:
        StorageError: If not enough space
    """
    usage = get_bucket_usage()

    if usage is None:
        # If we can't check usage, log warning but allow upload
        logger.warning("Cannot check storage usage - proceeding with upload")
        return

    if file_size > usage["remaining_bytes"]:
        raise StorageError(
            f"Storage quota exceeded: need {file_size} bytes, "
            f"only {usage['remaining_bytes']} bytes remaining "
            f"({usage['used_bytes']}/{usage['quota_bytes']} used)",
            error_code="STORAGE_QUOTA_EXCEEDED",
        )

    logger.debug(
        f"💾 Storage check passed: {file_size} bytes fits in "
        f"{usage['remaining_bytes']} bytes remaining"
    )


async def upload_paper(
    file_content: bytes,
    filename: str,
    user_id: UUID,
    title: Optional[str] = None,
    doi: Optional[str] = None,
    field: Optional[str] = None,
    topic: Optional[str] = None,
    library_id: Optional[UUID] = None,
) -> Dict[str, Union[str, UUID, bool]]:
    """
    Complete paper upload flow - single entry point

    Args:
        file_content: PDF file content as bytes
        filename: Original filename
        user_id: ID of user uploading the file
        title: Optional paper title (extracted from PDF if not provided)
        doi: Optional DOI
        field: Optional research field
        topic: Optional research topic
        library_id: Optional library to add paper to

    Returns:
        Upload result: {
            "paper_id": UUID,
            "status": "created|no-op",
            "storage_attached": bool,
            "extraction_run_id": UUID|None,
            "bucket_usage": dict|None
        }

    Raises:
        ValidationError: File validation failed
        StorageError: Storage operation failed
        PapersServiceError: Other service errors
    """
    try:
        logger.info(f"🚀 Starting paper upload: {filename} (user: {user_id})")

        # Step 1: Parse + validate input
        file_metadata = validate_pdf_file(file_content, filename)
        sha256 = file_metadata["sha256"]
        size_bytes = file_metadata["size_bytes"]
        mime_type = file_metadata["mime_type"]

        # Step 2: Check storage capacity
        check_storage_capacity(size_bytes)

        # Step 3: Upsert paper by SHA256 (idempotent create)
        sb = service_client()

        paper_data = {
            "title": title or filename.replace(".pdf", ""),
            "original_filename": filename,
            "doi": doi,
        }

        paper_id, paper_status = upsert_by_sha256(
            sb=sb, sha256=sha256, paper_data=paper_data, first_uploader_user_id=user_id
        )

        logger.info(f"📝 Paper upsert: {paper_status} (ID: {paper_id})")

        # Step 4: Upload to Storage (if paper was created or if storage not attached)
        storage_attached = False
        if paper_status == "created":
            try:
                # Use paper_id for storage filename
                storage_result = await store_pdf_in_supabase(
                    file_content=file_content,
                    original_filename=filename,
                    doc_id=str(paper_id),
                )


                logger.info(
                    f"📁 Storage upload successful: {storage_result['storage_path']}"
                )

                # Step 5: Attach storage metadata to paper
                success = update_storage_fields(
                    sb=sb,
                    paper_id=paper_id,
                    storage_bucket=STORAGE_BUCKET,
                    storage_path=storage_result["storage_path"],
                    mime_type=mime_type,
                    size_bytes=size_bytes,
                    sha256=sha256,
                )

                if success:
                    storage_attached = True
                    logger.info(f"✅ Storage metadata attached to paper {paper_id}")
                else:
                    raise StorageError(
                        "Failed to attach storage metadata", "METADATA_ATTACH_FAILED"
                    )

            except Exception as storage_error:
                logger.error(f"❌ Storage upload failed: {storage_error}")
                # TODO: Consider rolling back paper creation here
                raise StorageError(
                    f"Storage upload failed: {str(storage_error)}",
                    "STORAGE_UPLOAD_FAILED",
                )
        else:
            # Paper already existed - assume storage is attached
            storage_attached = True
            logger.info(f"📄 Paper already exists, skipping storage upload")

        # Step 6: Kick off processing (create extraction run)
        # Only create extraction run for NEW papers - existing papers already have extracts
        extraction_run_id = None
        if storage_attached and paper_status == "created":
            try:
                run_id, run_status = upsert_extraction_run_by_job_id(
                    sb=sb,
                    paper_id=paper_id,
                    job_id=None,  # Let it generate UUID
                    status="queued",
                    params={
                        "uploaded_by": str(user_id),
                        "original_filename": filename,
                        "upload_timestamp": "now()",
                    },
                )

                extraction_run_id = run_id
                logger.info(f"⚡ Extraction run {run_status}: {run_id}")

            except Exception as run_error:
                # Log error but don't fail the upload
                logger.error(f"⚠️ Failed to create extraction run: {run_error}")
        elif storage_attached and paper_status == "no-op":
            logger.info(f"📄 Paper already processed, skipping extraction run creation")

        # Step 7: Get final bucket usage for monitoring
        bucket_usage = get_bucket_usage()

        # Step 8: Return compact result
        result = {
            "paper_id": paper_id,
            "status": paper_status,
            "storage_attached": storage_attached,
            "extraction_run_id": extraction_run_id,
            "bucket_usage": bucket_usage,
        }

        logger.info(f"✅ Paper upload complete: {result}")
        return result

    except (ValidationError, StorageError) as e:
        # Re-raise service errors as-is
        logger.error(f"❌ Service error in upload_paper: {e}")
        raise

    except Exception as e:
        # Wrap unexpected errors
        logger.error(f"❌ Unexpected error in upload_paper: {e}")
        raise PapersServiceError(f"Unexpected error: {str(e)}", "INTERNAL_ERROR")


def get_paper_info(paper_id: UUID) -> Optional[Dict]:
    """
    Get paper information including storage status

    Args:
        paper_id: Paper UUID

    Returns:
        Paper info dict or None if not found
    """
    # TODO: Implement using queries.papers.get_by_id
    pass


def get_bucket_info() -> Dict[str, Union[int, float]]:
    """
    Get bucket usage information for monitoring

    Returns:
        Bucket stats: {
            "used_bytes": int,
            "quota_bytes": int,
            "remaining_bytes": int,
            "usage_percentage": float
        }
    """
    usage = get_bucket_usage()

    if usage is None:
        return {
            "used_bytes": 0,
            "quota_bytes": STORAGE_QUOTA_BYTES,
            "remaining_bytes": STORAGE_QUOTA_BYTES,
            "usage_percentage": 0.0,
        }

    usage_pct = (usage["used_bytes"] / usage["quota_bytes"]) * 100

    return {**usage, "usage_percentage": round(usage_pct, 2)}


def delete_paper(
    user_jwt: str,
    paper_id: UUID,
    delete_from_storage: bool = False,
    request_id: str = None,
) -> Dict[str, Union[str, int, Dict]]:
    """
    Delete paper and all related data with proper cascading

    Args:
        user_jwt: User's JWT token for authentication
        paper_id: Paper UUID to delete
        delete_from_storage: Whether to also delete from Supabase Storage
        request_id: Optional request ID for tracing

    Returns:
        Result dict: {
            "paper_id": UUID,
            "status": "deleted",
            "deleted_counts": {
                "library_papers": int,
                "extraction_runs": int,
                "extracts": int,
                "papers": int
            },
            "storage_deleted": bool
        }

    Raises:
        ServiceError: Normalized service errors with retry hints
    """
    with ServiceMetrics(
        "delete_paper", request_id=request_id, paper_id=paper_id
    ) as metrics:
        try:
            logger.info(f"🗑️ Starting paper deletion: {paper_id}")

            # Step 1: Validate inputs
            if not user_jwt:
                raise ServiceError(
                    "User JWT is required",
                    ServiceErrorType.VALIDATION_ERROR,
                    "MISSING_JWT",
                    "input_validation",
                )

            if not paper_id:
                raise ServiceError(
                    "Paper ID is required",
                    ServiceErrorType.VALIDATION_ERROR,
                    "MISSING_PAPER_ID",
                    "input_validation",
                )

            metrics.log_stage("input_validation", "success")

            # Step 2: Delete from database (cascading order)
            try:
                sb = user_client(user_jwt)  # User-scoped for RLS validation
                deleted_counts = delete_paper_db(sb, paper_id)

                metrics.log_stage(
                    "database_delete",
                    "success",
                    details={"deleted_counts": deleted_counts},
                )

                logger.info(f"📊 Database deletion completed: {deleted_counts}")

            except Exception as e:
                service_error = handle_service_error(e, "database_delete")
                metrics.log_stage(
                    "database_delete", "failed", details={"error": str(e)}
                )
                raise service_error

            # Step 3: Delete from storage (after DB delete succeeds)
            storage_deleted = False
            if delete_from_storage:
                try:
                    # Get storage path from deleted paper data if available
                    # For now, use paper_id-based path
                    storage_filename = f"{paper_id}.pdf"

                    sb_service = service_client()  # Service client for storage ops
                    response = sb_service.storage.from_(STORAGE_BUCKET).remove(
                        [storage_filename]
                    )

                    storage_deleted = True
                    metrics.log_stage("storage_delete", "success")
                    logger.info(f"📁 Storage deletion completed: {storage_filename}")

                except Exception as e:
                    # Log storage error but don't fail the operation
                    # DB integrity is more important than storage cleanup
                    logger.warning(f"⚠️ Storage deletion failed (non-critical): {e}")
                    metrics.log_stage(
                        "storage_delete", "failed", details={"error": str(e)}
                    )
                    storage_deleted = False

            # Step 4: Return result
            result = {
                "paper_id": paper_id,
                "status": "deleted",
                "deleted_counts": deleted_counts,
                "storage_deleted": storage_deleted,
            }

            logger.info(f"✅ Paper deletion complete: {result}")
            return result

        except ServiceError:
            # Re-raise ServiceErrors as-is
            raise

        except Exception as e:
            # Wrap unexpected errors
            service_error = handle_service_error(e, "delete_paper")
            raise service_error


def delete_storage_file(paper_id: UUID) -> bool:
    """
    Delete a paper's file from storage (utility function)

    Args:
        paper_id: Paper UUID

    Returns:
        bool: True if deleted successfully
    """
    try:
        storage_filename = f"{paper_id}.pdf"
        sb = service_client()

        response = sb.storage.from_(STORAGE_BUCKET).remove([storage_filename])
        logger.info(f"📁 Storage file deleted: {storage_filename}")
        return True

    except Exception as e:
        logger.error(f"❌ Storage file deletion failed: {e}")
        return False
