# Grounding: transcribed from oshima/api/app/api/v1/endpoints/jobs_new.py
#!/usr/bin/env python3
"""
Job Management API Endpoints - Database-Only Version

Completely database-based job management using JobService.
Replaces all file-based operations with database operations.
"""

import json
import logging
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from fastapi.responses import JSONResponse
from supabase import Client

from app.api.deps import optional_supabase_user_client, supabase_service_client
from app.db.errors import DBError
from app.db.repositories import (
    extraction_runs_repo,
    libraries_repo,
    library_papers_repo,
    papers_repo,
)
from app.models.responses import (
    JobDeleteResponse,
    JobListResponse,
    JobLogsResponse,
    JobManifestResponse,
    JobStatusResponse,
    LibraryJobsResponse,
)
from app.services.jobs.job_service import get_job_service

logger = logging.getLogger(__name__)

router = APIRouter()

# Use centralized job service
job_service = get_job_service()


@router.get("/jobs/{doc_id}/status", response_model=JobStatusResponse)
def get_job_status(
    doc_id: str,
    supabase: Client = Depends(optional_supabase_user_client),
) -> JobStatusResponse:
    """Get job processing status from database"""
    try:
        # Get job summary from database
        summary = job_service.get_job_summary(doc_id)

        if not summary:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Job {doc_id} not found"
            )

        return JobStatusResponse(
            message="Job status retrieved successfully",
            data={
                "doc_id": summary["doc_id"],
                "status": summary["status"],
                "library_name": summary["library_name"],
                "filename": summary["filename"],
                "created_at": summary["created_at"],
                "updated_at": summary["updated_at"],
                "stages": summary.get("stages", {}),
                "total_duration_seconds": summary.get("total_duration_seconds"),
            },
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get job status for {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve job status",
        )


@router.get("/jobs/{doc_id}/manifest", response_model=JobManifestResponse)
def get_job_manifest(
    doc_id: str,
    supabase: Client = Depends(optional_supabase_user_client),
) -> JobManifestResponse:
    """Get complete job manifest from database"""
    try:
        # Load manifest from database
        manifest = job_service.load_job_manifest(doc_id)

        if not manifest:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Job manifest {doc_id} not found",
            )

        return JobManifestResponse(
            message="Job manifest retrieved successfully", data=manifest.model_dump()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get job manifest for {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve job manifest",
        )


@router.get("/jobs/{doc_id}/artifacts/{stage_name}/{artifact_name}")
def get_job_artifact(
    doc_id: str,
    stage_name: str,
    artifact_name: str,
    supabase: Client = Depends(optional_supabase_user_client),
):
    """Get specific job artifact from database"""
    try:
        # Get artifact from database
        artifact_data = job_service.get_artifact(doc_id, stage_name, artifact_name)

        if not artifact_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Artifact {stage_name}/{artifact_name} not found for job {doc_id}",
            )

        return JSONResponse(
            content={
                "message": "Artifact retrieved successfully",
                "data": artifact_data,
            }
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(
            f"Failed to get artifact {stage_name}/{artifact_name} for {doc_id}: {e}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve artifact",
        )


@router.get("/jobs/{doc_id}/final-output")
def get_job_final_output(
    doc_id: str,
    supabase: Client = Depends(optional_supabase_user_client),
):
    """Get final consolidated output from database"""
    try:
        # Get final output artifact from database
        final_output = job_service.get_artifact(doc_id, "consolidation", "final_output")

        if not final_output:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Final output not found for job {doc_id}",
            )

        # Get manifest for filename
        manifest = job_service.load_job_manifest(doc_id)
        filename = manifest.file_info.original_filename if manifest else "unknown"

        return JSONResponse(
            content=final_output,
            headers={
                "Content-Disposition": f'attachment; filename="{filename.rsplit(".", 1)[0]}_final_output.json"'
            },
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get final output for {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve final output",
        )


@router.get("/jobs/{doc_id}/artifacts")
def get_all_job_artifacts(
    doc_id: str,
    supabase: Client = Depends(optional_supabase_user_client),
):
    """Get all artifacts for a job from database"""
    try:
        # Get manifest to see available stages
        manifest = job_service.load_job_manifest(doc_id)

        if not manifest:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Job {doc_id} not found"
            )

        # Collect all artifacts from manifest stages
        all_artifacts = {}
        for stage_name, stage_result in manifest.stages.items():
            if hasattr(stage_result, "artifact_paths") and stage_result.artifact_paths:
                stage_artifacts = {}
                for (
                    artifact_name,
                    artifact_content,
                ) in stage_result.artifact_paths.items():
                    # If it's stored as content (new way), include it
                    if isinstance(artifact_content, dict):
                        stage_artifacts[artifact_name] = artifact_content
                    else:
                        # Legacy path reference, try to get from database
                        artifact_data = job_service.get_artifact(
                            doc_id, stage_name, artifact_name
                        )
                        if artifact_data:
                            stage_artifacts[artifact_name] = artifact_data

                if stage_artifacts:
                    all_artifacts[stage_name] = stage_artifacts

        return JSONResponse(
            content={
                "message": "All artifacts retrieved successfully",
                "data": {"doc_id": doc_id, "artifacts": all_artifacts},
            }
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get all artifacts for {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve artifacts",
        )


@router.get("/jobs", response_model=JobListResponse)
def list_jobs(
    limit: int = Query(default=50, le=1000),
    status_filter: Optional[str] = Query(default=None, alias="status"),
    supabase: Client = Depends(optional_supabase_user_client),
) -> JobListResponse:
    """List jobs from database"""
    try:
        if status_filter == "pending":
            # Get pending jobs
            pending_jobs = job_service.list_pending_jobs(limit=limit)

            jobs_data = []
            for job in pending_jobs:
                summary = job_service.get_job_summary(str(job["doc_id"]))
                if summary:
                    jobs_data.append(summary)

        else:
            # Get all jobs from database (would need a new database function)
            # For now, get pending jobs as a fallback
            pending_jobs = job_service.list_pending_jobs(limit=limit)
            jobs_data = []
            for job in pending_jobs:
                summary = job_service.get_job_summary(str(job["doc_id"]))
                if summary:
                    jobs_data.append(summary)

        return JobListResponse(message=f"Found {len(jobs_data)} jobs", data=jobs_data)

    except Exception as e:
        logger.error(f"Failed to list jobs: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve jobs",
        )


@router.delete("/jobs/{doc_id}", response_model=JobDeleteResponse)
def delete_job(
    doc_id: str,
    supabase: Client = Depends(optional_supabase_user_client),
) -> JobDeleteResponse:
    """Delete job and cleanup artifacts in database"""
    try:
        # Verify job exists
        manifest = job_service.load_job_manifest(doc_id)
        if not manifest:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Job {doc_id} not found"
            )

        # Cleanup job in database (soft delete)
        success = job_service.cleanup_job(doc_id)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete job",
            )

        return JobDeleteResponse(
            message="Job deleted successfully", data={"doc_id": doc_id, "deleted": True}
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete job {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete job",
        )


@router.get("/jobs/{doc_id}/logs", response_model=JobLogsResponse)
def get_job_logs(
    doc_id: str,
    lines: int = Query(default=100, le=10000),
    supabase: Client = Depends(optional_supabase_user_client),
) -> JobLogsResponse:
    """Get job processing logs (placeholder - logs are in application logs now)"""
    try:
        # Since we're database-only now, we don't have separate log files
        # Return a message indicating logs are in application logs
        return JobLogsResponse(
            message="Job logs retrieved (from application logs)",
            data={
                "doc_id": doc_id,
                "logs": [
                    "Job processing logs are now integrated into application logs.",
                    "Check the main application log for job processing details.",
                    f"Search for doc_id: {doc_id} to find relevant log entries.",
                ],
            },
        )

    except Exception as e:
        logger.error(f"Failed to get logs for {doc_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve logs",
        )


@router.get("/libraries/{library_name}/jobs", response_model=LibraryJobsResponse)
def list_library_jobs(
    library_name: str,
    supabase: Client = Depends(supabase_service_client),
) -> LibraryJobsResponse:
    """List all jobs in a library from database"""
    try:
        # For now, use a default user ID - in production this should come from auth
        user_id = "3acd2e99-37f3-4c7e-a06e-ffba087e0357"  # Test user

        # Get library collections from database
        collections = job_service.list_library_collections(library_name, user_id)

        # Get library stats
        stats = job_service.get_library_stats(library_name, user_id)

        return LibraryJobsResponse(
            message=f"Found {len(collections)} jobs in library {library_name}",
            data=collections,
            metadata=stats,
        )

    except Exception as e:
        logger.error(f"Failed to list jobs for library {library_name}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve library jobs",
        )


@router.get("/health")
def health_check():
    """Health check endpoint for job service"""
    try:
        health = job_service.health_check()
        return JSONResponse(content=health)
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(
            content={"status": "unhealthy", "error": str(e)}, status_code=500
        )
