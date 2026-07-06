# Grounding: transcribed from oshima/api/app/api/v1/endpoints/papers.py
#!/usr/bin/env python3
"""
Papers endpoint for upload and retrieval with service layer integration
"""

import logging
from typing import Dict, List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.db.queries.extracts import get_latest_extraction_run_by_paper_id
from app.db.queries.libraries import list_by_user_id as list_libraries_by_user_id
from app.db.queries.papers import get_by_id as get_paper_by_id
from app.db.queries.papers import get_user_papers
from app.db.supabase_client import service_client, user_client
from app.models.responses import (
    LibraryFullPaperMetadata,
    PaperData,
    PaperResponse,
    PaperUploadData,
    PaperUploadResponse,
    ProcessingInfo,
    StorageInfo,
    UserPaper,
    UserPapersMetadata,
    UserPapersResponse,
)
from app.services.papers_service import (
    PapersServiceError,
    StorageError,
    ValidationError,
    upload_paper,
)
from app.services.service_utils import ServiceError, ServiceErrorType

logger = logging.getLogger(__name__)
router = APIRouter()

# Security scheme for JWT tokens
security = HTTPBearer()


@router.get("/", response_model=UserPapersResponse)
async def list_user_papers(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserPapersResponse:
    """
    List all papers for the authenticated user

    Aggregates papers from all user's libraries, deduplicates by paper ID,
    and returns with metadata including total claims and evidence counts.

    Args:
        credentials: JWT Bearer token

    Returns:
        List of user's papers with aggregated metadata

    Raises:
        401: Invalid or missing JWT token
        500: Internal service error
    """
    try:
        logger.info("📄 Listing all papers for authenticated user")

        # Extract user ID from JWT token
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)
        sb_service = service_client()

        # Get user info from token to extract user_id
        try:
            user_response = sb_user.auth.get_user(user_jwt)
            user_id = user_response.user.id
            # logger.info(f"👤 Authenticated user: {user_id}")
        except Exception as e:
            logger.error(f"Failed to extract user from JWT: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "error": "invalid_token",
                    "message": "Failed to extract user information from JWT token",
                    "hint": "Ensure your JWT token is valid and not expired",
                },
            )

        # Get all papers for user (papers table only, no extracts)
        try:
            papers = get_user_papers(sb_user, UUID(user_id))
            logger.info(f"📚 Found {len(papers)} papers for user")
        except Exception as e:
            logger.error(f"Failed to get user papers: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "error": "database_error",
                    "message": "Failed to retrieve user's papers",
                    "hint": "Database operation failed",
                },
            )

        # Transform Paper DB models to UserPaper response models
        user_papers = []
        for paper in papers:
            paper_metadata = LibraryFullPaperMetadata(
                title=paper.title or "Untitled",
                doi=paper.doi,
                num_pages=paper.num_pages,
                original_filename=paper.original_filename,
                sha256=paper.sha256,
                size_bytes=paper.size_bytes,
                created_at=paper.created_at.isoformat() if paper.created_at else None,
            )

            user_paper = UserPaper(
                id=str(paper.id),
                metadata=paper_metadata,
            )
            user_papers.append(user_paper)

        # Create metadata (counts set to 0 since we're not querying extracts)
        metadata = UserPapersMetadata(
            total_papers=len(user_papers),
            total_claims=0,
            total_evidence=0,
            libraries_count=0,
        )

        logger.info(f"📊 Returning {len(user_papers)} papers for user")

        return UserPapersResponse(status="success", data=user_papers, metadata=metadata)

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error listing user papers: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error listing papers: {str(e)}",
                "hint": "Internal server error",
            },
        )


def map_service_error_to_http_status(error: Exception) -> tuple[int, dict]:
    """
    Map service errors to HTTP status codes and response format

    Args:
        error: Service error to map

    Returns:
        Tuple of (status_code, detail_dict)
    """
    if isinstance(error, ValidationError):
        if error.error_code == "FILE_TOO_LARGE":
            return status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, {
                "error": "file_too_large",
                "message": error.message,
                "hint": "Reduce file size or split into smaller files",
            }
        elif error.error_code in ("INVALID_PDF", "EMPTY_FILE"):
            return status.HTTP_422_UNPROCESSABLE_ENTITY, {
                "error": "invalid_file",
                "message": error.message,
                "hint": "Upload a valid PDF file",
            }
        else:
            return status.HTTP_422_UNPROCESSABLE_ENTITY, {
                "error": "validation_error",
                "message": error.message,
                "hint": "Check your file and try again",
            }

    elif isinstance(error, StorageError):
        if error.error_code == "STORAGE_QUOTA_EXCEEDED":
            return status.HTTP_507_INSUFFICIENT_STORAGE, {
                "error": "storage_quota_exceeded",
                "message": error.message,
                "hint": "Storage quota exceeded, please contact support",
            }
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {
                "error": "storage_error",
                "message": error.message,
                "hint": "Storage operation failed, please try again",
            }

    elif isinstance(error, ServiceError):
        if error.error_type == ServiceErrorType.VALIDATION_ERROR:
            return status.HTTP_422_UNPROCESSABLE_ENTITY, {
                "error": "validation_error",
                "message": error.message,
                "hint": "Check your request data",
            }
        elif error.error_type == ServiceErrorType.AUTH:
            return status.HTTP_403_FORBIDDEN, {
                "error": "access_denied",
                "message": error.message,
                "hint": "Check your authentication token",
            }
        elif error.error_type == ServiceErrorType.NOT_FOUND:
            return status.HTTP_404_NOT_FOUND, {
                "error": "not_found",
                "message": error.message,
                "hint": "Resource does not exist",
            }
        elif error.error_type == ServiceErrorType.CONFLICT:
            return status.HTTP_409_CONFLICT, {
                "error": "conflict",
                "message": error.message,
                "hint": "Resource conflict detected",
            }
        elif error.error_type in (ServiceErrorType.TIMEOUT, ServiceErrorType.TRANSIENT):
            return status.HTTP_503_SERVICE_UNAVAILABLE, {
                "error": "service_unavailable",
                "message": error.message,
                "hint": "Service temporarily unavailable, please retry",
            }
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {
                "error": "internal_error",
                "message": error.message,
                "hint": "Internal service error",
            }

    elif isinstance(error, PapersServiceError):
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {
            "error": "papers_service_error",
            "message": error.message,
            "hint": "Paper service operation failed",
        }

    else:
        # Generic error fallback
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {
            "error": "internal_error",
            "message": f"Unexpected error: {str(error)}",
            "hint": "Internal server error",
        }


@router.post(
    "/", response_model=PaperUploadResponse, status_code=status.HTTP_201_CREATED
)
async def upload_paper_file(
    file: UploadFile = File(..., description="PDF file to upload"),
    title: Optional[str] = Form(None, description="Paper title (optional)"),
    doi: Optional[str] = Form(None, description="Paper DOI (optional)"),
    field: Optional[str] = Form(None, description="Research field (optional)"),
    topic: Optional[str] = Form(None, description="Research topic (optional)"),
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> PaperUploadResponse:
    """
    Upload a PDF paper with automatic processing

    Content-Type: multipart/form-data

    Flow:
    1. Validate file (PDF, size limits)
    2. Compute SHA256 → upsert by SHA256 (idempotent)
    3. Upload to Storage (service client)
    4. Write storage metadata (bucket/path/mime/size/sha256)
    5. Create extraction_runs row with status='queued'

    Args:
        file: PDF file upload (multipart/form-data)
        title: Optional paper title
        doi: Optional paper DOI
        field: Optional research field
        topic: Optional research topic
        credentials: JWT Bearer token

    Returns:
        201: Upload successful with paper info
        202: Could also use this to emphasize async processing

    Edge cases:
        - Same file twice → no-op (status: 'no-op')
        - Failed Storage upload → retryable error, paper in non-ready state
        - Invalid file → 422 validation error
        - Storage quota exceeded → 507 insufficient storage
    """
    try:
        logger.info(f"📤 Paper upload started: {file.filename}")

        # Extract user ID from JWT token
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)

        # Get user info from token to extract user_id
        try:
            user_response = sb_user.auth.get_user(user_jwt)
            user_id = user_response.user.id
        except Exception as e:
            logger.error(f"Failed to extract user from JWT: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "error": "invalid_token",
                    "message": "Failed to extract user information from JWT token",
                    "hint": "Ensure your JWT token is valid and not expired",
                },
            )

        # Validate file is PDF
        if file.content_type not in ("application/pdf", "application/x-pdf"):
            raise ValidationError(
                f"Invalid file type: {file.content_type}. Only PDF files are allowed.",
                "INVALID_MIME_TYPE",
            )

        # Read file content
        file_content = await file.read()

        # Use papers service for upload
        result = await upload_paper(
            file_content=file_content,
            filename=file.filename or "untitled.pdf",
            user_id=UUID(user_id),
            title=title,
            doi=doi,
            field=field,
            topic=topic,
        )

        # Map result to response model
        upload_data = PaperUploadData(
            paper_id=str(result["paper_id"]),
            status=result["status"],
            storage_attached=result["storage_attached"],
            extraction_run_id=(
                str(result["extraction_run_id"])
                if result["extraction_run_id"]
                else None
            ),
            processing_status="queued" if result["extraction_run_id"] else None,
            bucket_usage=result["bucket_usage"],
        )

        # Return 201 for created, 200 for no-op
        response_status = (
            status.HTTP_201_CREATED
            if result["status"] == "created"
            else status.HTTP_200_OK
        )

        logger.info(
            f"✅ Paper upload completed: {result['paper_id']} ({result['status']})"
        )

        return PaperUploadResponse(status="success", data=upload_data)

    except (ValidationError, StorageError, PapersServiceError, ServiceError) as e:
        logger.error(f"❌ Paper upload service error: {e}")
        status_code, detail = map_service_error_to_http_status(e)
        raise HTTPException(status_code=status_code, detail=detail)

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected paper upload error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected upload error: {str(e)}",
                "hint": "Internal server error during upload",
            },
        )


@router.get("/{paper_id}", response_model=PaperResponse)
def get_paper(
    paper_id: UUID,
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> PaperResponse:
    """
    Get paper information including storage refs and processing status

    Returns:
        - Paper metadata (title, DOI, etc.)
        - Storage information (bucket, path, mime, size, sha256)
        - Processing status and extraction run info

    Raises:
        404: Paper not found or user doesn't have access
        401: Invalid or missing JWT token
        403: User doesn't have permission to access this paper
    """
    try:
        logger.info(f"📄 Getting paper: {paper_id}")

        # Create user-scoped client for RLS enforcement
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)

        # Get paper data using .single() query (will 404 if not found/accessible)
        try:
            paper = get_paper_by_id(sb_user, paper_id)
        except Exception as e:
            if "not found" in str(e).lower() or "no rows" in str(e).lower():
                logger.warning(f"Paper {paper_id} not found or access denied")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={
                        "error": "paper_not_found",
                        "message": f"Paper {paper_id} not found or access denied",
                        "hint": "Check the paper ID and ensure you have access to this paper",
                    },
                )
            else:
                logger.error(f"Database error getting paper {paper_id}: {e}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail={
                        "error": "database_error",
                        "message": "Failed to retrieve paper from database",
                        "hint": "Database operation failed",
                    },
                )

        # Get latest extraction run for processing status
        processing_info = ProcessingInfo()
        try:
            # Use service client for extraction run query (might not be user-visible)
            sb_service = service_client()
            extraction_run = get_latest_extraction_run_by_paper_id(sb_service, paper_id)
            if extraction_run:
                processing_info = ProcessingInfo(
                    extraction_run_id=str(extraction_run.id),
                    status=extraction_run.status,
                    created_at=(
                        extraction_run.created_at.isoformat()
                        if extraction_run.created_at
                        else None
                    ),
                    updated_at=(
                        extraction_run.updated_at.isoformat()
                        if extraction_run.updated_at
                        else None
                    ),
                )
        except Exception as e:
            logger.warning(f"Failed to get extraction run for paper {paper_id}: {e}")
            # Continue without processing info if extraction run query fails

        # Build storage info
        storage_info = StorageInfo(
            storage_bucket=paper.storage_bucket,
            storage_path=paper.storage_path,
            storage_url=(
                f"supabase://{paper.storage_bucket}/{paper.storage_path}"
                if paper.storage_bucket and paper.storage_path
                else None
            ),
            mime_type=paper.mime_type,
            size_bytes=paper.size_bytes,
            sha256=paper.sha256,
        )

        # Build paper data response
        paper_data = PaperData(
            paper_id=str(paper.id),
            title=paper.title,
            doi=paper.doi,
            original_filename=paper.original_filename,
            num_pages=paper.num_pages,
            created_at=paper.created_at.isoformat(),
            updated_at=paper.updated_at.isoformat() if paper.updated_at else None,
            first_uploader_user_id=(
                str(paper.first_uploader_user_id)
                if paper.first_uploader_user_id
                else None
            ),
            storage=storage_info,
            processing=processing_info,
        )

        logger.info(f"✅ Paper retrieved successfully: {paper_id}")

        return PaperResponse(status="success", data=paper_data)

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error getting paper {paper_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error retrieving paper: {str(e)}",
                "hint": "Internal server error",
            },
        )
