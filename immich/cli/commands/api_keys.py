"""Generated CLI commands for API keys tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='An api key can be used to programmatically access the Immich API.. https://api.immich.app/endpoints/api-keys', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-api-key")
def create_api_key(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create an API key"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
    id: str,
) -> None:
    """Delete an API key"""
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
    id: str,
) -> None:
    """Retrieve an API key"""
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
    """List all API keys"""
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
    """Retrieve the current API key"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'get_my_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-api-key")
def update_api_key(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update an API key"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.api_key_update_dto import APIKeyUpdateDto
        api_key_update_dto = deserialize_request_body(json_data, APIKeyUpdateDto)
        kwargs['api_key_update_dto'] = api_key_update_dto
    client = ctx.obj['client']
    api_group = client.api_keys
    result = run_command(client, api_group, 'update_api_key', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
