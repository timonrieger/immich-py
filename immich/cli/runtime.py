"""Runtime helpers for executing async client calls and handling output."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from immich import AsyncClient
from immich.client.exceptions import ApiException
from pydantic import ValidationError
from rich import print_json


def load_file_bytes(path: Path) -> tuple[str, bytes]:
    """Load a file as bytes and return (filename, bytes) for multipart uploads."""
    try:
        return (path.name, path.read_bytes())
    except Exception as e:
        print(f"Error: Failed to read file {path}: {e}", file=sys.stderr)
        sys.exit(1)


def set_nested(d: dict[str, Any], path: list[str], value: Any) -> None:
    """Set a nested dictionary value using a path list.

    Example: set_nested({}, ['user', 'name'], 'John') -> {'user': {'name': 'John'}}
    """
    current = d
    for part in path[:-1]:
        if part not in current:
            current[part] = {}
        elif not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[path[-1]] = value


def deserialize_request_body(json_data: dict[str, Any], model_class: type[Any]) -> Any:
    """Deserialize JSON data into Pydantic model."""
    try:
        return model_class.model_validate(json_data)
    except ValidationError as e:
        print(f"Error: Invalid request body: {e}", file=sys.stderr)
        sys.exit(1)


def serialize_response(data: Any, format_mode: str = "pretty") -> str:
    """Serialize response data to JSON string."""

    def convert_to_dict(obj: Any) -> Any:
        """Recursively convert Pydantic models to dicts."""
        if hasattr(obj, "model_dump"):
            return obj.model_dump()
        elif hasattr(obj, "dict"):  # Pydantic v1 compatibility
            return obj.dict()
        elif isinstance(obj, list):
            return [convert_to_dict(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: convert_to_dict(v) for k, v in obj.items()}
        return obj

    data = convert_to_dict(data)
    indent = 2 if format_mode == "pretty" else None
    json_str = json.dumps(data, indent=indent, default=str)

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

    async def _call_and_close() -> Any:
        try:
            return await method(**kwargs)
        finally:
            # Ensure we don't leak aiohttp connectors/sessions after each command.
            # In a CLI context we generally run one command per process.
            await client.close()

    try:
        return asyncio.run(run_async(_call_and_close()))
    except Exception as e:
        if isinstance(e, ApiException):
            handle_api_error(e)
        raise
