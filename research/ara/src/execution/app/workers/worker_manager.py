# Grounding: transcribed from oshima/api/app/workers/worker_manager.py
#!/usr/bin/env python3
"""
Parallel Worker Manager for Job Processing

Manages a pool of background job processing workers with database-based job claiming.
Supports parallel processing with thread pools, job claiming, rate limiting, and
connection pooling for external services.
"""

import asyncio
import logging
import os
import signal
import subprocess
import threading
import time
import uuid
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set

from supabase import Client

from app.core.config import settings
from app.db.supabase_client import service_client
from app.middlewares.rate_limiter import get_llm_rate_limiter
from app.services.corenlp_client import close_corenlp_client, get_corenlp_client
from app.services.jobs.job_service import get_job_service
from app.services.pipeline.storage_pipeline import StoragePipeline

logger = logging.getLogger(__name__)


class ParallelWorkerManager:
    """
    Manages a pool of background job processing workers with database-based job claiming.

    This class handles:
    - Parallel worker threads with ThreadPoolExecutor
    - Database-based atomic job claiming to prevent conflicts
    - Rate limiting for LLM API calls
    - Connection pooling for CoreNLP servers
    - Graceful startup/shutdown with resource cleanup
    - Health monitoring and metrics collection
    """

    def __init__(
        self,
        model: str = "gpt-5-mini-2025-08-07",
        worker_count: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ):
        """
        Initialize parallel worker manager.

        Args:
            model: OpenAI model to use for extraction
            worker_count: Number of worker threads (defaults to settings.WORKER_COUNT)
            poll_interval: Seconds between job checks when queue is empty
        """
        self.model = model
        self.worker_count = worker_count or settings.WORKER_COUNT
        self.poll_interval = poll_interval or settings.JOB_POLL_SEC

        # Generate unique worker ID for this manager instance
        self.manager_id = f"manager-{uuid.uuid4().hex[:8]}"

        # Components
        self.job_service = None
        self.db_client = None
        self.corenlp_client = None
        self.rate_limiter = None

        # Thread pool for parallel workers
        self._executor: Optional[ThreadPoolExecutor] = None
        self._worker_futures: List[Future] = []

        # Control and coordination
        self._running = False
        self._shutdown_event = threading.Event()
        self._stats_lock = threading.Lock()

        # Statistics and monitoring
        self._worker_stats = {
            "jobs_claimed": 0,
            "jobs_completed": 0,
            "jobs_failed": 0,
            "total_processing_time": 0.0,
            "last_activity": None,
            "active_workers": 0,
        }

        # Active job tracking
        self._active_jobs: Dict[str, Dict] = {}  # job_id -> job_info
        self._active_jobs_lock = threading.Lock()

        logger.info(f"ParallelWorkerManager initialized:")
        logger.info(f"  Model: {model}")
        logger.info(f"  Workers: {self.worker_count}")
        logger.info(f"  Poll interval: {self.poll_interval}s")
        logger.info(f"  Manager ID: {self.manager_id}")

    async def start_worker(self) -> None:
        """
        Start the parallel job processing workers.
        Called during FastAPI startup.
        """
        if self._running:
            logger.warning("Workers are already running")
            return

        if not settings.WORKER_ENABLED:
            logger.info("🔕 Workers disabled by configuration")
            return

        logger.info(
            f"🚀 Starting {self.worker_count} parallel job processing workers..."
        )

        try:
            # Clean up any stuck system processes from previous runs FIRST
            # This prevents killing workers we're about to create
            await self._cleanup_system_processes()

            # Initialize shared components
            self.job_service = get_job_service()
            self.db_client = service_client()
            self.corenlp_client = get_corenlp_client()
            self.rate_limiter = get_llm_rate_limiter()

            # Set running flag
            self._running = True
            self._shutdown_event.clear()

            # Create thread pool executor
            self._executor = ThreadPoolExecutor(
                max_workers=self.worker_count,
                thread_name_prefix=f"Worker-{self.manager_id}",
            )

            # Start worker threads
            self._worker_futures = []
            for worker_id in range(self.worker_count):
                worker_name = f"{self.manager_id}-worker-{worker_id}"
                future = self._executor.submit(self._worker_loop, worker_name)
                self._worker_futures.append(future)

            logger.info(f"✅ Started {self.worker_count} parallel workers successfully")

        except Exception as e:
            logger.error(f"❌ Failed to start parallel workers: {e}")
            self._running = False
            # Cleanup on failure
            if self._executor:
                self._executor.shutdown(wait=False)
            raise

    async def stop_worker(self) -> None:
        """
        Stop all parallel job processing workers.
        Called during FastAPI shutdown.
        """
        if not self._running:
            logger.info("Workers are not running")
            return

        logger.info(f"🛑 Stopping {self.worker_count} parallel workers...")

        # Signal shutdown to all workers
        self._running = False
        self._shutdown_event.set()

        # Wait for all worker futures to complete (with timeout)
        if self._executor:
            logger.info("Waiting for worker threads to finish...")

            # Give workers time to finish current jobs
            shutdown_timeout = 30
            try:
                self._executor.shutdown(wait=True, timeout=shutdown_timeout)
                logger.info("✅ All worker threads stopped successfully")
            except Exception as e:
                logger.warning(f"Some worker threads did not stop cleanly: {e}")

        # Release any active job claims
        await self._cleanup_active_claims()

        # Clean up resources
        if self.corenlp_client:
            close_corenlp_client()

        self.job_service = None
        self.db_client = None
        self.corenlp_client = None
        self.rate_limiter = None
        self._executor = None
        self._worker_futures.clear()

        logger.info("✅ Parallel worker shutdown completed")

    async def _cleanup_system_processes(self) -> None:
        """Kill only specific stuck processes that might interfere with workers."""
        try:
            logger.info("🧹 Checking for stuck worker processes from previous runs...")

            current_pid = os.getpid()
            current_parent_pid = os.getppid()  # uvicorn reloader process
            killed_any = False

            # Look for processes with our manager IDs (these are definitely our workers)
            result = subprocess.run(
                ["pgrep", "-f", "manager-.*-worker"], capture_output=True, text=True
            )
            if result.stdout:
                worker_pids = [
                    pid.strip()
                    for pid in result.stdout.strip().split("\n")
                    if pid.strip()
                ]
                for pid in worker_pids:
                    if pid and int(pid) not in [current_pid, current_parent_pid]:
                        logger.info(f"🔫 Killing stuck worker process: {pid}")
                        subprocess.run(
                            ["kill", "-9", pid], check=False, capture_output=True
                        )
                        killed_any = True

            # Check for processes holding port 8000 (but not current process)
            result = subprocess.run(
                ["lsof", "-ti:8000"], capture_output=True, text=True
            )
            if result.stdout:
                port_pids = [
                    pid.strip()
                    for pid in result.stdout.strip().split("\n")
                    if pid.strip()
                ]
                for pid in port_pids:
                    if pid and int(pid) not in [current_pid, current_parent_pid]:
                        logger.info(f"🔫 Killing process holding port 8000: {pid}")
                        subprocess.run(
                            ["kill", "-9", pid], check=False, capture_output=True
                        )
                        killed_any = True

            if killed_any:
                # Wait a moment for processes to die
                await asyncio.sleep(1)
                logger.info("✅ Cleaned up stuck processes")
            else:
                logger.info("✅ No stuck processes found")

        except Exception as e:
            logger.warning(f"⚠️ Process cleanup failed (continuing anyway): {e}")

    async def _cleanup_active_claims(self) -> None:
        """Clean up any job claims held by this manager's workers."""
        with self._active_jobs_lock:
            if not self._active_jobs:
                return

            logger.info(f"🧹 Cleaning up {len(self._active_jobs)} active job claims...")

            for job_id in list(self._active_jobs.keys()):
                try:
                    # Release the job claim in database
                    result = self.db_client.rpc(
                        "release_job_claim",
                        {"job_id": job_id, "worker_id": self.manager_id},
                    ).execute()
                    logger.debug(f"Released claim for job {job_id}")
                except Exception as e:
                    logger.warning(f"Failed to release claim for job {job_id}: {e}")

            self._active_jobs.clear()

    def _worker_loop(self, worker_name: str) -> None:
        """
        Main worker loop that claims and processes jobs continuously.
        Runs in a separate thread within the ThreadPoolExecutor.

        Args:
            worker_name: Unique identifier for this worker thread
        """
        logger.info(f"👀 Worker {worker_name} started")

        # Update active worker count
        with self._stats_lock:
            self._worker_stats["active_workers"] += 1

        try:
            while self._running and not self._shutdown_event.is_set():
                try:
                    # Try to claim a job atomically
                    job_data = self._claim_next_job(worker_name)

                    if job_data:
                        # Process the claimed job
                        success = self._process_claimed_job(worker_name, job_data)

                        # Update statistics
                        with self._stats_lock:
                            if success:
                                self._worker_stats["jobs_completed"] += 1
                                logger.info(
                                    f"✅ Worker {worker_name} completed job {job_data['id']}"
                                )
                            else:
                                self._worker_stats["jobs_failed"] += 1
                                logger.error(
                                    f"❌ Worker {worker_name} failed job {job_data['id']}"
                                )

                            self._worker_stats["last_activity"] = datetime.now()

                        # Add 2-second delay after job completion to prevent race conditions
                        # This allows database updates to fully commit before claiming next job
                        logger.debug(
                            f"Worker {worker_name} waiting 2s after job completion"
                        )
                        for _ in range(2):
                            if not self._running or self._shutdown_event.is_set():
                                break
                            time.sleep(1)
                    else:
                        # No jobs available, sleep before retrying
                        for _ in range(self.poll_interval):
                            if not self._running or self._shutdown_event.is_set():
                                break
                            time.sleep(1)

                except Exception as e:
                    logger.error(f"❌ Worker {worker_name} error: {e}")
                    time.sleep(5)  # Brief pause before retry

        except Exception as e:
            logger.error(f"❌ Worker {worker_name} fatal error: {e}")
        finally:
            # Update active worker count
            with self._stats_lock:
                self._worker_stats["active_workers"] -= 1
            logger.info(f"👋 Worker {worker_name} stopped")

    def _claim_next_job(self, worker_name: str) -> Optional[Dict]:
        """
        Atomically claim the next available job from the database.

        Priority order:
        1. paper_extraction (user uploads)
        2. metadata_fetch (post-processing for user uploads)
        3. peripheral_search (discovery of related papers)
        4. theme_extraction (library-wide theme generation)

        Args:
            worker_name: Unique identifier for this worker

        Returns:
            Job data if a job was claimed, None if no jobs available
        """
        try:
            # Try job types in priority order
            job_types = ["paper_extraction", "metadata_fetch", "peripheral_search", "theme_extraction"]

            for job_type in job_types:
                result = self.db_client.rpc(
                    "claim_next_job",
                    {
                        "worker_id_param": worker_name,
                        "claim_ttl_seconds": settings.JOB_CLAIM_TTL_SEC,
                        "job_type_param": job_type,
                    },
                ).execute()

                if result.data and len(result.data) > 0:
                    break

            # If no result from any job type, return None
            if not result.data or len(result.data) == 0:
                return None

            if result.data and len(result.data) > 0:
                job_data = result.data[0]
                job_id = job_data["id"]
                job_type = job_data.get("job_type", "paper_extraction")

                # Track the active job
                with self._active_jobs_lock:
                    # Get doc_id from params for tracking
                    params = job_data.get("params", {})
                    doc_id = params.get("doc_id", "unknown")

                    self._active_jobs[job_id] = {
                        "worker_name": worker_name,
                        "claimed_at": datetime.now(),
                        "doc_id": doc_id,
                        "attempts": job_data["attempts"],
                    }

                # Update statistics
                with self._stats_lock:
                    self._worker_stats["jobs_claimed"] += 1

                job_type = job_data.get("job_type", "paper_extraction")
                logger.debug(
                    f"🎯 Worker {worker_name} claimed {job_type} job {job_id} (attempt {job_data['attempts']})"
                )
                return job_data

            return None

        except Exception as e:
            logger.error(f"❌ Failed to claim job for worker {worker_name}: {e}")
            return None

    def _process_claimed_job(self, worker_name: str, job_data: Dict) -> bool:
        """
        Route claimed job to appropriate processor based on job_type.

        Args:
            worker_name: Worker identifier
            job_data: Job information from database claim

        Returns:
            True if successful, False otherwise
        """
        job_type = job_data.get("job_type", "paper_extraction")

        if job_type == "paper_extraction":
            return self._process_paper_job(worker_name, job_data)
        elif job_type == "theme_extraction":
            return self._process_theme_job(worker_name, job_data)
        elif job_type == "metadata_fetch":
            return self._process_metadata_job(worker_name, job_data)
        elif job_type == "peripheral_search":
            return self._process_peripheral_search_job(worker_name, job_data)
        else:
            logger.error(f"Unknown job type: {job_type}")
            self._update_job_status(
                job_data["id"], "failed", worker_name, f"Unknown job type: {job_type}"
            )
            return False

    def _process_paper_job(self, worker_name: str, job_data: Dict) -> bool:
        """
        Process a paper extraction job through the pipeline.

        Args:
            worker_name: Worker identifier
            job_data: Job information from database claim

        Returns:
            True if successful, False otherwise
        """
        job_id = job_data["id"]

        # For extraction_runs table: the ID IS the doc_id
        doc_id = job_id  # Simple fix - they're the same in this schema

        start_time = time.time()

        try:
            logger.info(
                f"🚀 Worker {worker_name} processing job {job_id} (doc_id {doc_id})"
            )
            logger.debug(f"   Job data: {job_data}")

            # Test manifest loading first
            pipeline = StoragePipeline(
                manifest_manager=None,
                model=self.model,
                auto_start_corenlp=False,
                corenlp_client=self.corenlp_client,
                rate_limiter=self.rate_limiter,
            )

            # DEBUG: Test manifest loading before processing
            manifest = pipeline.manifest_manager.load_job_manifest(doc_id)
            if not manifest:
                logger.error(f"CRITICAL: Cannot load manifest for doc_id {doc_id}")
                self._update_job_status(
                    job_id, "failed", worker_name, "Manifest loading failed"
                )
                return False

            logger.info(f"Successfully loaded manifest for doc_id {doc_id}")
            logger.debug(
                f"Manifest: field={manifest.field}, topic={manifest.topic}, library={manifest.library_name}"
            )

            # Process the job using our existing pipeline
            # Note: We need to run the async pipeline in a new event loop
            # since we're in a separate thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                logger.info(f"   Starting pipeline processing for doc_id: {doc_id}")

                # Process the document using the correct doc_id
                result = loop.run_until_complete(pipeline.process_document(doc_id))

                logger.info(f"   Pipeline processing completed for doc_id: {doc_id}")
                logger.debug(f"   Pipeline result: {result}")

                # Update job status to completed
                self._update_job_status(job_id, "completed", worker_name)

                # Log processing results
                duration = time.time() - start_time
                stages_completed = result["stages_completed"]
                logger.info(f"✅ Worker {worker_name} completed job {job_id}")
                logger.info(f"   Stages: {', '.join(stages_completed)}")
                logger.info(f"   Duration: {duration:.2f}s")
                logger.info(f"   Total errors: {len(result.get('errors', []))}")

                # Update statistics
                with self._stats_lock:
                    self._worker_stats["total_processing_time"] += duration

                # === POST-PROCESSING: Trigger metadata fetch + peripheral search ===
                # Only trigger for user-uploaded papers (not peripheral search papers)
                if self._should_trigger_post_processing(job_data):
                    logger.info(f"[DEV.SEARCH] 🔗 Queueing post-processing jobs for {job_id}")
                    self._queue_post_processing_jobs(job_id, manifest)

                return True

            finally:
                loop.close()

        except Exception as e:
            logger.error(f"❌ Worker {worker_name} job {job_id} failed: {e}")
            logger.error(f"   Exception type: {type(e).__name__}")
            logger.error(f"   Doc ID: {doc_id}")
            import traceback

            logger.error(f"   Full traceback: {traceback.format_exc()}")

            # Check if we've exceeded maximum retry attempts (default: 3)
            max_attempts = getattr(settings, "MAX_JOB_RETRY_ATTEMPTS", 3)
            current_attempts = job_data.get("attempts", 1)

            if current_attempts >= max_attempts:
                logger.error(
                    f"❌ Job {job_id} permanently failed after {current_attempts} attempts - STOPPING RETRIES"
                )
                # Update job status to failed (not permanently_failed since DB doesn't allow it)
                # This is fine since we kill all workers on API restart anyway
                self._update_job_status(
                    job_id,
                    "failed",
                    worker_name,
                    f"MAX RETRIES EXCEEDED: {type(e).__name__}: {str(e)}",
                )

                # Mark the extraction_run as failed (no need for permanently_failed)
                try:
                    self.db_client.table("extraction_runs").update(
                        {
                            "status": "failed",
                            "finished_at": datetime.now().isoformat(),
                            "params": {
                                "error_message": f"Job failed after {current_attempts} attempts: {str(e)}"
                            },
                        }
                    ).eq("id", job_id).execute()
                    logger.info(
                        f"🔒 Marked extraction_run {job_id} as failed (max retries reached)"
                    )
                except Exception as db_e:
                    logger.error(f"Failed to mark extraction_run as failed: {db_e}")

            else:
                logger.warning(
                    f"⚠️ Job {job_id} failed attempt {current_attempts}/{max_attempts}, will retry"
                )
                # Update job status to failed (will be retried)
                self._update_job_status(
                    job_id, "failed", worker_name, f"{type(e).__name__}: {str(e)}"
                )

            return False

        finally:
            # Remove from active jobs tracking
            with self._active_jobs_lock:
                self._active_jobs.pop(job_id, None)

    def _should_trigger_post_processing(self, job_data: Dict) -> bool:
        """
        Determine if post-processing jobs (metadata fetch + peripheral search) should be triggered.

        Only trigger for user-uploaded papers, not for papers created by peripheral search.

        Args:
            job_data: Job information from database

        Returns:
            True if post-processing should be triggered
        """
        try:
            params = job_data.get("params", {})

            # Check extraction_runs table for source
            job_id = job_data["id"]
            result = (
                self.db_client.table("extraction_runs")
                .select("paper_id")
                .eq("id", job_id)
                .execute()
            )

            if not result.data:
                return False

            paper_id = result.data[0].get("paper_id")
            if not paper_id:
                return False

            # Check library_papers for source
            lib_result = (
                self.db_client.table("library_papers")
                .select("source")
                .eq("paper_id", paper_id)
                .execute()
            )

            if not lib_result.data:
                return False

            source = lib_result.data[0].get("source", "user")

            # Only trigger for user-uploaded papers
            should_trigger = source == "user"

            if should_trigger:
                logger.info(
                    f"[DEV.SEARCH] ✓ Paper {paper_id[:8]}... is user-uploaded, will trigger post-processing"
                )
            else:
                logger.info(
                    f"[DEV.SEARCH] ⏭️  Paper {paper_id[:8]}... source is '{source}', skipping post-processing"
                )

            return should_trigger

        except Exception as e:
            logger.error(f"[DEV.SEARCH] Error checking post-processing eligibility: {e}")
            return False

    def _queue_post_processing_jobs(self, extraction_run_id: str, manifest) -> None:
        """
        Queue metadata fetch and peripheral search jobs after paper extraction completes.

        Creates a job chain:
        1. Metadata fetch job (runs once for the paper)
        2. Peripheral search job (runs once, but associates discoveries with ALL libraries containing trigger paper)

        Args:
            extraction_run_id: The completed extraction run ID
            manifest: Job manifest with paper_id
        """
        try:
            paper_id = manifest.paper_id

            if not paper_id:
                logger.warning(f"[DEV.SEARCH] No paper_id in manifest, skipping post-processing")
                return

            # Get all libraries containing this paper
            lib_result = (
                self.db_client.table("library_papers")
                .select("library_id")
                .eq("paper_id", paper_id)
                .execute()
            )

            if not lib_result.data:
                logger.warning(f"[DEV.SEARCH] Paper {paper_id[:8]}... not in any library, skipping post-processing")
                return

            library_ids = [row["library_id"] for row in lib_result.data]
            logger.info(f"[DEV.SEARCH] 📋 Paper {paper_id[:8]}... is in {len(library_ids)} library(ies)")

            # Create ONE metadata fetch job (metadata is paper-level, not library-specific)
            logger.info(f"[DEV.SEARCH] 📋 Creating metadata fetch job for paper {paper_id[:8]}...")
            metadata_job_id = str(uuid.uuid4())
            metadata_job_data = {
                "id": metadata_job_id,
                "paper_id": paper_id,
                "library_id": None,  # Metadata is not library-specific
                "user_id": manifest.user_id,
                "job_type": "metadata_fetch",
                "status": "queued",
                "params": {
                    "paper_id": paper_id,
                    "source_extraction_run": extraction_run_id,
                },
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
            }

            result = self.db_client.table("extraction_runs").insert(metadata_job_data).execute()

            if result.data:
                logger.info(f"[DEV.SEARCH] ✅ Queued metadata fetch job: {metadata_job_id[:8]}...")
            else:
                logger.error(f"[DEV.SEARCH] ❌ Failed to queue metadata fetch job")
                return

            # Create ONE peripheral search job that will add discovered papers to ALL libraries
            peripheral_job_id = str(uuid.uuid4())
            peripheral_job_data = {
                "id": peripheral_job_id,
                "paper_id": paper_id,
                "library_id": None,  # Will associate with multiple libraries
                "user_id": manifest.user_id,
                "job_type": "peripheral_search",
                "status": "queued",
                "params": {
                    "paper_id": paper_id,
                    "library_ids": library_ids,  # Pass ALL library IDs
                    "source_extraction_run": extraction_run_id,
                    "source_metadata_job": metadata_job_id,
                },
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
            }

            result = self.db_client.table("extraction_runs").insert(peripheral_job_data).execute()

            if result.data:
                logger.info(f"[DEV.SEARCH] ✅ Queued peripheral search job (will add to {len(library_ids)} libraries): {peripheral_job_id[:8]}...")
            else:
                logger.error(f"[DEV.SEARCH] ❌ Failed to queue peripheral search job")

        except Exception as e:
            logger.error(f"[DEV.SEARCH] ❌ Error queueing post-processing jobs: {e}")
            import traceback
            traceback.print_exc()

    def _process_theme_job(self, worker_name: str, job_data: Dict) -> bool:
        """
        Process a theme extraction job.

        Args:
            worker_name: Worker identifier
            job_data: Job information from database claim

        Returns:
            True if successful, False otherwise
        """
        job_id = job_data["id"]
        library_id = job_data.get("library_id")
        params = job_data.get("params", {})

        if not library_id:
            logger.error(f"Theme job {job_id} missing library_id")
            self._update_job_status(job_id, "failed", worker_name, "Missing library_id")
            return False

        start_time = time.time()

        try:
            logger.info(
                f"🎨 Worker {worker_name} processing theme extraction for library {library_id}"
            )
            if params.get("force_full_extraction"):
                logger.info(f"   Force flag ENABLED - will do full regeneration")

            # Import theme service
            from app.services.themes import extract_library_themes

            # Run theme extraction in event loop (since it's async)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            try:
                result = loop.run_until_complete(
                    extract_library_themes(library_id, job_params=params)
                )

                logger.info(f"Theme extraction result: {result}")

                # Update job status to completed
                self._update_job_status(job_id, "completed", worker_name)

                # Log processing results
                duration = time.time() - start_time
                logger.info(f"✅ Worker {worker_name} completed theme job {job_id}")
                logger.info(f"   Library: {library_id}")
                logger.info(f"   Themes: {result.get('themes_count', 0)}")
                logger.info(f"   Version: {result.get('version', 'N/A')}")
                logger.info(f"   Duration: {duration:.2f}s")

                # Update statistics
                with self._stats_lock:
                    self._worker_stats["total_processing_time"] += duration

                return True

            finally:
                loop.close()

        except Exception as e:
            logger.error(f"❌ Worker {worker_name} theme job {job_id} failed: {e}")
            logger.error(f"   Exception type: {type(e).__name__}")
            logger.error(f"   Library ID: {library_id}")
            import traceback

            logger.error(f"   Full traceback: {traceback.format_exc()}")

            # Check if we've exceeded maximum retry attempts
            max_attempts = getattr(settings, "MAX_JOB_RETRY_ATTEMPTS", 3)
            current_attempts = job_data.get("attempts", 1)

            if current_attempts >= max_attempts:
                logger.error(
                    f"❌ Theme job {job_id} permanently failed after {current_attempts} attempts - STOPPING RETRIES"
                )
                self._update_job_status(
                    job_id,
                    "failed",
                    worker_name,
                    f"MAX RETRIES EXCEEDED: {type(e).__name__}: {str(e)}",
                )

                # Mark the extraction_run as failed
                try:
                    self.db_client.table("extraction_runs").update(
                        {
                            "status": "failed",
                            "finished_at": datetime.now().isoformat(),
                            "params": {
                                "error_message": f"Job failed after {current_attempts} attempts: {str(e)}"
                            },
                        }
                    ).eq("id", job_id).execute()
                    logger.info(
                        f"🔒 Marked extraction_run {job_id} as failed (max retries reached)"
                    )
                except Exception as db_e:
                    logger.error(f"Failed to mark extraction_run as failed: {db_e}")

            else:
                logger.warning(
                    f"⚠️ Theme job {job_id} failed attempt {current_attempts}/{max_attempts}, will retry"
                )
                self._update_job_status(
                    job_id, "failed", worker_name, f"{type(e).__name__}: {str(e)}"
                )

            return False

        finally:
            # Remove from active jobs tracking
            with self._active_jobs_lock:
                self._active_jobs.pop(job_id, None)

    def _process_metadata_job(self, worker_name: str, job_data: Dict) -> bool:
        """
        Process a metadata fetch job.

        Args:
            worker_name: Worker identifier
            job_data: Job information from database claim

        Returns:
            True if successful, False otherwise
        """
        job_id = job_data["id"]
        params = job_data.get("params", {})

        start_time = time.time()

        try:
            logger.info(f"[DEV.SEARCH] 🔍 Worker {worker_name} processing metadata fetch job {job_id}")

            # Import and call metadata service
            from app.services.search.metadata_service import process_metadata_job

            result = process_metadata_job(params)

            duration = time.time() - start_time

            if result.get("success"):
                self._update_job_status(job_id, "completed", worker_name)
                logger.info(f"[DEV.SEARCH] ✅ Worker {worker_name} completed metadata job {job_id}")
                logger.info(f"[DEV.SEARCH]    Duration: {duration:.2f}s")

                # Update statistics
                with self._stats_lock:
                    self._worker_stats["total_processing_time"] += duration

                return True
            else:
                error_msg = result.get("error", "Unknown error")
                self._update_job_status(job_id, "failed", worker_name, error_msg)
                logger.error(f"[DEV.SEARCH] ❌ Metadata job failed: {error_msg}")
                return False

        except Exception as e:
            logger.error(f"[DEV.SEARCH] ❌ Worker {worker_name} metadata job {job_id} failed: {e}")
            import traceback
            traceback.print_exc()

            self._update_job_status(job_id, "failed", worker_name, str(e))
            return False

        finally:
            with self._active_jobs_lock:
                self._active_jobs.pop(job_id, None)

    def _process_peripheral_search_job(self, worker_name: str, job_data: Dict) -> bool:
        """
        Process a peripheral search job.

        Args:
            worker_name: Worker identifier
            job_data: Job information from database claim

        Returns:
            True if successful, False otherwise
        """
        job_id = job_data["id"]
        params = job_data.get("params", {})

        start_time = time.time()

        try:
            logger.info(f"[DEV.SEARCH] 🔍 Worker {worker_name} processing peripheral search job {job_id}")

            # Import and call peripheral search service
            from app.services.search.peripheral_search_service import process_peripheral_search_job

            result = process_peripheral_search_job(params)

            duration = time.time() - start_time

            if result.get("success"):
                self._update_job_status(job_id, "completed", worker_name)
                logger.info(f"[DEV.SEARCH] ✅ Worker {worker_name} completed peripheral search job {job_id}")
                logger.info(f"[DEV.SEARCH]    Discovered: {result.get('discovered', 0)}")
                logger.info(f"[DEV.SEARCH]    Downloaded: {result.get('downloaded', 0)}")
                logger.info(f"[DEV.SEARCH]    Uploaded: {result.get('uploaded', 0)}")
                logger.info(f"[DEV.SEARCH]    Skipped (existing): {result.get('skipped_existing', 0)}")
                logger.info(f"[DEV.SEARCH]    Duration: {duration:.2f}s")

                # Update statistics
                with self._stats_lock:
                    self._worker_stats["total_processing_time"] += duration

                return True
            else:
                error_msg = result.get("error", "Unknown error")
                self._update_job_status(job_id, "failed", worker_name, error_msg)
                logger.error(f"[DEV.SEARCH] ❌ Peripheral search job failed: {error_msg}")
                return False

        except Exception as e:
            logger.error(f"[DEV.SEARCH] ❌ Worker {worker_name} peripheral search job {job_id} failed: {e}")
            import traceback
            traceback.print_exc()

            self._update_job_status(job_id, "failed", worker_name, str(e))
            return False

        finally:
            with self._active_jobs_lock:
                self._active_jobs.pop(job_id, None)

    def _update_job_status(
        self, job_id: str, status: str, worker_name: str, error_message: str = None
    ) -> None:
        """
        Update job status in database and release claim.

        Args:
            job_id: Job identifier
            status: New status ('completed' or 'failed')
            worker_name: Worker that processed the job
            error_message: Error details if status is 'failed'
        """
        try:

            # Update the job status in extraction_runs table
            update_data = {"status": status, "finished_at": datetime.now().isoformat()}

            if error_message:
                # Store error in params JSON field, preserving existing params
                # Fetch current params from database to avoid losing job data
                try:
                    current_job = (
                        self.db_client.table("extraction_runs")
                        .select("params")
                        .eq("id", job_id)
                        .execute()
                    )
                    existing_params = current_job.data[0].get("params", {}) if current_job.data else {}
                except Exception:
                    existing_params = {}

                params = {**existing_params, "error_message": error_message}
                update_data["params"] = params

            update_result = (
                self.db_client.table("extraction_runs")
                .update(update_data)
                .eq("id", job_id)
                .execute()
            )

            if len(update_result.data) == 0:
                logger.warning(
                    f"[DEBUG] ⚠️ UPDATE matched 0 rows for job {job_id} - job may not exist or already updated"
                )

            # Release the job claim
            release_result = self.db_client.rpc(
                "release_job_claim",
                {"job_id_param": job_id, "worker_id_param": worker_name},
            ).execute()

            logger.debug(f"Updated job {job_id} status to {status}")

        except Exception as e:
            logger.error(f"Failed to update job {job_id} status: {e}")

    @property
    def is_running(self) -> bool:
        """Check if workers are currently running."""
        return self._running

    def get_status(self) -> dict:
        """
        Get current parallel worker manager status.

        Returns:
            Dict with comprehensive worker status information
        """
        with self._stats_lock:
            stats = self._worker_stats.copy()

        with self._active_jobs_lock:
            active_job_count = len(self._active_jobs)
            active_jobs_info = [
                {
                    "job_id": job_id,
                    "worker_name": info["worker_name"],
                    "claimed_at": (
                        info["claimed_at"].isoformat() if info["claimed_at"] else None
                    ),
                    "attempts": info["attempts"],
                }
                for job_id, info in self._active_jobs.items()
            ]

        # Get resource status
        corenlp_status = self.corenlp_client.get_status() if self.corenlp_client else {}
        rate_limiter_status = (
            self.rate_limiter.get_status() if self.rate_limiter else {}
        )

        return {
            "running": self._running,
            "manager_id": self.manager_id,
            "model": self.model,
            "worker_count": self.worker_count,
            "poll_interval": self.poll_interval,
            # Worker statistics
            "active_workers": stats["active_workers"],
            "jobs_claimed": stats["jobs_claimed"],
            "jobs_completed": stats["jobs_completed"],
            "jobs_failed": stats["jobs_failed"],
            "total_processing_time": stats["total_processing_time"],
            "last_activity": (
                stats["last_activity"].isoformat() if stats["last_activity"] else None
            ),
            # Current activity
            "active_jobs": active_job_count,
            "active_jobs_detail": active_jobs_info,
            # Resource pool status
            "corenlp": corenlp_status,
            "rate_limiter": rate_limiter_status,
            # Health indicators
            "healthy": self._running and stats["active_workers"] > 0,
            "avg_processing_time": (
                stats["total_processing_time"] / stats["jobs_completed"]
                if stats["jobs_completed"] > 0
                else 0
            ),
        }


# Backward compatibility alias
WorkerManager = ParallelWorkerManager

# Global worker manager instance
_worker_manager: Optional[ParallelWorkerManager] = None
_manager_lock = threading.Lock()


def get_worker_manager() -> ParallelWorkerManager:
    """
    Get the global parallel worker manager instance.
    Thread-safe singleton pattern.
    """
    global _worker_manager

    if _worker_manager is None:
        with _manager_lock:
            # Double-check locking pattern
            if _worker_manager is None:
                _worker_manager = ParallelWorkerManager()

    return _worker_manager


def close_worker_manager() -> None:
    """Close and clean up the global worker manager."""
    global _worker_manager

    if _worker_manager is not None:
        with _manager_lock:
            if _worker_manager is not None:
                # Note: This would need to be called from an async context
                # For now, we'll let the FastAPI lifespan handle shutdown
                _worker_manager = None
