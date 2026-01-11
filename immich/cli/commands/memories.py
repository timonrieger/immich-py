"""Generated CLI commands for Memories tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A memory is a specialized collection of assets with dedicated viewing implementations in the web and mobile clients. A memory includes fields related to visibility and are automatically generated per user via a background job.

Docs: https://api.immich.app/endpoints/memories""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("add-memory-assets")
def add_memory_assets(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Add assets to a memory

Docs: https://api.immich.app/endpoints/memories/addMemoryAssets
    """
    kwargs = {}
    kwargs['id'] = id
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
    api_group = client.memories
    result = run_command(client, api_group, 'add_memory_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-memory")
def create_memory(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] | None = typer.Option(None, "--assetIds"),
    data_year: float = typer.Option(..., "--data.year"),
    is_saved: bool | None = typer.Option(None, "--isSaved"),
    memory_at: str = typer.Option(..., "--memoryAt"),
    seen_at: str | None = typer.Option(None, "--seenAt"),
    type: str = typer.Option(..., "--type"),
) -> None:
    """Create a memory

Docs: https://api.immich.app/endpoints/memories/createMemory
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids, data_year, is_saved, memory_at, seen_at, type])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.memory_create_dto import MemoryCreateDto
        memory_create_dto = deserialize_request_body(json_data, MemoryCreateDto)
        kwargs['memory_create_dto'] = memory_create_dto
    elif any([
        asset_ids,
        data_year,
        is_saved,
        memory_at,
        seen_at,
        type,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is not None:
            set_nested(json_data, ['assetIds'], asset_ids)
        if data_year is None:
            raise SystemExit("Error: --data.year is required")
        set_nested(json_data, ['data', 'year'], data_year)
        if is_saved is not None:
            set_nested(json_data, ['isSaved'], is_saved)
        if memory_at is None:
            raise SystemExit("Error: --memoryAt is required")
        set_nested(json_data, ['memoryAt'], memory_at)
        if seen_at is not None:
            set_nested(json_data, ['seenAt'], seen_at)
        if type is None:
            raise SystemExit("Error: --type is required")
        set_nested(json_data, ['type'], type)
        if json_data:
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
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a memory

Docs: https://api.immich.app/endpoints/memories/deleteMemory
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'delete_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-memory")
def get_memory(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a memory

Docs: https://api.immich.app/endpoints/memories/getMemory
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'get_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("memories-statistics")
def memories_statistics(
    ctx: typer.Context,
    for_: str | None = typer.Option(None, "--for"),
    is_saved: bool | None = typer.Option(None, "--is-saved"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    order: str | None = typer.Option(None, "--order"),
    size: int | None = typer.Option(None, "--size"),
    type: str | None = typer.Option(None, "--type"),
) -> None:
    """Retrieve memories statistics

Docs: https://api.immich.app/endpoints/memories/memoriesStatistics
    """
    kwargs = {}
    if for_ is not None:
        kwargs['for_'] = for_
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
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Remove assets from a memory

Docs: https://api.immich.app/endpoints/memories/removeMemoryAssets
    """
    kwargs = {}
    kwargs['id'] = id
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
    api_group = client.memories
    result = run_command(client, api_group, 'remove_memory_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-memories")
def search_memories(
    ctx: typer.Context,
    for_: str | None = typer.Option(None, "--for"),
    is_saved: bool | None = typer.Option(None, "--is-saved"),
    is_trashed: bool | None = typer.Option(None, "--is-trashed"),
    order: str | None = typer.Option(None, "--order"),
    size: int | None = typer.Option(None, "--size"),
    type: str | None = typer.Option(None, "--type"),
) -> None:
    """Retrieve memories

Docs: https://api.immich.app/endpoints/memories/searchMemories
    """
    kwargs = {}
    if for_ is not None:
        kwargs['for_'] = for_
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
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    is_saved: bool | None = typer.Option(None, "--isSaved"),
    memory_at: str | None = typer.Option(None, "--memoryAt"),
    seen_at: str | None = typer.Option(None, "--seenAt"),
) -> None:
    """Update a memory

Docs: https://api.immich.app/endpoints/memories/updateMemory
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([is_saved, memory_at, seen_at])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.memory_update_dto import MemoryUpdateDto
        memory_update_dto = deserialize_request_body(json_data, MemoryUpdateDto)
        kwargs['memory_update_dto'] = memory_update_dto
    elif any([
        is_saved,
        memory_at,
        seen_at,
    ]):
        # Build body from dotted flags
        json_data = {}
        if is_saved is not None:
            set_nested(json_data, ['isSaved'], is_saved)
        if memory_at is not None:
            set_nested(json_data, ['memoryAt'], memory_at)
        if seen_at is not None:
            set_nested(json_data, ['seenAt'], seen_at)
        if json_data:
            from immich.client.models.memory_update_dto import MemoryUpdateDto
            memory_update_dto = deserialize_request_body(json_data, MemoryUpdateDto)
            kwargs['memory_update_dto'] = memory_update_dto
    client = ctx.obj['client']
    api_group = client.memories
    result = run_command(client, api_group, 'update_memory', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
