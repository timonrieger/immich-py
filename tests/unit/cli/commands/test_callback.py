from pathlib import Path
from unittest.mock import MagicMock

from typer.testing import CliRunner

from immich.cli import main


class TestCallbackConfigResolution:
    def test_cli_options_take_precedence_over_profile(
        self, runner: CliRunner, mock_config_path: Path, mock_api_calls: MagicMock
    ):
        """Test that CLI options take precedence over profile values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner.invoke(
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
        mock_api_calls.assert_called_once()
        call_kwargs = mock_api_calls.call_args.kwargs
        assert call_kwargs["base_url"] == "https://cli.immich.app/api"
        assert call_kwargs["api_key"] == "cli-key"
        assert call_kwargs["bearer_token"] == "cli-token"

    def test_profile_values_used_when_cli_options_missing(
        self, runner: CliRunner, mock_config_path: Path, mock_api_calls: MagicMock
    ):
        """Test that profile values are used when CLI options are not provided."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner.invoke(
            main.app,
            ["server", "get-about-info"],
        )

        assert result.exit_code == 0
        mock_api_calls.assert_called_once()
        call_kwargs = mock_api_calls.call_args.kwargs
        assert call_kwargs["base_url"] == "https://profile.immich.app/api"
        assert call_kwargs["api_key"] == "profile-key"
        assert call_kwargs["bearer_token"] == "profile-token"

    def test_partial_cli_options_merge_with_profile(
        self, runner: CliRunner, mock_config_path: Path, mock_api_calls: MagicMock
    ):
        """Test that partial CLI options merge with profile values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            "[profiles.default]\n"
            'base_url = "https://profile.immich.app/api"\n'
            'api_key = "profile-key"\n'
            'access_token = "profile-token"'
        )

        result = runner.invoke(
            main.app,
            [
                "--base-url",
                "https://cli.immich.app/api",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        mock_api_calls.assert_called_once()
        call_kwargs = mock_api_calls.call_args.kwargs
        assert call_kwargs["base_url"] == "https://cli.immich.app/api"
        assert call_kwargs["api_key"] == "profile-key"
        assert call_kwargs["bearer_token"] == "profile-token"

    def test_custom_profile_resolution(
        self, runner: CliRunner, mock_config_path: Path, mock_api_calls: MagicMock
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

        result = runner.invoke(
            main.app,
            [
                "--profile",
                "production",
                "server",
                "get-about-info",
            ],
        )

        assert result.exit_code == 0
        mock_api_calls.assert_called_once()
        call_kwargs = mock_api_calls.call_args.kwargs
        assert call_kwargs["base_url"] == "https://prod.immich.app/api"
        assert call_kwargs["api_key"] == "prod-key"
        assert call_kwargs["bearer_token"] is None
