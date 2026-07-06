# Grounding: transcribed from oshima/api/app/api/v1/api.py
"""API v1 router configuration."""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    artifacts,
    health,
    items,
    jobs,
    libraries,
    library_papers,
    papers,
    storage,
    themes,
    users,
)

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])

# Jobs endpoints - DISABLED: upload endpoint is broken (storage filename mismatch)
# api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
# Additional database-only job endpoints for newer functionality
from app.api.v1.endpoints.jobs_new import router as jobs_new_router

api_router.include_router(jobs_new_router, prefix="/jobs-new", tags=["jobs-new"])
api_router.include_router(artifacts.router, tags=["artifacts"])
api_router.include_router(libraries.router, prefix="/libraries", tags=["libraries"])
# Library-paper associations (must come after libraries but before papers for proper routing)
api_router.include_router(
    library_papers.router, prefix="/libraries", tags=["library-papers"]
)
# Library themes endpoint
api_router.include_router(themes.router, prefix="/libraries", tags=["themes"])
api_router.include_router(papers.router, prefix="/papers", tags=["papers"])
api_router.include_router(storage.router, prefix="/storage", tags=["storage"])

# TODO: Remove old jobs.py endpoints once fully migrated to new structure
