from pathlib import Path

import rtoml
from typer.testing import CliRunner

from immich.cli.main import app


class TestSetup:
    def test_setup_with_all_parameters(self, runner: CliRunner, mock_config_path: Path):
        """Test setup command with all parameters provided."""
        result = runner.invoke(
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

        assert result.exit_code == 0
        assert mock_config_path.exists()
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["default"]["base_url"]
            == "https://demo.immich.app/api"
        )
        assert config_data["profiles"]["default"]["api_key"] == "test-api-key"
        assert config_data["profiles"]["default"]["access_token"] == "test-access-token"
        assert "Profile 'default' written to" in result.stdout

    def test_setup_with_custom_profile(self, runner: CliRunner, mock_config_path: Path):
        """Test setup command with custom profile."""
        result = runner.invoke(
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
        assert "Profile 'production' written to" in result.stdout

    def test_setup_with_only_base_url(self, runner: CliRunner, mock_config_path: Path):
        """Test setup command with only base_url (empty api_key and access_token)."""
        result = runner.invoke(
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

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["default"]["base_url"]
            == "https://demo.immich.app/api"
        )
        assert config_data["profiles"]["default"]["api_key"] == ""
        assert config_data["profiles"]["default"]["access_token"] == ""

    def test_setup_overwrites_existing_profile(
        self, runner: CliRunner, mock_config_path: Path
    ):
        """Test that setup overwrites an existing profile."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\nbase_url = "old-url"\napi_key = "old-key"'
        )

        result = runner.invoke(
            app,
            [
                "setup",
                "--base-url",
                "https://new.immich.app/api",
                "--api-key",
                "new-key",
                "--access-token",
                "",
            ],
        )

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["default"]["base_url"]
            == "https://new.immich.app/api"
        )
        assert config_data["profiles"]["default"]["api_key"] == "new-key"
