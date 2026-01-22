from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from typer.testing import CliRunner

from immich.cli import main


@pytest.fixture
def mock_server_api():
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


class TestCallbackConfigResolution:
    def test_cli_options_take_precedence_over_profile(
        self,
        runner_without_auth: CliRunner,
        mock_config_path: Path,
        mock_server_api: MagicMock,
    ):
        """Test that CLI options take precedence over profile values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner_without_auth.invoke(
            main.app,
            [
                "--base-url",
                "https://cli.immich.app/api",
                "--api-key",
                "cli-key",
                "--access-token",
                "cli-token",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        mock_server_api.assert_called_once()
        call_kwargs = mock_server_api.call_args.kwargs
        assert call_kwargs["base_url"] == "https://cli.immich.app/api"
        assert call_kwargs["api_key"] == "cli-key"
        # Access token is omitted because API key is provided
        assert call_kwargs["access_token"] is None

    def test_profile_values_used_when_cli_options_missing(
        self,
        runner_without_auth: CliRunner,
        mock_config_path: Path,
        mock_server_api: MagicMock,
    ):
        """Test that profile values are used when CLI options are not provided."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner_without_auth.invoke(
            main.app,
            ["server", "get-about-info"],
        )

        assert result.exit_code == 0, result.output
        mock_server_api.assert_called_once()
        call_kwargs = mock_server_api.call_args.kwargs
        assert call_kwargs["base_url"] == "https://profile.immich.app/api"
        assert call_kwargs["api_key"] == "profile-key"
        # Access token is omitted because API key is provided
        assert call_kwargs["access_token"] is None

    def test_partial_cli_options_merge_with_profile(
        self,
        runner_without_auth: CliRunner,
        mock_config_path: Path,
        mock_server_api: MagicMock,
    ):
        """Test that partial CLI options merge with profile values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner_without_auth.invoke(
            main.app,
            [
                "--base-url",
                "https://cli.immich.app/api",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        mock_server_api.assert_called_once()
        call_kwargs = mock_server_api.call_args.kwargs
        assert call_kwargs["base_url"] == "https://cli.immich.app/api"
        assert call_kwargs["api_key"] == "profile-key"
        # Access token is omitted because API key is provided
        assert call_kwargs["access_token"] is None

    def test_custom_profile_resolution(
        self,
        runner_without_auth: CliRunner,
        mock_config_path: Path,
        mock_server_api: MagicMock,
    ):
        """Test that custom profile is used when specified."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.production]\n"
            'base_url = "https://prod.immich.app/api"\n'
            'api_key = "prod-key"\n'
            "[profiles.default]\n"
            'base_url = "https://default.immich.app/api"\n'
            'api_key = "default-key"\n'
            'access_token = "default-token"'
        )

        result = runner_without_auth.invoke(
            main.app,
            [
                "--profile",
                "production",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        mock_server_api.assert_called_once()
        call_kwargs = mock_server_api.call_args.kwargs
        assert call_kwargs["base_url"] == "https://prod.immich.app/api"
        assert call_kwargs["api_key"] == "prod-key"
        # Access token is omitted because it is not set in the profile
        assert call_kwargs["access_token"] is None

    def test_no_base_url_exits_with_error(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ) -> None:
        """Test that missing base_url exits with error code 1."""
        # Create config file without base_url
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('[profiles.default]\napi_key = "profile-key"\n')

        result = runner_without_auth.invoke(
            main.app,
            ["server", "get-about-info"],
        )

        assert result.exit_code == 1
        assert "No base URL provided" in result.output
        assert "immich setup" in result.output

    @patch("immich.cli.main.print_")
    def test_verbose_mode_prints_debug_config(
        self,
        mock_print: MagicMock,
        runner_without_auth: CliRunner,
        mock_config_path: Path,
        mock_server_api: MagicMock,
    ) -> None:
        """Test that verbose mode prints debug configuration messages."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
        )

        result = runner_without_auth.invoke(
            main.app,
            [
                "--verbose",
                "--base-url",
                "https://cli.immich.app/api",
                "--api-key",
                "cli-key",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        # Verify print_ was called with "Configuration used:" debug message
        debug_calls = [
            call
            for call in mock_print.call_args_list
            if call.kwargs.get("type") == "debug"
        ]
        assert len(debug_calls) > 0
        assert any("Configuration used:" in str(call.args[0]) for call in debug_calls)
        # Verify that configuration fields are printed
        assert any("base_url" in str(call.args[0]) for call in debug_calls)
