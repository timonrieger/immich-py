"""Runtime helpers for executing async client calls and handling output."""

from __future__ import annotations

import asyncio
import json
from typing import Any, Awaitable, Callable

from immich.cli.utils import print_
from pydantic import BaseModel
from typer import Context, Exit

from immich.cli.types import MaybeBaseModel

from immich import AsyncClient
from immich.client.generated.exceptions import ApiException


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


def print_response(data: MaybeBaseModel, ctx: Context) -> None:
    """Print response data."""

    def convert_to_dict(obj: MaybeBaseModel) -> Any:
        """Recursively convert Pydantic models to dicts."""
        if isinstance(obj, list):
            return [convert_to_dict(item) for item in obj]
        elif isinstance(obj, BaseModel):
            return obj.model_dump()
        else:
            return obj

    json_str = json.dumps(convert_to_dict(data), default=str)

    print_(message=json_str, type="json", ctx=ctx)


def handle_api_error(e: ApiException, ctx: Context | None = None) -> None:
    """Handle API exceptions and exit with appropriate code."""
    if not e.body:
        raise Exit(code=1 if e.status is None else e.status // 100)

    if isinstance(e.body, str):
        json_str = e.body
    else:
        json_str = json.dumps(e.body, default=str)

    print_(message=json_str, type="json", ctx=ctx)
    raise Exit(code=1 if e.status is None else e.status // 100)


async def run_async(coro: Awaitable[Any]) -> Any:
    """Run async coroutine from sync context."""
    return await coro


def run_command(
    client: AsyncClient,
    api_group: Any,
    method_name: str,
    ctx: Context | None = None,
    **kwargs: Any,
) -> Any:
    """Run a client API method and return result."""
    method: Callable[..., Awaitable[Any]] = getattr(api_group, method_name)

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
            handle_api_error(e, ctx)
        raise
