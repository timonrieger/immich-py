"""Generated CLI commands for API keys tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""An api key can be used to programmatically access the Immich API.\n\nDocs: https://api.immich.app/endpoints/api-keys"""
)


@app.command("create-api-key", deprecated=False, rich_help_panel="API commands")
def create_api_key(
    ctx: typer.Context,
    name: str | None = typer.Option(None, "--name", help=""""""),
    permissions: list[Permission] = typer.Option(..., "--permissions", help=""""""),
) -> None:  # pragma: no cover
    """Create an API key

    Docs: https://api.immich.app/endpoints/api-keys/createApiKey
    """
    kwargs = {}
    json_data = {}
    if name is not None:
        set_nested(json_data, ["name"], name)
    set_nested(json_data, ["permissions"], permissions)
    api_key_create_dto = APIKeyCreateDto.model_validate(json_data)
    kwargs["api_key_create_dto"] = api_key_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "create_api_key", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-api-key", deprecated=False, rich_help_panel="API commands")
def delete_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Delete an API key

    Docs: https://api.immich.app/endpoints/api-keys/deleteApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "delete_api_key", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-api-key", deprecated=False, rich_help_panel="API commands")
def get_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Retrieve an API key

    Docs: https://api.immich.app/endpoints/api-keys/getApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_key", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-api-keys", deprecated=False, rich_help_panel="API commands")
def get_api_keys(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """List all API keys

    Docs: https://api.immich.app/endpoints/api-keys/getApiKeys
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_keys", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-my-api-key", deprecated=False, rich_help_panel="API commands")
def get_my_api_key(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Retrieve the current API key

    Docs: https://api.immich.app/endpoints/api-keys/getMyApiKey
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_my_api_key", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-api-key", deprecated=False, rich_help_panel="API commands")
def update_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    permissions: list[Permission] | None = typer.Option(
        None, "--permissions", help=""""""
    ),
) -> None:  # pragma: no cover
    """Update an API key

    Docs: https://api.immich.app/endpoints/api-keys/updateApiKey
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if name is not None:
        set_nested(json_data, ["name"], name)
    if permissions is not None:
        set_nested(json_data, ["permissions"], permissions)
    api_key_update_dto = APIKeyUpdateDto.model_validate(json_data)
    kwargs["api_key_update_dto"] = api_key_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.api_keys, "update_api_key", ctx, **kwargs)
    print_response(result, ctx)
