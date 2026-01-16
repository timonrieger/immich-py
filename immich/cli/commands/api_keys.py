"""Generated CLI commands for API keys tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""An api key can be used to programmatically access the Immich API.

Docs: https://api.immich.app/endpoints/api-keys""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-api-key")
def create_api_key(
    ctx: typer.Context,
    name: str | None = typer.Option(None, "--name"),
    permissions: list[str] = typer.Option(..., "--permissions"),
) -> None:
    """Create an API key

    Docs: https://api.immich.app/endpoints/api-keys/createApiKey
    """
    kwargs = {}
    has_flags = any([name, permissions])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            name,
            permissions,
        ]
    ):
        json_data = {}
        if name is not None:
            set_nested(json_data, ["name"], name)
        set_nested(json_data, ["permissions"], permissions)
        from immich.client.models.api_key_create_dto import APIKeyCreateDto

        api_key_create_dto = deserialize_request_body(json_data, APIKeyCreateDto)
        kwargs["api_key_create_dto"] = api_key_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "create_api_key", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-api-key")
def delete_api_key(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete an API key

    Docs: https://api.immich.app/endpoints/api-keys/deleteApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "delete_api_key", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-api-key")
def get_api_key(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve an API key

    Docs: https://api.immich.app/endpoints/api-keys/getApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_key", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-api-keys")
def get_api_keys(
    ctx: typer.Context,
) -> None:
    """List all API keys

    Docs: https://api.immich.app/endpoints/api-keys/getApiKeys
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_api_keys", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-my-api-key")
def get_my_api_key(
    ctx: typer.Context,
) -> None:
    """Retrieve the current API key

    Docs: https://api.immich.app/endpoints/api-keys/getMyApiKey
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "get_my_api_key", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-api-key")
def update_api_key(
    ctx: typer.Context,
    id: str,
    name: str | None = typer.Option(None, "--name"),
    permissions: list[str] | None = typer.Option(None, "--permissions"),
) -> None:
    """Update an API key

    Docs: https://api.immich.app/endpoints/api-keys/updateApiKey
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([name, permissions])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            name,
            permissions,
        ]
    ):
        json_data = {}
        if name is not None:
            set_nested(json_data, ["name"], name)
        if permissions is not None:
            set_nested(json_data, ["permissions"], permissions)
        from immich.client.models.api_key_update_dto import APIKeyUpdateDto

        api_key_update_dto = deserialize_request_body(json_data, APIKeyUpdateDto)
        kwargs["api_key_update_dto"] = api_key_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.api_keys, "update_api_key", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
