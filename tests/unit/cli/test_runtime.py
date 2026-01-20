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
    handle_api_error,
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


class TestHandleApiError:
    """Tests for handle_api_error function."""

    def test_handle_api_error_no_body(self) -> None:
        """Test handle_api_error with no body (with and without status)."""
        e: ApiException = ApiException(status=404)
        e.body = None

        with pytest.raises(Exit) as exc_info:
            handle_api_error(e, None)

        assert exc_info.value.exit_code == 4

        # Test with no status
        e = ApiException(status=None)
        e.body = None

        with pytest.raises(Exit) as exc_info:
            handle_api_error(e, None)

        assert exc_info.value.exit_code == 1

    @patch("immich.cli.utils.print_json")
    def test_handle_api_error_string_body_pretty(self, mock_print_json: Mock) -> None:
        """Test handle_api_error with string body and pretty format."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "pretty"}

        e: ApiException = ApiException(status=400)
        e.body = '{"error": "test"}'

        with pytest.raises(Exit) as exc_info:
            handle_api_error(e, ctx)

        mock_print_json.assert_called_once_with('{"error": "test"}')
        assert exc_info.value.exit_code == 4

    @patch("immich.cli.utils.print_json")
    def test_handle_api_error_dict_body(self, mock_print_json: Mock) -> None:
        """Test handle_api_error with dict body (converts to JSON)."""
        e: ApiException = ApiException(status=500)
        e.body = {"error": "test", "code": 500}

        with pytest.raises(Exit) as exc_info:
            handle_api_error(e, None)

        call_args = mock_print_json.call_args[0][0]
        parsed = json.loads(call_args)
        assert parsed == {"error": "test", "code": 500}
        assert exc_info.value.exit_code == 5


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

    @patch("immich.cli.runtime.handle_api_error")
    @patch("immich.cli.runtime.asyncio.run")
    def test_run_command_api_exception(
        self, mock_asyncio_run: Mock, mock_handle_error: Mock
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
        mock_handle_error.side_effect = Exit(4)

        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        with pytest.raises(Exit):
            run_command(mock_client, mock_api_group, "test_method", ctx)

        mock_handle_error.assert_called_once_with(api_error, ctx)

    @patch("immich.cli.runtime.asyncio.run")
    def test_run_command_other_exception(self, mock_asyncio_run: Mock) -> None:
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

        with pytest.raises(ValueError, match="test error"):
            run_command(mock_client, mock_api_group, "test_method", None)

        mock_asyncio_run.assert_called_once()
