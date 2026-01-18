"""Generated CLI commands for API keys tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""An api key can be used to programmatically access the Immich API.\n\nDocs: https://api.immich.app/endpoints/api-keys"""
)


@app.command("create-api-key", deprecated=False)
def create_api_key(
    ctx: typer.Context,
    name: str | None = typer.Option(None, "--name", help=""""""),
    permissions: list[Permission] = typer.Option(..., "--permissions", help=""""""),
) -> None:
    """Create an API key

    Docs: https://api.immich.app/endpoints/api-keys/createApiKey
    """
    kwargs = {}
    json_data = {}
    if name is not None:
        set_nested(json_data, ["name"], name)
    set_nested(json_data, ["permissions"], permissions)
    from immich.client.models.api_key_create_dto import APIKeyCreateDto

    api_key_create_dto = APIKeyCreateDto.model_validate(json_data)
    kwargs["api_key_create_dto"] = api_key_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "create_api_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-api-key", deprecated=False)
def delete_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete an API key

    Docs: https://api.immich.app/endpoints/api-keys/deleteApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "delete_api_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-api-key", deprecated=False)
def get_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve an API key

    Docs: https://api.immich.app/endpoints/api-keys/getApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-api-keys", deprecated=False)
def get_api_keys(
    ctx: typer.Context,
) -> None:
    """List all API keys

    Docs: https://api.immich.app/endpoints/api-keys/getApiKeys
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_keys", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-my-api-key", deprecated=False)
def get_my_api_key(
    ctx: typer.Context,
) -> None:
    """Retrieve the current API key

    Docs: https://api.immich.app/endpoints/api-keys/getMyApiKey
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_my_api_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-api-key", deprecated=False)
def update_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    permissions: list[Permission] | None = typer.Option(
        None, "--permissions", help=""""""
    ),
) -> None:
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
    from immich.client.models.api_key_update_dto import APIKeyUpdateDto

    api_key_update_dto = APIKeyUpdateDto.model_validate(json_data)
    kwargs["api_key_update_dto"] = api_key_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "update_api_key", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
