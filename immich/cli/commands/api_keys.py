"""Generated CLI commands for API keys tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""An api key can be used to programmatically access the Immich API.

Docs: https://api.immich.app/endpoints/api-keys""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-api-key")
def create_api_key(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    name: str | None = typer.Option(None, "--name", help="""API key name"""),
    permissions: list[str] = typer.Option(..., "--permissions", help="""List of permissions"""),
) -> None:
    """Create an API key

Docs: https://api.immich.app/endpoints/api-keys/createApiKey
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([name, permissions])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.api_key_create_dto import APIKeyCreateDto
        api_key_create_dto = deserialize_request_body(json_data, APIKeyCreateDto)
        kwargs['api_key_create_dto'] = api_key_create_dto
    elif any([
        name,
        permissions,
    ]):
        # Build body from dotted flags
        json_data = {}
        if name is not None:
            set_nested(json_data, ['name'], name)
        if permissions is None:
            raise SystemExit("Error: --permissions is required")
        value_permissions = json.loads(permissions)
        set_nested(json_data, ['permissions'], value_permissions)
        if json_data:
            from immich.client.models.api_key_create_dto import APIKeyCreateDto
            api_key_create_dto = deserialize_request_body(json_data, APIKeyCreateDto)
            kwargs['api_key_create_dto'] = api_key_create_dto
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'create_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-api-key")
def delete_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""API key ID"""),
) -> None:
    """Delete an API key

Docs: https://api.immich.app/endpoints/api-keys/deleteApiKey
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'delete_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-api-key")
def get_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""API key ID"""),
) -> None:
    """Retrieve an API key

Docs: https://api.immich.app/endpoints/api-keys/getApiKey
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'get_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-api-keys")
def get_api_keys(
    ctx: typer.Context,
) -> None:
    """List all API keys

Docs: https://api.immich.app/endpoints/api-keys/getApiKeys
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'get_api_keys', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-api-key")
def get_my_api_key(
    ctx: typer.Context,
) -> None:
    """Retrieve the current API key

Docs: https://api.immich.app/endpoints/api-keys/getMyApiKey
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'get_my_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-api-key")
def update_api_key(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""API key ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    name: str | None = typer.Option(None, "--name", help="""API key name"""),
    permissions: list[str] | None = typer.Option(None, "--permissions", help="""List of permissions"""),
) -> None:
    """Update an API key

Docs: https://api.immich.app/endpoints/api-keys/updateApiKey
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([name, permissions])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.api_key_update_dto import APIKeyUpdateDto
        api_key_update_dto = deserialize_request_body(json_data, APIKeyUpdateDto)
        kwargs['api_key_update_dto'] = api_key_update_dto
    elif any([
        name,
        permissions,
    ]):
        # Build body from dotted flags
        json_data = {}
        if name is not None:
            set_nested(json_data, ['name'], name)
        if permissions is not None:
            value_permissions = json.loads(permissions)
            set_nested(json_data, ['permissions'], value_permissions)
        if json_data:
            from immich.client.models.api_key_update_dto import APIKeyUpdateDto
            api_key_update_dto = deserialize_request_body(json_data, APIKeyUpdateDto)
            kwargs['api_key_update_dto'] = api_key_update_dto
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'update_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
