"""Generated CLI commands for Memories tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A memory is a specialized collection of assets with dedicated viewing implementations in the web and mobile clients. A memory includes fields related to visibility and are automatically generated per user via a background job.\n\nDocs: https://api.immich.app/endpoints/memories"""
)


@app.command("add-memory-assets", deprecated=False)
def add_memory_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Add assets to a memory

    Docs: https://api.immich.app/endpoints/memories/addMemoryAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "add_memory_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("create-memory", deprecated=False)
def create_memory(
    ctx: typer.Context,
    asset_ids: list[str] | None = typer.Option(None, "--asset-ids", help=""""""),
    data_year: float = typer.Option(..., "--data-year", help="""""", min=1),
    is_saved: Literal["true", "false"] | None = typer.Option(
        None, "--is-saved", help=""""""
    ),
    memory_at: datetime = typer.Option(..., "--memory-at", help=""""""),
    seen_at: datetime | None = typer.Option(None, "--seen-at", help=""""""),
    type: str = typer.Option(..., "--type", help=""""""),
) -> None:
    """Create a memory

    Docs: https://api.immich.app/endpoints/memories/createMemory
    """
    kwargs = {}
    json_data = {}
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["data_year"], data_year)
    if is_saved is not None:
        set_nested(json_data, ["is_saved"], is_saved.lower() == "true")
    set_nested(json_data, ["memory_at"], memory_at)
    if seen_at is not None:
        set_nested(json_data, ["seen_at"], seen_at)
    set_nested(json_data, ["type"], type)
    from immich.client.models.memory_create_dto import MemoryCreateDto

    memory_create_dto = MemoryCreateDto.model_validate(json_data)
    kwargs["memory_create_dto"] = memory_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "create_memory", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-memory", deprecated=False)
def delete_memory(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a memory

    Docs: https://api.immich.app/endpoints/memories/deleteMemory
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "delete_memory", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-memory", deprecated=False)
def get_memory(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a memory

    Docs: https://api.immich.app/endpoints/memories/getMemory
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "get_memory", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("memories-statistics", deprecated=False)
def memories_statistics(
    ctx: typer.Context,
    for_: datetime | None = typer.Option(None, "--for", help=""""""),
    is_saved: Literal["true", "false"] | None = typer.Option(
        None, "--is-saved", help=""""""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help=""""""
    ),
    order: MemorySearchOrder | None = typer.Option(None, "--order", help=""""""),
    size: int | None = typer.Option(
        None, "--size", help="""Number of memories to return""", min=1
    ),
    type: MemoryType | None = typer.Option(None, "--type", help=""""""),
) -> None:
    """Retrieve memories statistics

    Docs: https://api.immich.app/endpoints/memories/memoriesStatistics
    """
    kwargs = {}
    if for_ is not None:
        kwargs["for_"] = for_
    if is_saved is not None:
        kwargs["is_saved"] = is_saved.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if order is not None:
        kwargs["order"] = order
    if size is not None:
        kwargs["size"] = size
    if type is not None:
        kwargs["type"] = type
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "memories_statistics", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-memory-assets", deprecated=False)
def remove_memory_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Remove assets from a memory

    Docs: https://api.immich.app/endpoints/memories/removeMemoryAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "remove_memory_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("search-memories", deprecated=False)
def search_memories(
    ctx: typer.Context,
    for_: datetime | None = typer.Option(None, "--for", help=""""""),
    is_saved: Literal["true", "false"] | None = typer.Option(
        None, "--is-saved", help=""""""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help=""""""
    ),
    order: MemorySearchOrder | None = typer.Option(None, "--order", help=""""""),
    size: int | None = typer.Option(
        None, "--size", help="""Number of memories to return""", min=1
    ),
    type: MemoryType | None = typer.Option(None, "--type", help=""""""),
) -> None:
    """Retrieve memories

    Docs: https://api.immich.app/endpoints/memories/searchMemories
    """
    kwargs = {}
    if for_ is not None:
        kwargs["for_"] = for_
    if is_saved is not None:
        kwargs["is_saved"] = is_saved.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if order is not None:
        kwargs["order"] = order
    if size is not None:
        kwargs["size"] = size
    if type is not None:
        kwargs["type"] = type
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "search_memories", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-memory", deprecated=False)
def update_memory(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    is_saved: Literal["true", "false"] | None = typer.Option(
        None, "--is-saved", help=""""""
    ),
    memory_at: datetime | None = typer.Option(None, "--memory-at", help=""""""),
    seen_at: datetime | None = typer.Option(None, "--seen-at", help=""""""),
) -> None:
    """Update a memory

    Docs: https://api.immich.app/endpoints/memories/updateMemory
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if is_saved is not None:
        set_nested(json_data, ["is_saved"], is_saved.lower() == "true")
    if memory_at is not None:
        set_nested(json_data, ["memory_at"], memory_at)
    if seen_at is not None:
        set_nested(json_data, ["seen_at"], seen_at)
    from immich.client.models.memory_update_dto import MemoryUpdateDto

    memory_update_dto = MemoryUpdateDto.model_validate(json_data)
    kwargs["memory_update_dto"] = memory_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.memories, "update_memory", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
