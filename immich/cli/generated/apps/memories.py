"""Generated CLI commands for Memories tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Memories operations")

@app.command("add-memory-assets")
def add_memory_assets(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Add assets to a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'add_memory_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-memory")
def create_memory(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.memory_create_dto import MemoryCreateDto
        memory_create_dto = deserialize_request_body(json_data, MemoryCreateDto)
        kwargs['memory_create_dto'] = memory_create_dto
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'create_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-memory")
def delete_memory(
    id: str,
    ctx: typer.Context,
) -> None:
    """Delete a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'delete_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-memory")
def get_memory(
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'get_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("memories-statistics")
def memories_statistics(
    for: str | None = typer.Option(None, "--for"),
    is_saved: bool | None = typer.Option(None, "--is-saved"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    order: MemorySearchOrder | None = typer.Option(None, "--order"),
    size: int | None = typer.Option(None, "--size"),
    type: MemoryType | None = typer.Option(None, "--type"),
    ctx: typer.Context,
) -> None:
    """Retrieve memories statistics"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if for is not None:
        kwargs['for'] = for
    if is_saved is not None:
        kwargs['is_saved'] = is_saved
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if order is not None:
        kwargs['order'] = order
    if size is not None:
        kwargs['size'] = size
    if type is not None:
        kwargs['type'] = type
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'memories_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-memory-assets")
def remove_memory_assets(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Remove assets from a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'remove_memory_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-memories")
def search_memories(
    for: str | None = typer.Option(None, "--for"),
    is_saved: bool | None = typer.Option(None, "--is-saved"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    order: MemorySearchOrder | None = typer.Option(None, "--order"),
    size: int | None = typer.Option(None, "--size"),
    type: MemoryType | None = typer.Option(None, "--type"),
    ctx: typer.Context,
) -> None:
    """Retrieve memories"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if for is not None:
        kwargs['for'] = for
    if is_saved is not None:
        kwargs['is_saved'] = is_saved
    if is_trashed is not None:
        kwargs['is_trashed'] = is_trashed
    if order is not None:
        kwargs['order'] = order
    if size is not None:
        kwargs['size'] = size
    if type is not None:
        kwargs['type'] = type
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'search_memories', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-memory")
def update_memory(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update a memory"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.memory_update_dto import MemoryUpdateDto
        memory_update_dto = deserialize_request_body(json_data, MemoryUpdateDto)
        kwargs['memory_update_dto'] = memory_update_dto
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'update_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
