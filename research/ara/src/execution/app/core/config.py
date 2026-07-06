# Grounding: transcribed from oshima/api/app/core/config.py
"""Application configuration settings."""

import os
import secrets
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    # App Configuration
    APP_NAME: str = "Oshima API"
    APP_VERSION: str = "0.1.1"
    APP_DESCRIPTION: str = "FastAPI backend for Oshima ecosystem"
    DEBUG: bool = True  # Enable auto docs for development
    ENVIRONMENT: str = "development"

    # Server Configuration
    HOST: str = "127.0.0.1"
    PORT: int = 8000  # Changed from 8000 to avoid conflicts
    RELOAD: bool = False

    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:4321",
        "https://www.oshimascience.com",
        "https://api.oshimascience.com",
        "https://oshimascience.com",
    ]
    ALLOWED_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
    ALLOWED_HEADERS: List[str] = ["*"]

    # Database Configuration
    DATABASE_URL: Optional[str] = None

    # Redis Configuration
    REDIS_URL: Optional[str] = None
    REDIS_DB: int = 0

    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # File Upload
    MAX_FILE_SIZE: int = 41943040  # 40MB
    UPLOAD_PATH: str = "./uploads"

    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60

    # Adobe PDF Services
    PDF_SERVICES_CLIENT_ID: Optional[str] = None
    PDF_SERVICES_CLIENT_SECRET: Optional[str] = None
    PDF_SERVICES_ORGANIZATION_ID: Optional[str] = None
    
    # Ingestion Provider Configuration
    INGEST_PROVIDER: str = "adobe"  # Options: "adobe" or "azure"
    
    # Azure Document Intelligence
    AZURE_DOCINTEL_ENDPOINT: Optional[str] = None
    AZURE_DOCINTEL_KEY: Optional[str] = None

    # OpenAI
    OPENAI_API_KEY: Optional[str] = None

    # Supabase Configuration
    SUPABASE_PROJECT_ID: Optional[str] = None
    SUPABASE_URL: Optional[str] = None
    SUPABASE_ANON_KEY: Optional[str] = None
    SUPABASE_SERVICE_ROLE: Optional[str] = None
    SUPABASE_SERVICE_ROLE_KEY: Optional[str] = None

    # Parallel Processing Configuration
    WORKER_ENABLED: bool = True
    WORKER_COUNT: int = 4  # Number of worker threads per process

    # LLM Rate Limiting
    LLM_RPS: float = 1.0  # Requests per second to OpenAI API

    # CoreNLP Configuration
    CORENLP_URLS: str = "http://localhost:9000"  # Comma-separated URLs
    CORENLP_MAX_CONCURRENCY: int = 3  # Max concurrent CoreNLP requests

    # Job Management
    JOB_CLAIM_TTL_SEC: int = 600  # Job claim timeout in seconds (10 minutes)
    JOB_POLL_SEC: int = 5  # Polling interval when queue is empty
    MAX_JOB_RETRY_ATTEMPTS: int = 3  # Maximum retry attempts for failed jobs

    @field_validator("INGEST_PROVIDER")
    @classmethod
    def validate_ingest_provider(cls, v: str) -> str:
        """Validate ingestion provider setting."""
        valid_providers = ["adobe", "azure"]
        if v.lower() not in valid_providers:
            raise ValueError(f"INGEST_PROVIDER must be one of {valid_providers}, got: {v}")
        return v.lower()
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """Parse CORS origins."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @field_validator("ALLOWED_METHODS", mode="before")
    @classmethod
    def assemble_cors_methods(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """Parse CORS methods."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @field_validator("CORENLP_URLS", mode="before")
    @classmethod
    def parse_corenlp_urls(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """Parse CoreNLP URLs from comma-separated string."""
        if isinstance(v, str) and "," in v:
            return [url.strip() for url in v.split(",") if url.strip()]
        return v

    def get_corenlp_urls(self) -> List[str]:
        """Get CoreNLP URLs as a list."""
        if isinstance(self.CORENLP_URLS, list):
            return self.CORENLP_URLS
        return [self.CORENLP_URLS]

    model_config = {
        "case_sensitive": True,
        "env_file": ".env",
        "extra": "ignore",
    }


# Global settings instance
settings = Settings()


# Helper functions for backwards compatibility
def get_supabase_url() -> str:
    """Get Supabase URL from environment"""
    if not settings.SUPABASE_URL:
        raise ValueError("SUPABASE_URL environment variable not set")
    return settings.SUPABASE_URL


def get_supabase_anon_key() -> str:
    """Get Supabase anonymous key from environment"""
    if not settings.SUPABASE_ANON_KEY:
        raise ValueError("SUPABASE_ANON_KEY environment variable not set")
    return settings.SUPABASE_ANON_KEY


def get_supabase_service_role() -> Optional[str]:
    """Get Supabase service role key from environment (optional)"""
    return settings.SUPABASE_SERVICE_ROLE
