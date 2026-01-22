from pathlib import Path
from unittest.mock import patch

import rtoml
from typer.testing import CliRunner

from immich.cli.main import app


class TestSetup:
    def test_setup_with_all_parameters(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setup command with all parameters provided."""
        result = runner_without_auth.invoke(
            app,
            [
                "setup",
                "--base-url",
                "https://demo.immich.app/api",
                "--api-key",
                "test-api-key",
                "--access-token",
                "test-access-token",
            ],
        )

        if result.exit_code != 5:  # 5 handles downtimes of the server
            assert result.exit_code == 0
            assert mock_config_path.exists()
            config_data = rtoml.load(mock_config_path)
            assert (
                config_data["profiles"]["default"]["base_url"]
                == "https://demo.immich.app/api"
            )
            assert config_data["profiles"]["default"]["api_key"] == "test-api-key"
            assert (
                config_data["profiles"]["default"]["access_token"]
                == "test-access-token"
            )
            assert "Success" in result.stdout
            assert "default" in result.stdout

    def test_setup_with_custom_profile(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setup command with custom profile."""
        result = runner_without_auth.invoke(
            app,
            [
                "setup",
                "--profile",
                "production",
                "--base-url",
                "https://prod.immich.app/api",
                "--api-key",
                "prod-key",
                "--access-token",
                "",
                "--skip-validation",
            ],
        )

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["production"]["base_url"]
            == "https://prod.immich.app/api"
        )
        assert config_data["profiles"]["production"]["api_key"] == "prod-key"
        assert config_data["profiles"]["production"]["access_token"] == ""
        assert "Success" in result.stdout
        assert "production" in result.stdout

    def test_setup_with_only_base_url(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setup command with only base_url (empty api_key and access_token)."""
        result = runner_without_auth.invoke(
            app,
            [
                "setup",
                "--base-url",
                "https://demo.immich.app/api",
                "--api-key",
                "",
                "--access-token",
                "",
            ],
        )

        if result.exit_code != 5:  # 5 handles downtimes of the server
            assert result.exit_code == 0
            config_data = rtoml.load(mock_config_path)
            assert (
                config_data["profiles"]["default"]["base_url"]
                == "https://demo.immich.app/api"
            )
            assert config_data["profiles"]["default"]["api_key"] == ""
            assert config_data["profiles"]["default"]["access_token"] == ""

    def test_setup_overwrites_existing_profile(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that setup overwrites an existing profile."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\nbase_url = "old-url"\napi_key = "old-key"'
        )

        result = runner_without_auth.invoke(
            app,
            [
                "setup",
                "--base-url",
                "https://new.immich.app/api",
                "--api-key",
                "new-key",
                "--access-token",
                "",
                "--skip-validation",
            ],
        )

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["default"]["base_url"]
            == "https://new.immich.app/api"
        )
        assert config_data["profiles"]["default"]["api_key"] == "new-key"

    @patch("immich.cli.wrapper.setup.run_command")
    def test_setup_ping_server_validation_fails(
        self, mock_run_command, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setup command when ping server validation fails."""
        # Mock run_command to raise an exception simulating a failed ping
        mock_run_command.side_effect = Exception("Connection refused")

        result = runner_without_auth.invoke(
            app,
            [
                "setup",
                "--base-url",
                "https://invalid.immich.app/api",
                "--api-key",
                "test-key",
                "--access-token",
                "",
            ],
        )

        assert result.exit_code == 1
        # Check both stdout and stderr for the error message
        output = result.stdout + result.stderr
        assert "Error validating server" in output
        # Config file should not be created when validation fails
        assert not mock_config_path.exists()
        # Verify run_command was called for validation
        mock_run_command.assert_called_once()
