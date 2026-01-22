from pathlib import Path

import rtoml
from typer.testing import CliRunner

from immich.cli.wrapper import config as config_commands


class TestConfigSet:
    def test_set_simple_key(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setting a simple key-value pair."""
        result = runner_without_auth.invoke(
            config_commands.app,
            ["set", "test_key", "--value", "test_value"],
        )

        assert result.exit_code == 0
        assert mock_config_path.exists()
        config_data = rtoml.load(mock_config_path)
        assert config_data["test_key"] == "test_value"

    def test_set_nested_key(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test setting a nested key using dot notation."""
        result = runner_without_auth.invoke(
            config_commands.app,
            [
                "set",
                "profiles.production.base_url",
                "--value",
                "https://prod.immich.app/api",
            ],
        )

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert (
            config_data["profiles"]["production"]["base_url"]
            == "https://prod.immich.app/api"
        )

    def test_set_overwrites_existing(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that set overwrites an existing value."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('key = "old-value"')

        result = runner_without_auth.invoke(
            config_commands.app,
            ["set", "key", "--value", "new-value"],
        )

        assert result.exit_code == 0
        config_data = rtoml.load(mock_config_path)
        assert config_data["key"] == "new-value"


class TestConfigGet:
    def test_get_simple_key(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test getting a simple key value."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('key = "value"')

        result = runner_without_auth.invoke(
            config_commands.app,
            ["get", "key"],
        )

        assert result.exit_code == 0
        assert "value" in result.stdout

    def test_get_nested_key(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test getting a nested key value."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\nbase_url = "https://demo.immich.app/api"'
        )

        result = runner_without_auth.invoke(
            config_commands.app,
            ["get", "profiles.default.base_url"],
        )

        assert result.exit_code == 0
        assert "https://demo.immich.app/api" in result.stdout

    def test_get_secret_masked(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that secrets are masked by default."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('[profiles.default]\napi_key = "secret-key-123"')

        result = runner_without_auth.invoke(
            config_commands.app,
            ["get", "profiles.default.api_key"],
        )

        assert result.exit_code == 0
        assert "secret-key-123" not in result.stdout
        assert "*" in result.stdout

    def test_get_secret_with_show_secrets(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that secrets are shown when --show-secrets is used."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('[profiles.default]\napi_key = "secret-key-123"')

        result = runner_without_auth.invoke(
            config_commands.app,
            ["get", "profiles.default.api_key", "--show-secrets"],
        )

        assert result.exit_code == 0
        assert "secret-key-123" in result.stdout

    def test_get_nonexistent_key(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that getting a non-existent key raises an error."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('key = "value"')

        result = runner_without_auth.invoke(
            config_commands.app,
            ["get", "nonexistent"],
        )

        assert result.exit_code != 0


class TestConfigReset:
    def test_reset_deletes_file(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that reset deletes the config file."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('key = "value"')
        assert mock_config_path.exists()

        result = runner_without_auth.invoke(
            config_commands.app,
            ["reset", "--yes"],
        )

        assert result.exit_code == 0
        assert not mock_config_path.exists()
        assert "Config file removed" in result.stdout

    def test_reset_nonexistent_file(
        self, runner_without_auth: CliRunner, mock_config_path: Path
    ):
        """Test that reset fails when config file doesn't exist."""
        assert not mock_config_path.exists()

        result = runner_without_auth.invoke(
            config_commands.app,
            ["reset", "--yes"],
        )

        assert result.exit_code != 0
