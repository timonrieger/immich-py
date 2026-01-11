"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints for managing and identifying duplicate assets.

Docs: https://api.immich.app/endpoints/duplicates""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("delete-duplicate")
def delete_duplicate(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Duplicate asset ID"""),
) -> None:
    """Delete a duplicate

Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicate
    """
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
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Delete duplicates

Docs: https://api.immich.app/endpoints/duplicates/deleteDuplicates
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    elif any([
        ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ['ids'], ids)
        if json_data:
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
    """Retrieve duplicates

Docs: https://api.immich.app/endpoints/duplicates/getAssetDuplicates
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.duplicates
    result = run_command(client, api_group, 'get_asset_duplicates', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
