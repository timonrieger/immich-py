"""Runtime helpers for executing async client calls and handling output."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Optional

from immich.client.exceptions import ApiException
from pydantic import ValidationError

try:
    from rich import print_json
    from rich.console import Console
except ImportError:
    # Fallback if rich not available (shouldn't happen with cli extra)
    print_json = None
    Console = None


def load_json_file(path: Path) -> dict[str, Any]:
    """Load and parse JSON file."""
    try:
        content = path.read_text(encoding="utf-8")
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to read {path}: {e}", file=sys.stderr)
        sys.exit(1)

def load_file_bytes(path: Path) -> tuple[str, bytes]:
    """Load a file as bytes and return (filename, bytes) for multipart uploads."""
    try:
        return (path.name, path.read_bytes())
    except Exception as e:
        print(f"Error: Failed to read file {path}: {e}", file=sys.stderr)
        sys.exit(1)


def deserialize_request_body(
    json_data: dict[str, Any], model_class: type[Any]
) -> Any:
    """Deserialize JSON data into Pydantic model."""
    try:
        return model_class.model_validate(json_data)
    except ValidationError as e:
        print(f"Error: Invalid request body: {e}", file=sys.stderr)
        sys.exit(1)


def serialize_response(data: Any, format_mode: str = "pretty") -> str:
    """Serialize response data to JSON string."""
    # Convert Pydantic models to dict
    if hasattr(data, "model_dump"):
        data = data.model_dump()
    elif hasattr(data, "dict"):  # Pydantic v1 compatibility
        data = data.dict()

    json_str = json.dumps(data, indent=2, default=str)

    if format_mode == "pretty" and print_json:
        # Rich will handle the pretty printing
        return json_str
    return json_str


def print_response(data: Any, format_mode: str = "pretty") -> None:
    """Print response data."""
    json_str = serialize_response(data, format_mode)

    if format_mode == "pretty" and print_json:
        print_json(json_str)
    else:
        print(json_str)


def handle_api_error(e: ApiException) -> None:
    """Handle API exceptions and exit with appropriate code."""
    error_msg = f"API Error ({e.status}): {e.reason or 'Unknown error'}"
    if e.body:
        error_msg += f"\n{e.body}"
    print(error_msg, file=sys.stderr)
    sys.exit(1 if e.status is None else e.status // 100)


async def run_async(coro: Any) -> Any:
    """Run async coroutine from sync context."""
    try:
        return await coro
    except ApiException as e:
        handle_api_error(e)
        raise  # Should not reach here due to sys.exit


def run_command(
    client: AsyncClient,
    api_group: Any,
    method_name: str,
    **kwargs: Any,
) -> Any:
    """Run a client API method and return result."""
    method = getattr(api_group, method_name, None)
    if not callable(method):
        print(
            f"Error: Method {method_name} not found on API group",
            file=sys.stderr,
        )
        sys.exit(1)

    coro = method(**kwargs)
    
    # Run async call - client lifecycle is managed by the caller
    try:
        return asyncio.run(run_async(coro))
    except Exception as e:
        if isinstance(e, ApiException):
            handle_api_error(e)
        raise

