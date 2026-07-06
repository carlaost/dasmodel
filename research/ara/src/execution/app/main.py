# Grounding: transcribed from oshima/api/app/main.py
"""Main FastAPI application."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app import __description__, __version__, __release_notes__
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logging import get_logger, setup_logging
from app.middlewares.logging_middleware import RequestLoggingMiddleware
from app.workers.worker_manager import get_worker_manager

# Set up logging
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan events."""
    # Startup
    logger.info("Starting Oshima API", version=__version__)

    # Configure DSPy once at application startup (before workers start)
    import os
    use_dspy = os.getenv("USE_DSPY_EXTRACTION", "false").lower() == "true"
    if use_dspy:
        import dspy
        dspy.settings.configure(
            lm=dspy.LM(
                'anthropic/claude-sonnet-4-5-20250929',
                max_tokens=64000,  # Sonnet 4.5 max output tokens
                timeout=600  # 10 minute timeout for API calls
            ),
            adapter=dspy.JSONAdapter()
        )
        logger.info("DSPy configured globally with Claude Sonnet 4.5 (max_tokens=64000)")

    # Start the background job processing worker
    worker_manager = get_worker_manager()
    await worker_manager.start_worker()

    # Start the theme extraction monitor
    from app.services.themes import start_theme_monitor
    await start_theme_monitor()

    yield

    # Shutdown
    logger.info("Shutting down Oshima API")

    # Stop the theme extraction monitor
    from app.services.themes import stop_theme_monitor
    await stop_theme_monitor()

    # Stop the background job processing worker
    await worker_manager.stop_worker()


def create_application() -> FastAPI:
    """Create FastAPI application with all configurations."""

    # Combine description with release notes for API docs
    full_description = f"{__description__}\n\n{__release_notes__}"

    app = FastAPI(
        title=settings.APP_NAME,
        description=full_description,
        version=__version__,
        openapi_url="/api/v1/openapi.json" if settings.DEBUG else None,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        lifespan=lifespan,
    )

    # Add security middleware
    if not settings.DEBUG:
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["localhost", "127.0.0.1", "*.oshimascience.com"],
        )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    # Add request logging middleware
    app.add_middleware(RequestLoggingMiddleware)

    # Include API routers
    app.include_router(api_router, prefix="/api/v1")

    # Root endpoint
    @app.get("/", response_class=JSONResponse)
    async def root():
        """Root endpoint with API information."""
        return {
            "message": "Welcome to Oshima API",
            "version": __version__,
            "description": __description__,
            "docs_url": "/docs" if settings.DEBUG else None,
            "redoc_url": "/redoc" if settings.DEBUG else None,
        }

    # Health check endpoint
    @app.get("/health", response_class=JSONResponse)
    async def health_check():
        """Health check endpoint."""
        worker_manager = get_worker_manager()
        worker_status = worker_manager.get_status()

        return {
            "status": "healthy",
            "version": __version__,
            "environment": settings.ENVIRONMENT,
            "worker": worker_status,
        }

    return app


# Create the FastAPI app
app = create_application()


def main() -> None:
    """Run the application."""
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL.lower(),
    )


if __name__ == "__main__":
    main()
