"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.

Docs: https://api.immich.app/endpoints/tags""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("bulk-tag-assets")
def bulk_tag_assets(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
    tag_ids: list[str] = typer.Option(..., "--tagIds"),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/bulkTagAssets
    """
    kwargs = {}
    has_flags = any([asset_ids, tag_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([asset_ids, tag_ids]):
        json_data = {}
        set_nested(json_data, ["assetIds"], asset_ids)
        set_nested(json_data, ["tagIds"], tag_ids)
        from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto

        tag_bulk_assets_dto = deserialize_request_body(json_data, TagBulkAssetsDto)
        kwargs["tag_bulk_assets_dto"] = tag_bulk_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "bulk_tag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("create-tag")
def create_tag(
    ctx: typer.Context,
    color: str | None = typer.Option(None, "--color"),
    name: str = typer.Option(..., "--name"),
    parent_id: str | None = typer.Option(None, "--parentId"),
) -> None:
    """Create a tag

    Docs: https://api.immich.app/endpoints/tags/createTag
    """
    kwargs = {}
    has_flags = any([color, name, parent_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([color, name, parent_id]):
        json_data = {}
        if color is not None:
            set_nested(json_data, ["color"], color)
        set_nested(json_data, ["name"], name)
        if parent_id is not None:
            set_nested(json_data, ["parentId"], parent_id)
        from immich.client.models.tag_create_dto import TagCreateDto

        tag_create_dto = deserialize_request_body(json_data, TagCreateDto)
        kwargs["tag_create_dto"] = tag_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "create_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-tag")
def delete_tag(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a tag

    Docs: https://api.immich.app/endpoints/tags/deleteTag
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "delete_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-tags")
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags

    Docs: https://api.immich.app/endpoints/tags/getAllTags
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_all_tags", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-tag-by-id")
def get_tag_by_id(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a tag

    Docs: https://api.immich.app/endpoints/tags/getTagById
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_tag_by_id", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("tag-assets")
def tag_assets(
    ctx: typer.Context,
    id: str,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/tagAssets
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "tag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("untag-assets")
def untag_assets(
    ctx: typer.Context,
    id: str,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Untag assets

    Docs: https://api.immich.app/endpoints/tags/untagAssets
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "untag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-tag")
def update_tag(
    ctx: typer.Context,
    id: str,
    color: str | None = typer.Option(None, "--color"),
) -> None:
    """Update a tag

    Docs: https://api.immich.app/endpoints/tags/updateTag
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([color])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([color]):
        json_data = {}
        if color is not None:
            set_nested(json_data, ["color"], color)
        from immich.client.models.tag_update_dto import TagUpdateDto

        tag_update_dto = deserialize_request_body(json_data, TagUpdateDto)
        kwargs["tag_update_dto"] = tag_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "update_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("upsert-tags")
def upsert_tags(
    ctx: typer.Context,
    tags: list[str] = typer.Option(..., "--tags"),
) -> None:
    """Upsert tags

    Docs: https://api.immich.app/endpoints/tags/upsertTags
    """
    kwargs = {}
    has_flags = any([tags])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([tags]):
        json_data = {}
        set_nested(json_data, ["tags"], tags)
        from immich.client.models.tag_upsert_dto import TagUpsertDto

        tag_upsert_dto = deserialize_request_body(json_data, TagUpsertDto)
        kwargs["tag_upsert_dto"] = tag_upsert_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "upsert_tags", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
