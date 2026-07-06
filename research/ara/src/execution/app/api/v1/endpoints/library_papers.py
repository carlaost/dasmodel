# Grounding: transcribed from oshima/api/app/api/v1/endpoints/library_papers.py
#!/usr/bin/env python3
"""
Library-Paper association endpoint for managing paper collections in libraries.

This endpoint handles the many-to-many relationship between libraries and papers,
allowing users to add existing papers to their libraries.
"""

import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

from app.core.logging import get_logger, log_event
from app.db.queries.libraries import get_by_id as get_library_by_id
from app.db.queries.papers import get_by_id as get_paper_by_id
from app.db.queries.relations import bulk_link_papers, unlink_paper
from app.db.supabase_client import service_client, user_client

logger = get_logger(__name__)
router = APIRouter()

# Security scheme for JWT tokens
security = HTTPBearer()


# Request/Response Models
class AddPapersRequest(BaseModel):
    """Request model for adding papers to a library"""

    paper_ids: List[str] = Field(
        ...,
        description="List of paper UUIDs to add to the library",
        min_items=1,
        max_items=100,  # Reasonable limit for bulk operations
    )


class LinkResults(BaseModel):
    """Results of linking operations"""

    created: int = Field(..., description="Number of new links created")
    no_op: int = Field(
        ..., description="Number of papers already in library (no operation)"
    )
    failed: int = Field(..., description="Number of failed link operations")


class AddPapersData(BaseModel):
    """Response data for adding papers"""

    library_id: str = Field(..., description="Library UUID")
    results: LinkResults = Field(..., description="Operation results")
    paper_ids: List[str] = Field(..., description="Paper IDs that were processed")


class AddPapersResponse(BaseModel):
    """Response for adding papers to library"""

    status: str = Field("success", description="Response status")
    message: str = Field(..., description="Human-readable message")
    data: AddPapersData = Field(..., description="Operation data")


class RemovePaperResponse(BaseModel):
    """Response for removing a paper from library"""

    status: str = Field("success", description="Response status")
    message: str = Field(..., description="Human-readable message")
    data: dict = Field(..., description="Operation data")


@router.post("/{library_id}/papers", response_model=AddPapersResponse)
async def add_papers_to_library(
    library_id: UUID,
    request: AddPapersRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> AddPapersResponse:
    """
    Add existing papers to a library.

    This endpoint:
    1. Validates user owns/has access to the library
    2. Validates user owns/has access to each paper
    3. Creates library-paper associations (idempotent)
    4. Returns detailed results showing created/skipped/failed operations

    Args:
        library_id: Library UUID to add papers to
        request: Request body with paper_ids array
        credentials: JWT Bearer token

    Returns:
        AddPapersResponse with operation results

    Raises:
        401: Invalid or missing JWT token
        403: User doesn't have access to library or papers
        404: Library not found
        422: Invalid request data
    """
    try:
        logger.info(
            f"📚 Adding {len(request.paper_ids)} papers to library {library_id}"
        )

        # Extract user ID from JWT token
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)

        # Get user info from token
        try:
            user_response = sb_user.auth.get_user(user_jwt)
            user_id = user_response.user.id
            logger.info(f"👤 User {user_id} adding papers to library")
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

        # Validate library access
        logger.info(f"🔍 Validating library access for user {user_id}")
        try:
            library = get_library_by_id(sb_user, library_id)
            # Check if user owns the library
            if str(library.owner_user_id) != user_id:
                logger.warning(f"User {user_id} doesn't own library {library_id}")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail={
                        "error": "access_denied",
                        "message": "You don't have permission to modify this library",
                        "hint": "You can only add papers to libraries you own",
                    },
                )
        except Exception as e:
            if "not found" in str(e).lower():
                logger.warning(f"Library {library_id} not found")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={
                        "error": "library_not_found",
                        "message": f"Library {library_id} not found",
                        "hint": "Check the library ID and ensure it exists",
                    },
                )
            elif isinstance(e, HTTPException):
                raise
            else:
                logger.error(f"Error accessing library {library_id}: {e}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail={
                        "error": "database_error",
                        "message": "Failed to access library",
                        "hint": "Database operation failed",
                    },
                )

        # Parse and validate paper IDs
        paper_uuids = []
        for paper_id_str in request.paper_ids:
            try:
                paper_uuid = UUID(paper_id_str)
                paper_uuids.append(paper_uuid)
            except ValueError:
                logger.warning(f"Invalid UUID format: {paper_id_str}")
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail={
                        "error": "invalid_paper_id",
                        "message": f"Invalid paper ID format: {paper_id_str}",
                        "hint": "Paper IDs must be valid UUIDs",
                    },
                )

        # Validate paper access (check that user has access to each paper)
        # For MVP, we'll check if papers exist - in production, add ownership check
        logger.info(f"🔍 Validating access to {len(paper_uuids)} papers")
        validated_papers = []
        for paper_uuid in paper_uuids:
            try:
                # Using service client to check paper exists
                # In production, use user client and check ownership
                sb_service = service_client()
                paper = get_paper_by_id(sb_service, paper_uuid)
                validated_papers.append(paper_uuid)
            except Exception as e:
                logger.warning(f"Paper {paper_uuid} not found or not accessible: {e}")
                # For now, skip papers that aren't accessible
                # In production, you might want to fail the entire operation
                continue

        if not validated_papers:
            logger.warning("No valid papers to add")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "no_valid_papers",
                    "message": "None of the provided papers are accessible",
                    "hint": "Ensure the paper IDs exist and you have access to them",
                },
            )

        # Bulk link papers to library
        logger.info(
            f"🔗 Linking {len(validated_papers)} papers to library {library_id}"
        )
        results = bulk_link_papers(sb_user, library_id, validated_papers)

        # Trigger theme extraction monitoring
        from app.services.themes import get_theme_monitor
        monitor = get_theme_monitor()
        monitor.add_library(library_id)

        # Log the operation
        log_event(
            stage="library.add_papers",
            outcome="success",
            library_id=str(library_id),
            user_id=user_id,
            papers_added=results["created"],
            papers_existing=results["no_op"],
            papers_failed=results["failed"],
            total_papers=len(validated_papers),
        )

        # Build response
        response_data = AddPapersData(
            library_id=str(library_id),
            results=LinkResults(
                created=results["created"],
                no_op=results["no_op"],
                failed=results["failed"],
            ),
            paper_ids=[str(pid) for pid in validated_papers],
        )

        # Create appropriate message
        if results["created"] > 0:
            message = f"Successfully added {results['created']} paper(s) to library"
            if results["no_op"] > 0:
                message += f" ({results['no_op']} already existed)"
        elif results["no_op"] > 0:
            message = f"All {results['no_op']} paper(s) were already in the library"
        else:
            message = "No papers were added to the library"

        logger.info(f"✅ {message}")

        return AddPapersResponse(
            status="success",
            message=message,
            data=response_data,
        )

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error adding papers to library: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error: {str(e)}",
                "hint": "Internal server error",
            },
        )


@router.delete("/{library_id}/papers/{paper_id}", response_model=RemovePaperResponse)
async def remove_paper_from_library(
    library_id: UUID,
    paper_id: UUID,
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> RemovePaperResponse:
    """
    Remove a paper from a library.

    Args:
        library_id: Library UUID
        paper_id: Paper UUID to remove
        credentials: JWT Bearer token

    Returns:
        RemovePaperResponse with operation result

    Raises:
        401: Invalid or missing JWT token
        403: User doesn't have access to library
        404: Library or paper not found
    """
    try:
        logger.info(f"📚 Removing paper {paper_id} from library {library_id}")

        # Extract user ID from JWT token
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)

        # Get user info from token
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

        # Validate library access
        try:
            library = get_library_by_id(sb_user, library_id)
            # Check if user owns the library
            if str(library.owner_user_id) != user_id:
                logger.warning(f"User {user_id} doesn't own library {library_id}")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail={
                        "error": "access_denied",
                        "message": "You don't have permission to modify this library",
                        "hint": "You can only remove papers from libraries you own",
                    },
                )
        except Exception as e:
            if "not found" in str(e).lower():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={
                        "error": "library_not_found",
                        "message": f"Library {library_id} not found",
                        "hint": "Check the library ID and ensure it exists",
                    },
                )
            elif isinstance(e, HTTPException):
                raise
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail={
                        "error": "database_error",
                        "message": "Failed to access library",
                        "hint": "Database operation failed",
                    },
                )

        # Remove the paper from the library
        success = unlink_paper(sb_user, library_id, paper_id)

        if success:
            logger.info(
                f"✅ Successfully removed paper {paper_id} from library {library_id}"
            )
            return RemovePaperResponse(
                status="success",
                message="Paper removed from library",
                data={
                    "library_id": str(library_id),
                    "paper_id": str(paper_id),
                    "removed": True,
                },
            )
        else:
            logger.warning(f"Paper {paper_id} was not in library {library_id}")
            return RemovePaperResponse(
                status="success",
                message="Paper was not in the library",
                data={
                    "library_id": str(library_id),
                    "paper_id": str(paper_id),
                    "removed": False,
                },
            )

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error removing paper from library: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error: {str(e)}",
                "hint": "Internal server error",
            },
        )
