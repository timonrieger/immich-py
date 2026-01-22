"""Generated CLI commands for Memories tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A memory is a specialized collection of assets with dedicated viewing implementations in the web and mobile clients. A memory includes fields related to visibility and are automatically generated per user via a background job.\n\n[link=https://api.immich.app/endpoints/memories]Immich API documentation[/link]"""
)


@app.command("add-memory-assets", deprecated=False, rich_help_panel="API commands")
def add_memory_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Add assets to a memory

    [link=https://api.immich.app/endpoints/memories/addMemoryAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "add_memory_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("create-memory", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/memories/createMemory]Immich API documentation[/link]
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
    memory_create_dto = MemoryCreateDto.model_validate(json_data)
    kwargs["memory_create_dto"] = memory_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "create_memory", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-memory", deprecated=False, rich_help_panel="API commands")
def delete_memory(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a memory

    [link=https://api.immich.app/endpoints/memories/deleteMemory]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "delete_memory", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-memory", deprecated=False, rich_help_panel="API commands")
def get_memory(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a memory

    [link=https://api.immich.app/endpoints/memories/getMemory]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "get_memory", ctx, **kwargs)
    print_response(result, ctx)


@app.command("memories-statistics", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/memories/memoriesStatistics]Immich API documentation[/link]
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
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "memories_statistics", ctx, **kwargs)
    print_response(result, ctx)


@app.command("remove-memory-assets", deprecated=False, rich_help_panel="API commands")
def remove_memory_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Remove assets from a memory

    [link=https://api.immich.app/endpoints/memories/removeMemoryAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "remove_memory_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-memories", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/memories/searchMemories]Immich API documentation[/link]
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
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "search_memories", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-memory", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/memories/updateMemory]Immich API documentation[/link]
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
    memory_update_dto = MemoryUpdateDto.model_validate(json_data)
    kwargs["memory_update_dto"] = memory_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.memories, "update_memory", ctx, **kwargs)
    print_response(result, ctx)
