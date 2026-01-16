"""Generated CLI commands for Trash tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.

Docs: https://api.immich.app/endpoints/trash""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("empty-trash")
def empty_trash(
    ctx: typer.Context,
) -> None:
    """Empty trash

Docs: https://api.immich.app/endpoints/trash/emptyTrash
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.trash, 'empty_trash', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("restore-assets")
def restore_assets(
    ctx: typer.Context,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Restore assets

Docs: https://api.immich.app/endpoints/trash/restoreAssets
    """
    kwargs = {}
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ['ids'], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    result = run_command(client, client.trash, 'restore_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("restore-trash")
def restore_trash(
    ctx: typer.Context,
) -> None:
    """Restore trash

Docs: https://api.immich.app/endpoints/trash/restoreTrash
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.trash, 'restore_trash', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
