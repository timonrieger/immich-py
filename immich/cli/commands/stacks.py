"""Generated CLI commands for Stacks tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A stack is a group of related assets. One asset is the "primary" asset, and the rest are "child" assets. On the main timeline, stack parents are included by default, while child assets are hidden.

Docs: https://api.immich.app/endpoints/stacks""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-stack")
def create_stack(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds", help="""Asset IDs (first becomes primary, min 2)"""),
) -> None:
    """Create a stack

Docs: https://api.immich.app/endpoints/stacks/createStack
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.stack_create_dto import StackCreateDto
        stack_create_dto = deserialize_request_body(json_data, StackCreateDto)
        kwargs['stack_create_dto'] = stack_create_dto
    elif any([
        asset_ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if json_data:
            from immich.client.models.stack_create_dto import StackCreateDto
            stack_create_dto = deserialize_request_body(json_data, StackCreateDto)
            kwargs['stack_create_dto'] = stack_create_dto
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'create_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-stack")
def delete_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Stack ID"""),
) -> None:
    """Delete a stack

Docs: https://api.immich.app/endpoints/stacks/deleteStack
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'delete_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-stacks")
def delete_stacks(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Delete stacks

Docs: https://api.immich.app/endpoints/stacks/deleteStacks
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
    api_group = client.stacks
    result = run_command(client, api_group, 'delete_stacks', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-stack")
def get_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Stack ID"""),
) -> None:
    """Retrieve a stack

Docs: https://api.immich.app/endpoints/stacks/getStack
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'get_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-asset-from-stack")
def remove_asset_from_stack(
    ctx: typer.Context,
    asset_id: str = typer.Argument(..., help="""Asset ID to remove"""),
    id: str = typer.Argument(..., help="""Stack ID"""),
) -> None:
    """Remove an asset from a stack

Docs: https://api.immich.app/endpoints/stacks/removeAssetFromStack
    """
    kwargs = {}
    kwargs['asset_id'] = asset_id
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'remove_asset_from_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-stacks")
def search_stacks(
    ctx: typer.Context,
    primary_asset_id: str | None = typer.Option(None, "--primary-asset-id", help="""Filter by primary asset ID"""),
) -> None:
    """Retrieve stacks

Docs: https://api.immich.app/endpoints/stacks/searchStacks
    """
    kwargs = {}
    if primary_asset_id is not None:
        kwargs['primary_asset_id'] = primary_asset_id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'search_stacks', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-stack")
def update_stack(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Stack ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    primary_asset_id: str | None = typer.Option(None, "--primaryAssetId", help="""Primary asset ID"""),
) -> None:
    """Update a stack

Docs: https://api.immich.app/endpoints/stacks/updateStack
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([primary_asset_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.stack_update_dto import StackUpdateDto
        stack_update_dto = deserialize_request_body(json_data, StackUpdateDto)
        kwargs['stack_update_dto'] = stack_update_dto
    elif any([
        primary_asset_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if primary_asset_id is not None:
            set_nested(json_data, ['primaryAssetId'], primary_asset_id)
        if json_data:
            from immich.client.models.stack_update_dto import StackUpdateDto
            stack_update_dto = deserialize_request_body(json_data, StackUpdateDto)
            kwargs['stack_update_dto'] = stack_update_dto
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'update_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
