# Grounding: transcribed from oshima/api/app/api/v1/endpoints/themes.py
#!/usr/bin/env python3
"""
Themes endpoint for retrieving library themes.

Provides read-only access to extracted themes for libraries.
"""

import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.logging import get_logger
from app.db.queries.libraries import get_by_id as get_library_by_id
from app.db.supabase_client import service_client, user_client
from app.models.responses import ThemeData, ThemesResponse, ThemesResponseData

logger = get_logger(__name__)
router = APIRouter()

# Security scheme for JWT tokens
security = HTTPBearer()


@router.get("/{library_id}/themes", response_model=ThemesResponse)
async def get_library_themes(
    library_id: UUID,
    version: int | None = None,
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> ThemesResponse:
    """
    Get themes for a library.

    Returns the hierarchical theme structure extracted from library papers.
    Themes are returned as a flat list with parent_theme_id relationships.

    Args:
        library_id: Library UUID to get themes for
        version: Optional specific version to retrieve (defaults to latest)
        credentials: JWT Bearer token

    Returns:
        ThemesResponse with themes data

    Raises:
        401: Invalid or missing JWT token
        403: User doesn't have access to library
        404: Library not found or no themes available
    """
    try:
        logger.info(f"🎨 Getting themes for library {library_id}")

        # Extract user ID from JWT token
        user_jwt = credentials.credentials
        sb_user = user_client(user_jwt)

        # Get user info from token
        try:
            user_response = sb_user.auth.get_user(user_jwt)
            user_id = user_response.user.id
            logger.info(f"👤 User {user_id} requesting themes")
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
            library_name = library.name
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

        # Use service client for theme retrieval (themes aren't user-scoped)
        sb = service_client()

        # Determine which version to retrieve
        if version is None:
            # Get latest version
            version_result = sb.table("library_themes").select("version").eq(
                "library_id", str(library_id)
            ).order("version", desc=True).limit(1).execute()

            if not version_result.data:
                logger.warning(f"No themes found for library {library_id}")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={
                        "error": "themes_not_found",
                        "message": f"No themes available for library {library_id}",
                        "hint": "Theme extraction may not have completed yet",
                    },
                )

            version = version_result.data[0]["version"]
            logger.info(f"Retrieved latest version: {version}")

        # Get all themes for this version
        themes_result = sb.table("library_themes").select("*").eq(
            "library_id", str(library_id)
        ).eq("version", version).execute()

        if not themes_result.data:
            logger.warning(f"No themes found for library {library_id} version {version}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "error": "version_not_found",
                    "message": f"Version {version} not found for library {library_id}",
                    "hint": "Try omitting the version parameter to get the latest version",
                },
            )

        # Convert database rows to response format
        themes = []
        for row in themes_result.data:
            theme = ThemeData(
                theme_id=row["theme_id"],
                parent_theme_id=row["parent_theme_id"],
                level=row["level"],
                name=row["name"],
                description=row["description"],
                claim_ids=row["claim_ids"],
                key_concepts=row["key_concepts"],
                confidence=row["confidence"],
            )
            themes.append(theme)

        logger.info(f"✅ Retrieved {len(themes)} themes for library {library_id} (version {version})")

        return ThemesResponse(
            status="success",
            message=f"Retrieved {len(themes)} themes for library",
            data=ThemesResponseData(
                library_id=str(library_id),
                library_name=library_name,
                version=version,
                themes=themes,
                total_themes=len(themes),
            ),
        )

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error getting library themes: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error: {str(e)}",
                "hint": "Internal server error",
            },
        )
