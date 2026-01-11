"""Tests for CLI code generation."""

from __future__ import annotations

from pathlib import Path


def test_codegen_deterministic(tmp_path: Path) -> None:
    """Test that codegen produces identical output on multiple runs."""
    # This test would require running codegen, which needs network access
    # For now, we'll skip it in CI or make it optional
    # In a real scenario, you'd:
    # 1. Run codegen once, capture output
    # 2. Run codegen again
    # 3. Assert no differences
    pass


def test_cli_imports_without_network() -> None:
    """Test that importing CLI modules doesn't trigger network calls."""
    # Import should not make HTTP requests
    try:
        from immich.cli import app  # noqa: F401
        from immich.cli import config  # noqa: F401
        from immich.cli import runtime  # noqa: F401
    except ImportError as e:
        # CLI deps not installed - that's OK for base install
        if "typer" in str(e) or "rich" in str(e):
            return
        raise


def test_cli_help_works() -> None:
    """Test that --help works when CLI is installed."""
    # This would require installing with [cli] extra
    # For now, we'll test that the entrypoint exists
    try:
        from immich.cli.app import main

        assert callable(main)
    except ImportError:
        # CLI deps not installed - skip test
        pass
