# Grounding: transcribed from oshima/api/app/services/jobs/job_service.py
#!/usr/bin/env python3
"""
Centralized Job Service - Complete Database Replacement for JobManager

This service completely replaces all file-based JobManager operations with
database-only operations using Supabase. All job management, artifact storage,
library management, and manifest operations are now database-backed.
"""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from app.db.supabase_client import service_client
from app.models.job_manifest import FileInfo, JobManifest, StageStatus
from app.services.manifests.db_manifest_manager import DatabaseManifestManager

logger = logging.getLogger(__name__)


class JobService:
    """
    Centralized service for ALL job-related operations using database-only storage.

    Completely replaces JobManager class with database-backed operations:
    - Job manifest storage/retrieval
    - Library management
    - Artifact storage
    - Job listing and status
    - Duplicate detection
    - Job cleanup
    """

    def __init__(self):
        """Initialize service with database connections"""
        self.supabase = service_client()
        self.manifest_manager = DatabaseManifestManager()
        logger.info("JobService initialized with database-only operations")

    # === JOB MANIFEST OPERATIONS ===

    def load_job_manifest(self, doc_id: str) -> Optional[JobManifest]:
        """Load job manifest from database"""
        return self.manifest_manager.load_job_manifest(doc_id)

    def save_job_manifest(self, manifest: JobManifest) -> bool:
        """Save job manifest to database"""
        return self.manifest_manager.save_job_manifest(manifest)

    def get_job_summary(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Get job summary from database"""
        try:
            result = self.supabase.rpc(
                "get_job_summary", {"doc_id_param": doc_id}
            ).execute()
            return result.data if result.data else None
        except Exception as e:
            logger.error(f"Failed to get job summary for {doc_id}: {e}")
            return None

    # === LIBRARY MANAGEMENT ===

    def get_or_create_library(
        self,
        library_name: str,
        user_id: str,
        field: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Optional[str]:
        """Get or create library in database"""
        try:
            result = self.supabase.rpc(
                "get_or_create_library",
                {
                    "library_name_param": library_name,
                    "user_id_param": user_id,
                    "field_param": field,
                    "topic_param": topic,
                },
            ).execute()
            return str(result.data) if result.data else None
        except Exception as e:
            logger.error(f"Failed to get/create library {library_name}: {e}")
            return None

    def list_user_libraries(self, user_id: str) -> List[Dict[str, Any]]:
        """List all libraries for a user from database"""
        try:
            result = self.supabase.rpc(
                "list_user_libraries", {"user_id_param": user_id}
            ).execute()
            return result.data or []
        except Exception as e:
            logger.error(f"Failed to list libraries for user {user_id}: {e}")
            return []

    def list_library_collections(
        self, library_name: str, user_id: str
    ) -> List[Dict[str, Any]]:
        """List all collections in a library from database"""
        try:
            result = self.supabase.rpc(
                "list_library_collections",
                {"library_name_param": library_name, "user_id_param": user_id},
            ).execute()
            return result.data or []
        except Exception as e:
            logger.error(f"Failed to list collections for library {library_name}: {e}")
            return []

    # === JOB OPERATIONS ===

    def list_pending_jobs(self, limit: int = 100) -> List[Dict[str, Any]]:
        """List pending jobs from database"""
        try:
            result = self.supabase.rpc(
                "list_pending_jobs", {"limit_param": limit}
            ).execute()
            return result.data or []
        except Exception as e:
            logger.error(f"Failed to list pending jobs: {e}")
            return []

    def find_duplicate_by_hash(self, file_hash: str) -> Optional[str]:
        """Find duplicate job by file hash from database"""
        try:
            result = self.supabase.rpc(
                "find_duplicate_by_hash", {"hash_param": file_hash}
            ).execute()
            return str(result.data) if result.data else None
        except Exception as e:
            logger.error(f"Failed to find duplicate by hash {file_hash}: {e}")
            return None

    def cleanup_job(self, doc_id: str) -> bool:
        """Cleanup job (soft delete) in database"""
        try:
            result = self.supabase.rpc(
                "cleanup_job", {"doc_id_param": doc_id}
            ).execute()
            return bool(result.data)
        except Exception as e:
            logger.error(f"Failed to cleanup job {doc_id}: {e}")
            return False

    # === ARTIFACT OPERATIONS ===

    def store_artifact(
        self, doc_id: str, stage_name: str, artifact_name: str, content: Dict[str, Any]
    ) -> bool:
        """Store artifact in database"""
        try:
            result = self.supabase.rpc(
                "store_job_artifact",
                {
                    "doc_id_param": doc_id,
                    "stage_name_param": stage_name,
                    "artifact_name_param": artifact_name,
                    "content_param": content,
                },
            ).execute()
            return bool(result.data)
        except Exception as e:
            logger.error(
                f"Failed to store artifact {stage_name}/{artifact_name} for {doc_id}: {e}"
            )
            return False

    def get_artifact(
        self, doc_id: str, stage_name: str, artifact_name: str
    ) -> Optional[Dict[str, Any]]:
        """Get artifact from database"""
        try:
            result = self.supabase.rpc(
                "get_job_artifact",
                {
                    "doc_id_param": doc_id,
                    "stage_name_param": stage_name,
                    "artifact_name_param": artifact_name,
                },
            ).execute()
            return result.data if result.data else None
        except Exception as e:
            logger.error(
                f"Failed to get artifact {stage_name}/{artifact_name} for {doc_id}: {e}"
            )
            return None

    # === JOB CREATION ===

    def create_job_manifest(
        self,
        user_id: str,
        library_name: str,
        file_info: FileInfo,
        field: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Optional[JobManifest]:
        """Create new job manifest in database (replaces create_job_from_file)"""
        try:
            # Get or create library
            library_id = self.get_or_create_library(library_name, user_id, field, topic)
            if not library_id:
                logger.error(f"Failed to create library {library_name}")
                return None

            # Create initial manifest
            manifest = self.manifest_manager.create_initial_manifest(
                doc_id=None,  # Will be generated
                job_id=None,  # Will be generated
                file_info=file_info,
                user_id=user_id,
                field=field,
                topic=topic,
                library_name=library_name,
            )

            # Save to database
            success = self.save_job_manifest(manifest)
            if not success:
                logger.error(
                    f"Failed to save manifest for {file_info.original_filename}"
                )
                return None

            logger.info(
                f"Created job manifest {manifest.doc_id} in library {library_name}"
            )
            return manifest

        except Exception as e:
            logger.error(f"Failed to create job manifest: {e}")
            return None

    # === STATUS OPERATIONS ===

    def update_job_status(
        self, doc_id: str, status: str, error_message: Optional[str] = None
    ) -> bool:
        """Update job status in database"""
        try:
            update_data = {
                "status": status,
                "updated_at": datetime.utcnow().isoformat(),
            }

            if error_message:
                update_data["error_message"] = error_message

            result = (
                self.supabase.table("extraction_runs")
                .update(update_data)
                .eq("id", doc_id)
                .execute()
            )
            return len(result.data) > 0
        except Exception as e:
            logger.error(f"Failed to update job status for {doc_id}: {e}")
            return False

    # === LEGACY FILE-BASED METHOD REPLACEMENTS ===

    def calculate_file_hash(self, file_content: bytes) -> str:
        """Calculate SHA256 hash of file content (no longer file-path based)"""
        import hashlib

        return hashlib.sha256(file_content).hexdigest()

    def get_job_by_library_and_filename(
        self, library_name: str, filename: str, user_id: str
    ) -> Optional[str]:
        """Find job by library and filename"""
        try:
            # Query through papers table - check both original_filename and title
            result = (
                self.supabase.table("extraction_runs")
                .select(
                    """
                id,
                papers!inner(title, original_filename),
                library_papers!inner(
                    libraries!inner(name, owner_user_id)
                )
            """
                )
                .or_(
                    f"papers.original_filename.eq.{filename},papers.title.eq.{filename}"
                )
                .eq("library_papers.libraries.name", library_name)
                .eq("library_papers.libraries.owner_user_id", user_id)
                .execute()
            )

            if result.data:
                return result.data[0]["id"]
            return None
        except Exception as e:
            logger.error(
                f"Failed to find job by library {library_name} and filename {filename}: {e}"
            )
            return None

    # === UTILITY METHODS ===

    def get_library_stats(self, library_name: str, user_id: str) -> Dict[str, Any]:
        """Get library statistics"""
        collections = self.list_library_collections(library_name, user_id)

        total_jobs = len(collections)
        completed_jobs = len([c for c in collections if c.get("status") == "completed"])
        failed_jobs = len([c for c in collections if c.get("status") == "failed"])
        pending_jobs = len([c for c in collections if c.get("status") == "pending"])

        return {
            "total_jobs": total_jobs,
            "completed_jobs": completed_jobs,
            "failed_jobs": failed_jobs,
            "pending_jobs": pending_jobs,
            "progress_percentage": (
                (completed_jobs / total_jobs * 100) if total_jobs > 0 else 0
            ),
        }

    def health_check(self) -> Dict[str, Any]:
        """Check service health"""
        try:
            # Test database connection
            result = (
                self.supabase.table("extraction_runs").select("id").limit(1).execute()
            )

            return {
                "status": "healthy",
                "database_connected": True,
                "timestamp": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "database_connected": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
            }


# Global service instance
_job_service = None


def get_job_service() -> JobService:
    """Get singleton job service instance"""
    global _job_service
    if _job_service is None:
        _job_service = JobService()
    return _job_service
