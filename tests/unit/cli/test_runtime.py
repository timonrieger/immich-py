"""Tests for immich.cli.runtime module."""

from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING, Any
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from pydantic import BaseModel
from typer import Context, Exit

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture

from immich.cli.runtime import (
    set_nested,
    print_response,
    format_api_error,
    run_async,
    run_command,
)
from immich.client.generated.exceptions import ApiException
from immich import AsyncClient


class TestSetNested:
    """Tests for set_nested function."""

    def test_set_nested_nested_levels(self) -> None:
        """Test setting nested values and overwriting non-dict values."""
        d: dict[str, Any] = {}
        set_nested(d, ["user", "name"], "John")
        assert d == {"user": {"name": "John"}}

        # Test overwriting non-dict value
        d = {"user": "not-a-dict"}
        set_nested(d, ["user", "name"], "John")
        assert d == {"user": {"name": "John"}}


class TestPrintResponse:
    """Tests for print_response function."""

    def test_print_response_base_model_json(
        self, capsys: "CaptureFixture[str]"
    ) -> None:
        """Test print_response with BaseModel and json format."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        class TestModel(BaseModel):
            name: str
            age: int

        data = TestModel(name="John", age=30)
        print_response(data, ctx)

        captured = capsys.readouterr()
        output = json.loads(captured.out)
        assert output["name"] == "John"
        assert output["age"] == 30

    def test_print_response_list_pretty(self, capsys: "CaptureFixture[str]") -> None:
        """Test print_response with list and pretty format."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "pretty"}

        class TestModel(BaseModel):
            name: str

        data = [TestModel(name="John"), TestModel(name="Jane")]
        print_response(data, ctx)

        captured = capsys.readouterr()
        assert "John" in captured.out
        assert "Jane" in captured.out

    def test_print_response_primitive_type(self, capsys: "CaptureFixture[str]") -> None:
        """Test print_response with primitive type (neither list nor BaseModel)."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        data = "simple string"
        print_response(data, ctx)

        captured = capsys.readouterr()
        output = json.loads(captured.out)
        assert output == "simple string"


class TestFormatApiError:
    """Tests for format_api_error function."""

    def test_format_api_error_no_body(self) -> None:
        """Test format_api_error with no body (with and without status)."""
        e: ApiException = ApiException(status=404)
        e.body = None

        message, code = format_api_error(e)
        assert message == "API error"
        assert code == 4

        # Test with no status
        e = ApiException(status=None)
        e.body = None

        message, code = format_api_error(e)
        assert message == "API error"
        assert code == 1

    def test_format_api_error_string_body(self) -> None:
        """Test format_api_error with string body."""
        e: ApiException = ApiException(status=400)
        e.body = '{"error": "test"}'

        message, code = format_api_error(e)
        assert message == '{"error": "test"}'
        assert code == 4

    def test_format_api_error_dict_body(self) -> None:
        """Test format_api_error with dict body (converts to JSON)."""
        e: ApiException = ApiException(status=500)
        e.body = {"error": "test", "code": 500}

        message, code = format_api_error(e)
        parsed = json.loads(message)
        assert parsed == {"error": "test", "code": 500}
        assert code == 5


class TestRunAsync:
    """Tests for run_async function."""

    async def test_run_async_success(self) -> None:
        """Test run_async with simple coroutine."""

        async def simple_coro() -> int:
            return 42

        result: int = await run_async(simple_coro())
        assert result == 42

    async def test_run_async_with_exception(self) -> None:
        """Test run_async with coroutine that raises exception."""

        async def failing_coro() -> None:
            raise ValueError("test error")

        with pytest.raises(ValueError, match="test error"):
            await run_async(failing_coro())


class TestRunCommand:
    """Tests for run_command function."""

    @patch("immich.cli.runtime.asyncio.run")
    def test_run_command_success(self, mock_asyncio_run: Mock) -> None:
        """Test run_command with successful execution."""
        mock_client: Mock = Mock(spec=AsyncClient)
        mock_client.close = AsyncMock()

        mock_api_group: MagicMock = MagicMock()
        mock_method: AsyncMock = AsyncMock(return_value={"result": "success"})
        mock_api_group.test_method = mock_method

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run

        result: dict[str, str] = run_command(
            mock_client, mock_api_group, "test_method", None, arg1="value1"
        )

        assert result == {"result": "success"}
        mock_asyncio_run.assert_called_once()

    @patch("immich.cli.runtime.print_")
    @patch("immich.cli.runtime.format_api_error")
    @patch("immich.cli.runtime.asyncio.run")
    def test_run_command_api_exception(
        self, mock_asyncio_run: Mock, mock_format_error: Mock, mock_print: Mock
    ) -> None:
        """Test run_command with ApiException."""
        mock_client: Mock = Mock(spec=AsyncClient)
        mock_client.close = AsyncMock()

        mock_api_group: MagicMock = MagicMock()
        api_error: ApiException = ApiException(status=404)
        api_error.body = {"error": "not found"}
        mock_method: AsyncMock = AsyncMock(side_effect=api_error)
        mock_api_group.test_method = mock_method

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run
        mock_format_error.return_value = ("not found", 4)

        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        with pytest.raises(Exit) as exc_info:
            run_command(mock_client, mock_api_group, "test_method", ctx)

        assert exc_info.value.exit_code == 4
        mock_format_error.assert_called_once_with(api_error)
        mock_print.assert_any_call("not found", type="error", ctx=ctx)

    @patch("immich.cli.runtime.print_")
    @patch("immich.cli.runtime.asyncio.run")
    def test_run_command_other_exception(
        self, mock_asyncio_run: Mock, mock_print: Mock
    ) -> None:
        """Test run_command with non-ApiException."""
        mock_client: Mock = Mock(spec=AsyncClient)
        mock_client.close = AsyncMock()

        mock_api_group: MagicMock = MagicMock()
        mock_method: AsyncMock = AsyncMock(side_effect=ValueError("test error"))
        mock_api_group.test_method = mock_method

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run

        with pytest.raises(Exit) as exc_info:
            run_command(mock_client, mock_api_group, "test_method", None)

        assert exc_info.value.exit_code == 1
        mock_print.assert_any_call(
            "Unexpected error: test error", type="error", ctx=None
        )

        mock_asyncio_run.assert_called_once()
