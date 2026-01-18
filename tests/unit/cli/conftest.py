from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from typer.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    """Typer CliRunner fixture for CLI testing."""
    return CliRunner()


@pytest.fixture
def mock_config_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Fixture that patches CONFIG_DIR and CONFIG_FILE to use tmp_path."""
    config_dir = tmp_path / ".immich-py"
    config_file = config_dir / "config.toml"

    monkeypatch.setattr("immich._internal.consts.CONFIG_DIR", config_dir)
    monkeypatch.setattr("immich._internal.consts.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich._internal.cli.utils.CONFIG_DIR", config_dir)
    monkeypatch.setattr("immich._internal.cli.utils.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich.cli_wrapper.commands.setup.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich.cli_wrapper.commands.config.CONFIG_FILE", config_file)

    return config_file


@pytest.fixture
def mock_api_calls():
    """Fixture that intercepts API calls by mocking AsyncClient and run_command."""

    def mock_run_command(*args, **kwargs):
        return {}

    with (
        patch("immich.cli.main.AsyncClient") as mock_client,
        patch("immich.cli.runtime.run_command", side_effect=mock_run_command),
    ):
        mock_client_instance = MagicMock()
        mock_client_instance.server = MagicMock()
        mock_client_instance.server.get_about_info = AsyncMock(return_value={})
        mock_client_instance.close = AsyncMock(return_value=None)
        mock_client.return_value = mock_client_instance
        yield mock_client
