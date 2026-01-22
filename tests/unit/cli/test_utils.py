from pathlib import Path
from unittest.mock import Mock, patch

import pytest
import typer

from immich.cli.utils import (
    check_config,
    resolve_client_config,
    get_path,
    load_config,
    _is_secret_key,
    mask,
    _redact_secret,
    set_path,
    write_config,
    print_,
)
from immich.cli.types import ClientConfig


class TestSetPath:
    def test_set_path_single_level(self):
        """Test setting a single-level path."""
        data = {}
        set_path(data, "name", "John")
        assert data == {"name": "John"}

    def test_set_path_nested(self):
        """Test setting a nested path."""
        data = {}
        set_path(data, "user.name", "John")
        assert data == {"user": {"name": "John"}}

    def test_set_path_overwrite_existing(self):
        """Test overwriting an existing value."""
        data = {"user": {"name": "John"}}
        set_path(data, "user.name", "Jane")
        assert data == {"user": {"name": "Jane"}}


class TestGetPath:
    def test_get_path_nested(self):
        """Test getting a nested path."""
        data = {"user": {"name": "John"}}
        assert get_path(data, "user.name") == "John"

    def test_get_path_key_error(self):
        """Test that KeyError is raised for missing keys."""
        data = {"user": {"name": "John"}}
        with pytest.raises(KeyError):
            get_path(data, "user.age")


class TestLoadConfig:
    def test_load_config_does_not_create_file(self, mock_config_path: Path):
        """Test load_config does not create file if it doesn't exist."""
        result = load_config()
        assert not mock_config_path.exists()
        assert result == {}

    def test_load_config_existing_file(self, mock_config_path: Path):
        """Test load_config on existing file."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('key = "value"')
        result = load_config()
        assert result == {"key": "value"}

    def test_load_config_file_not_exists(self, mock_config_path: Path):
        """Test load_config when file doesn't exist."""
        result = load_config()
        assert result == {}


class TestWriteConfig:
    def test_write_config_creates_file_and_sets_permissions(
        self, mock_config_path: Path
    ):
        """Test that write_config creates the file and sets permissions."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        write_config({"key": "value"})
        assert mock_config_path.exists()
        assert mock_config_path.read_text() == 'key = "value"\n'
        assert oct(mock_config_path.stat().st_mode)[-3:] == "600"


class TestCheckConfig:
    def test_check_config_file_exists(self, mock_config_path: Path):
        """Test check_config when file exists."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.touch()
        result = check_config()
        assert result is None

    def test_check_config_file_not_exists(self, mock_config_path: Path):
        """Test check_config when file doesn't exist."""
        with pytest.raises(typer.Exit) as exc_info:
            check_config()
        assert exc_info.value.exit_code == 1


class TestGetClientConfig:
    def test_get_client_config_from_file(self, mock_config_path: Path):
        """Test get_client_config loads from config file."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"'
        )
        config = ClientConfig(api_key=None, base_url=None, access_token=None)
        result = resolve_client_config(config, profile="default")
        assert result.api_key == "file-key"
        assert result.base_url == "http://file.url"

    def test_get_client_config_prefers_provided_values(self, mock_config_path: Path):
        """Test that provided config values override file values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"'
        )
        config = ClientConfig(
            api_key="provided-key",
            base_url="http://provided.url",
            access_token=None,
        )
        result = resolve_client_config(config, profile="default")
        assert result.api_key == "provided-key"
        assert result.base_url == "http://provided.url"

    def test_get_client_config_partial_override(self, mock_config_path: Path):
        """Test that only provided values override file values."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"\naccess_token = "file-token"'
        )
        config = ClientConfig(
            api_key="provided-key",
            base_url=None,
            access_token=None,
        )
        result = resolve_client_config(config, profile="default")
        assert result.api_key == "provided-key"
        assert result.base_url == "http://file.url"
        assert result.access_token == "file-token"

    def test_get_client_config_empty_file(self, mock_config_path: Path):
        """Test get_client_config with empty config file."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.touch()
        config = ClientConfig(api_key=None, base_url=None, access_token=None)
        with pytest.raises(typer.Exit):
            resolve_client_config(config, profile="default", profile_explicit=True)

    def test_get_client_config_profile_not_in_file(self, mock_config_path: Path):
        """Test get_client_config when profile doesn't exist in file."""
        mock_config_path.parent.mkdir(parents=True, exist_ok=True)
        mock_config_path.write_text('[profiles.default]\napi_key = "default-key"')
        config = ClientConfig(api_key=None, base_url=None, access_token=None)
        with pytest.raises(typer.Exit):
            resolve_client_config(config, profile="nonexistent", profile_explicit=True)


class TestRedactSecret:
    def test_redact_secret_empty_string(self):
        """Test redact_secret with empty string."""
        assert _redact_secret("") == ""

    def test_redact_secret_short_string(self):
        """Test redact_secret with string shorter than start + end."""
        assert _redact_secret("ab") == "**"
        assert _redact_secret("abc") == "***"


class TestIsSecretKey:
    def test_is_secret_key_api_key(self):
        """Test _is_secret_key with api_key."""
        assert _is_secret_key("api_key") is True
        assert _is_secret_key("my_api_key") is True
        assert _is_secret_key("api_key_value") is True

    def test_is_secret_key_access_token(self):
        """Test _is_secret_key with access_token."""
        assert _is_secret_key("access_token") is True
        assert _is_secret_key("my_access_token") is True
        assert _is_secret_key("access_token_value") is True

    def test_is_secret_key_not_secret(self):
        """Test _is_secret_key with non-secret keys."""
        assert _is_secret_key("base_url") is False
        assert _is_secret_key("profile") is False
        assert _is_secret_key("name") is False


class TestMask:
    def test_mask_dict_with_secret_string(self):
        """Test mask with dictionary containing secret string value."""
        obj = {"api_key": "mysecretkey123", "base_url": "http://example.com"}
        result = mask(obj)
        assert result == {"api_key": "mys********123", "base_url": "http://example.com"}

    def test_mask_dict_with_secret_non_string(self):
        """Test mask with dictionary containing secret key but non-string value."""
        obj = {"api_key": {"nested": "value"}, "base_url": "http://example.com"}
        result = mask(obj)
        assert result == {
            "api_key": {"nested": "value"},
            "base_url": "http://example.com",
        }

    def test_mask_dict_nested(self):
        """Test mask with nested dictionary."""
        obj = {"user": {"api_key": "secret123", "name": "John"}}
        result = mask(obj)
        assert result == {"user": {"api_key": "sec***123", "name": "John"}}

    def test_mask_list(self):
        """Test mask with list."""
        obj = [{"api_key": "secret123"}, {"name": "John"}]
        result = mask(obj)
        assert result == [{"api_key": "sec***123"}, {"name": "John"}]

    def test_mask_list_nested(self):
        """Test mask with nested list."""
        obj = {"items": [{"api_key": "secret123"}]}
        result = mask(obj)
        assert result == {"items": [{"api_key": "sec***123"}]}

    def test_mask_string_with_secret_key(self):
        """Test mask with top-level string and secret key."""
        result = mask("mysecretkey123", key="api_key")
        assert result == "mys********123"

    def test_mask_string_without_secret_key(self):
        """Test mask with top-level string and non-secret key."""
        result = mask("mysecretkey123", key="base_url")
        assert result == "mysecretkey123"

    def test_mask_string_without_key(self):
        """Test mask with top-level string without key."""
        result = mask("mysecretkey123")
        assert result == "mys********123"

    def test_mask_custom_start_end(self):
        """Test mask with custom start and end values."""
        obj = {"api_key": "mysecretkey123"}
        result = mask(obj, start=2, end=2)
        assert result == {"api_key": "my**********23"}

    def test_mask_multiple_secrets(self):
        """Test mask with multiple secret keys."""
        obj = {"api_key": "key123", "access_token": "token456"}
        result = mask(obj)
        assert result == {"api_key": "******", "access_token": "tok**456"}

    def test_mask_empty_dict(self):
        """Test mask with empty dictionary."""
        assert mask({}) == {}

    def test_mask_empty_list(self):
        """Test mask with empty list."""
        assert mask([]) == []

    def test_mask_other_types(self):
        """Test mask with other types (int, bool, None)."""
        assert mask(123) == 123
        assert mask(True) is True
        assert mask(None) is None


class TestPrint:
    """Tests for print_ function."""

    @patch("immich.cli.utils.print_rich")
    def test_print_warning(self, mock_print_rich: Mock) -> None:
        """Test print_ with warning type."""
        print_("Test warning message", type="warning")
        mock_print_rich.assert_called_once_with(
            "[yellow][bold][Warning][/bold] Test warning message[/yellow]"
        )

    @patch("immich.cli.utils.print_rich")
    def test_print_debug_with_verbose_true(self, mock_print_rich: Mock) -> None:
        """Test print_ with debug type when verbose is True."""
        ctx = Mock(spec=typer.Context)
        ctx.obj = {"verbose": True}
        print_("Test debug message", type="debug", ctx=ctx)
        mock_print_rich.assert_called_once_with(
            "[blue][bold][Debug][/bold] Test debug message[/blue]"
        )

    @patch("immich.cli.utils.print_rich")
    def test_print_debug_with_verbose_false(self, mock_print_rich: Mock) -> None:
        """Test print_ with debug type when verbose is False."""
        ctx = Mock(spec=typer.Context)
        ctx.obj = {"verbose": False}
        print_("Test debug message", type="debug", ctx=ctx)
        mock_print_rich.assert_not_called()

    @patch("immich.cli.utils.print_rich")
    def test_print_debug_without_ctx(self, mock_print_rich: Mock) -> None:
        """Test print_ with debug type when ctx is None."""
        print_("Test debug message", type="debug", ctx=None)
        mock_print_rich.assert_not_called()

    @patch("builtins.print")
    def test_print_text(self, mock_print: Mock) -> None:
        """Test print_ with text type."""
        print_("Test text message", type="text")
        mock_print.assert_called_once_with("Test text message")

    @patch("immich.cli.utils.print_rich")
    def test_print_info(self, mock_print_rich: Mock) -> None:
        """Test print_ with info type."""
        print_("Test info message", type="info")
        mock_print_rich.assert_called_once_with("Test info message")

    @patch("immich.cli.utils.print_rich")
    def test_print_success(self, mock_print_rich: Mock) -> None:
        """Test print_ with success type."""
        print_("Test success message", type="success")
        mock_print_rich.assert_called_once_with(
            "[green][bold][Success][/bold][/green] Test success message"
        )

    @patch("immich.cli.utils.print_rich")
    def test_print_error(self, mock_print_rich: Mock) -> None:
        """Test print_ with error type."""
        print_("Test error message", type="error")
        mock_print_rich.assert_called_once_with(
            "[red][bold][Error][/bold] Test error message[/red]"
        )

    @patch("immich.cli.utils.print_json")
    def test_print_json_ctx_missing_format(self, mock_print_json: Mock) -> None:
        """Test print_ with json type when ctx.obj is missing format key."""
        ctx = Mock(spec=typer.Context)
        ctx.obj = {}
        print_('{"key": "value"}', type="json", ctx=ctx)
        mock_print_json.assert_called_once_with('{"key": "value"}')

    @patch("immich.cli.utils.print_json")
    def test_print_json_ctx_attribute_error(self, mock_print_json: Mock) -> None:
        """Test print_ with json type when ctx.obj raises AttributeError."""
        ctx = Mock(spec=typer.Context)
        ctx.obj = None
        print_('{"key": "value"}', type="json", ctx=ctx)
        mock_print_json.assert_called_once_with('{"key": "value"}')
