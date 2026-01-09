"""Generated CLI commands for Trash tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.. https://api.immich.app/endpoints/trash', context_settings={'help_option_names': ['-h', '--help']})

@app.command("empty-trash")
def empty_trash(
    ctx: typer.Context,
) -> None:
    """Empty trash"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.trash
    result = run_command(client, api_group, 'empty_trash', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("restore-assets")
def restore_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Restore assets"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.trash
    result = run_command(client, api_group, 'restore_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("restore-trash")
def restore_trash(
    ctx: typer.Context,
) -> None:
    """Restore trash"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.trash
    result = run_command(client, api_group, 'restore_trash', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
