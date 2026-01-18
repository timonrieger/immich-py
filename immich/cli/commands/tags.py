"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.\n\nDocs: https://api.immich.app/endpoints/tags"""
)


@app.command("bulk-tag-assets", deprecated=False)
def bulk_tag_assets(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    tag_ids: list[str] = typer.Option(..., "--tag-ids", help=""""""),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/bulkTagAssets
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["tag_ids"], tag_ids)
    from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto

    tag_bulk_assets_dto = TagBulkAssetsDto.model_validate(json_data)
    kwargs["tag_bulk_assets_dto"] = tag_bulk_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "bulk_tag_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("create-tag", deprecated=False)
def create_tag(
    ctx: typer.Context,
    color: str | None = typer.Option(None, "--color", help=""""""),
    name: str = typer.Option(..., "--name", help=""""""),
    parent_id: str | None = typer.Option(None, "--parent-id", help=""""""),
) -> None:
    """Create a tag

    Docs: https://api.immich.app/endpoints/tags/createTag
    """
    kwargs = {}
    json_data = {}
    if color is not None:
        set_nested(json_data, ["color"], color)
    set_nested(json_data, ["name"], name)
    if parent_id is not None:
        set_nested(json_data, ["parent_id"], parent_id)
    from immich.client.models.tag_create_dto import TagCreateDto

    tag_create_dto = TagCreateDto.model_validate(json_data)
    kwargs["tag_create_dto"] = tag_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "create_tag", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-tag", deprecated=False)
def delete_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete a tag

    Docs: https://api.immich.app/endpoints/tags/deleteTag
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "delete_tag", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-all-tags", deprecated=False)
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags

    Docs: https://api.immich.app/endpoints/tags/getAllTags
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_all_tags", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-tag-by-id", deprecated=False)
def get_tag_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a tag

    Docs: https://api.immich.app/endpoints/tags/getTagById
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_tag_by_id", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("tag-assets", deprecated=False)
def tag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/tagAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "tag_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("untag-assets", deprecated=False)
def untag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Untag assets

    Docs: https://api.immich.app/endpoints/tags/untagAssets
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "untag_assets", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-tag", deprecated=False)
def update_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    color: str | None = typer.Option(None, "--color", help=""""""),
) -> None:
    """Update a tag

    Docs: https://api.immich.app/endpoints/tags/updateTag
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if color is not None:
        set_nested(json_data, ["color"], color)
    from immich.client.models.tag_update_dto import TagUpdateDto

    tag_update_dto = TagUpdateDto.model_validate(json_data)
    kwargs["tag_update_dto"] = tag_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "update_tag", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("upsert-tags", deprecated=False)
def upsert_tags(
    ctx: typer.Context,
    tags: list[str] = typer.Option(..., "--tags", help=""""""),
) -> None:
    """Upsert tags

    Docs: https://api.immich.app/endpoints/tags/upsertTags
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["tags"], tags)
    from immich.client.models.tag_upsert_dto import TagUpsertDto

    tag_upsert_dto = TagUpsertDto.model_validate(json_data)
    kwargs["tag_upsert_dto"] = tag_upsert_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "upsert_tags", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
