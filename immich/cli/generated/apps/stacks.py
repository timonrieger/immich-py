"""Generated CLI commands for Stacks tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Stacks operations")

@app.command("create-stack")
def create_stack(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a stack"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    id: str,
    ctx: typer.Context,
) -> None:
    """Delete a stack"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'delete_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-stacks")
def delete_stacks(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Delete stacks"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve a stack"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'get_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-asset-from-stack")
def remove_asset_from_stack(
    asset_id: str,
    id: str,
    ctx: typer.Context,
) -> None:
    """Remove an asset from a stack"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    primary_asset_id: str | None = typer.Option(None, "--primary-asset-id"),
    ctx: typer.Context,
) -> None:
    """Retrieve stacks"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update a stack"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.stack_update_dto import StackUpdateDto
        stack_update_dto = deserialize_request_body(json_data, StackUpdateDto)
        kwargs['stack_update_dto'] = stack_update_dto
    client = ctx.obj['client']
    api_group = client.stacks
    result = run_command(client, api_group, 'update_stack', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
