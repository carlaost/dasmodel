# Grounding: transcribed from oshima/api/app/db/supabase_client.py
# app/db/supabase_client.py
"""
Supabase client factories:
- user_client(jwt): per-request client bound to the caller's Supabase JWT (RLS enforced)
- service_client(): long-lived client using the service role key (bypasses RLS)
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional

from supabase import Client, create_client

# ---- Env helpers -------------------------------------------------------------


def _getenv(name: str, required: bool = True) -> Optional[str]:
    val = os.getenv(name)
    if required and not val:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val


# Required envs
_SUPABASE_URL = _getenv("SUPABASE_URL")
_SUPABASE_ANON_KEY = _getenv("SUPABASE_ANON_KEY")
# Service key is optional at runtime for user-only paths
_SUPABASE_SERVICE_ROLE_KEY = _getenv("SUPABASE_SERVICE_ROLE_KEY", required=False)


# ---- Client factories --------------------------------------------------------


def user_client(jwt: str) -> Client:
    """
    Returns a NEW Supabase client bound to the given user JWT.
    Safe for per-request use. RLS applies to all CRUD.
    """
    if not jwt:
        raise ValueError("user_client(jwt) requires a non-empty JWT")
    # Create a fresh anon client, then bind the user's access token.
    client = create_client(_SUPABASE_URL, _SUPABASE_ANON_KEY)
    # supabase-py v2: set_session sets the JWT for PostgREST/Storage calls
    client.auth.set_session(access_token=jwt, refresh_token="")
    return client


@lru_cache(maxsize=1)
def service_client() -> Client:
    """
    Returns a cached Supabase client using the service role key.
    Do NOT use from user-facing endpoints. Intended for background jobs/cron.
    """
    if not _SUPABASE_SERVICE_ROLE_KEY:
        raise RuntimeError(
            "SUPABASE_SERVICE_ROLE_KEY not set; service_client() cannot be created."
        )
    return create_client(_SUPABASE_URL, _SUPABASE_SERVICE_ROLE_KEY)


# Optional: anon client if you ever need public, unauthenticated reads
@lru_cache(maxsize=1)
def anon_client() -> Client:
    return create_client(_SUPABASE_URL, _SUPABASE_ANON_KEY)
