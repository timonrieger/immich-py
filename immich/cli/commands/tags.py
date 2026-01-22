"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.\n\n[link=https://api.immich.app/endpoints/tags]Immich API documentation[/link]"""
)


@app.command("bulk-tag-assets", deprecated=False, rich_help_panel="API commands")
def bulk_tag_assets(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    tag_ids: list[str] = typer.Option(..., "--tag-ids", help=""""""),
) -> None:
    """Tag assets

    [link=https://api.immich.app/endpoints/tags/bulkTagAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["tag_ids"], tag_ids)
    tag_bulk_assets_dto = TagBulkAssetsDto.model_validate(json_data)
    kwargs["tag_bulk_assets_dto"] = tag_bulk_assets_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "bulk_tag_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("create-tag", deprecated=False, rich_help_panel="API commands")
def create_tag(
    ctx: typer.Context,
    color: str | None = typer.Option(None, "--color", help=""""""),
    name: str = typer.Option(..., "--name", help=""""""),
    parent_id: str | None = typer.Option(None, "--parent-id", help=""""""),
) -> None:
    """Create a tag

    [link=https://api.immich.app/endpoints/tags/createTag]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if color is not None:
        set_nested(json_data, ["color"], color)
    set_nested(json_data, ["name"], name)
    if parent_id is not None:
        set_nested(json_data, ["parent_id"], parent_id)
    tag_create_dto = TagCreateDto.model_validate(json_data)
    kwargs["tag_create_dto"] = tag_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "create_tag", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-tag", deprecated=False, rich_help_panel="API commands")
def delete_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a tag

    [link=https://api.immich.app/endpoints/tags/deleteTag]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "delete_tag", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-all-tags", deprecated=False, rich_help_panel="API commands")
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags

    [link=https://api.immich.app/endpoints/tags/getAllTags]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "get_all_tags", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-tag-by-id", deprecated=False, rich_help_panel="API commands")
def get_tag_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a tag

    [link=https://api.immich.app/endpoints/tags/getTagById]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "get_tag_by_id", ctx, **kwargs)
    print_response(result, ctx)


@app.command("tag-assets", deprecated=False, rich_help_panel="API commands")
def tag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Tag assets

    [link=https://api.immich.app/endpoints/tags/tagAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "tag_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("untag-assets", deprecated=False, rich_help_panel="API commands")
def untag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Untag assets

    [link=https://api.immich.app/endpoints/tags/untagAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "untag_assets", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-tag", deprecated=False, rich_help_panel="API commands")
def update_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    color: str | None = typer.Option(None, "--color", help=""""""),
) -> None:
    """Update a tag

    [link=https://api.immich.app/endpoints/tags/updateTag]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if color is not None:
        set_nested(json_data, ["color"], color)
    tag_update_dto = TagUpdateDto.model_validate(json_data)
    kwargs["tag_update_dto"] = tag_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "update_tag", ctx, **kwargs)
    print_response(result, ctx)


@app.command("upsert-tags", deprecated=False, rich_help_panel="API commands")
def upsert_tags(
    ctx: typer.Context,
    tags: list[str] = typer.Option(..., "--tags", help=""""""),
) -> None:
    """Upsert tags

    [link=https://api.immich.app/endpoints/tags/upsertTags]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["tags"], tags)
    tag_upsert_dto = TagUpsertDto.model_validate(json_data)
    kwargs["tag_upsert_dto"] = tag_upsert_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.tags, "upsert_tags", ctx, **kwargs)
    print_response(result, ctx)
