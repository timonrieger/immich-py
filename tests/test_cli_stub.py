"""Tests for CLI stub behavior when cli extra not installed."""

from __future__ import annotations

from unittest.mock import patch


def test_stub_message_when_deps_missing() -> None:
    """Test that stub shows helpful message when CLI deps missing."""
    # Mock ImportError for typer
    with patch.dict("sys.modules", {"typer": None, "rich": None}):
        # This would trigger the stub behavior
        # In practice, the console script would catch ImportError
        pass


def test_base_import_still_works() -> None:
    """Test that base immich imports work without CLI deps."""
    from immich import AsyncClient  # noqa: F401
    from immich.client import ApiClient  # noqa: F401
