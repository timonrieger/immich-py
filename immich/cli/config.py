"""Configuration and client setup for CLI."""

from __future__ import annotations

import os
from typing import Optional

from immich import AsyncClient


def get_base_url() -> str:
    """Get base URL from environment or config."""
    base_url = os.environ.get("IMMICH_BASE_URL")
    if not base_url:
        raise ValueError(
            "IMMICH_BASE_URL environment variable is required. "
            "Set it to your Immich server URL (e.g., http://localhost:2283/api)"
        )
    return base_url


def get_auth() -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Get auth credentials from environment.

    :return: Tuple of (api_key, bearer_token, cookie)
    """
    api_key = os.environ.get("IMMICH_API_KEY")
    bearer_token = os.environ.get("IMMICH_BEARER_TOKEN")
    cookie = os.environ.get("IMMICH_COOKIE")

    if not any([api_key, bearer_token, cookie]):
        raise ValueError(
            "At least one auth method required. Set one of: "
            "IMMICH_API_KEY, IMMICH_BEARER_TOKEN, or IMMICH_COOKIE"
        )

    return api_key, bearer_token, cookie


def create_client() -> AsyncClient:
    """Create and return a configured AsyncClient."""
    base_url = get_base_url()
    api_key, bearer_token, cookie = get_auth()

    return AsyncClient(
        api_key=api_key,
        bearer_token=bearer_token,
        cookie=cookie,
        base_url=base_url,
    )
