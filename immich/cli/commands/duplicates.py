"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints for managing and identifying duplicate assets.. https://api.immich.app/endpoints/duplicates', context_settings={'help_option_names': ['-h', '--help']})

@app.command("delete-duplicate")
def delete_duplicate(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a duplicate"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.duplicates
    result = run_command(client, api_group, 'delete_duplicate', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-duplicates")
def delete_duplicates(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Delete duplicates"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.duplicates
    result = run_command(client, api_group, 'delete_duplicates', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-asset-duplicates")
def get_asset_duplicates(
    ctx: typer.Context,
) -> None:
    """Retrieve duplicates"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.duplicates
    result = run_command(client, api_group, 'get_asset_duplicates', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
