"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.

Docs: https://api.immich.app/endpoints/tags""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("bulk-tag-assets")
def bulk_tag_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    asset_ids: list[str] = typer.Option(..., "--assetIds", help="""Asset IDs"""),
    tag_ids: list[str] = typer.Option(..., "--tagIds", help="""Tag IDs"""),
) -> None:
    """Tag assets

Docs: https://api.immich.app/endpoints/tags/bulkTagAssets
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([asset_ids, tag_ids])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto
        tag_bulk_assets_dto = deserialize_request_body(json_data, TagBulkAssetsDto)
        kwargs['tag_bulk_assets_dto'] = tag_bulk_assets_dto
    elif any([
        asset_ids,
        tag_ids,
    ]):
        # Build body from dotted flags
        json_data = {}
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ['assetIds'], asset_ids)
        if tag_ids is None:
            raise SystemExit("Error: --tagIds is required")
        set_nested(json_data, ['tagIds'], tag_ids)
        if json_data:
            from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto
            tag_bulk_assets_dto = deserialize_request_body(json_data, TagBulkAssetsDto)
            kwargs['tag_bulk_assets_dto'] = tag_bulk_assets_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'bulk_tag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-tag")
def create_tag(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    color: str | None = typer.Option(None, "--color", help="""Tag color (hex)"""),
    name: str = typer.Option(..., "--name", help="""Tag name"""),
    parent_id: str | None = typer.Option(None, "--parentId", help="""Parent tag ID"""),
) -> None:
    """Create a tag

Docs: https://api.immich.app/endpoints/tags/createTag
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([color, name, parent_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.tag_create_dto import TagCreateDto
        tag_create_dto = deserialize_request_body(json_data, TagCreateDto)
        kwargs['tag_create_dto'] = tag_create_dto
    elif any([
        color,
        name,
        parent_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if color is not None:
            set_nested(json_data, ['color'], color)
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ['name'], name)
        if parent_id is not None:
            set_nested(json_data, ['parentId'], parent_id)
        if json_data:
            from immich.client.models.tag_create_dto import TagCreateDto
            tag_create_dto = deserialize_request_body(json_data, TagCreateDto)
            kwargs['tag_create_dto'] = tag_create_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'create_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-tag")
def delete_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Tag ID"""),
) -> None:
    """Delete a tag

Docs: https://api.immich.app/endpoints/tags/deleteTag
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'delete_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-tags")
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags

Docs: https://api.immich.app/endpoints/tags/getAllTags
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'get_all_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-tag-by-id")
def get_tag_by_id(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Tag ID"""),
) -> None:
    """Retrieve a tag

Docs: https://api.immich.app/endpoints/tags/getTagById
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'get_tag_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("tag-assets")
def tag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Tag ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Tag assets

Docs: https://api.immich.app/endpoints/tags/tagAssets
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
    api_group = client.tags
    result = run_command(client, api_group, 'tag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("untag-assets")
def untag_assets(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Tag ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Untag assets

Docs: https://api.immich.app/endpoints/tags/untagAssets
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
    api_group = client.tags
    result = run_command(client, api_group, 'untag_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-tag")
def update_tag(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Tag ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    color: str | None = typer.Option(None, "--color", help="""Tag color (hex)"""),
) -> None:
    """Update a tag

Docs: https://api.immich.app/endpoints/tags/updateTag
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([color])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.tag_update_dto import TagUpdateDto
        tag_update_dto = deserialize_request_body(json_data, TagUpdateDto)
        kwargs['tag_update_dto'] = tag_update_dto
    elif any([
        color,
    ]):
        # Build body from dotted flags
        json_data = {}
        if color is not None:
            set_nested(json_data, ['color'], color)
        if json_data:
            from immich.client.models.tag_update_dto import TagUpdateDto
            tag_update_dto = deserialize_request_body(json_data, TagUpdateDto)
            kwargs['tag_update_dto'] = tag_update_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'update_tag', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("upsert-tags")
def upsert_tags(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    tags: list[str] = typer.Option(..., "--tags", help="""Tag names to upsert"""),
) -> None:
    """Upsert tags

Docs: https://api.immich.app/endpoints/tags/upsertTags
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([tags])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.tag_upsert_dto import TagUpsertDto
        tag_upsert_dto = deserialize_request_body(json_data, TagUpsertDto)
        kwargs['tag_upsert_dto'] = tag_upsert_dto
    elif any([
        tags,
    ]):
        # Build body from dotted flags
        json_data = {}
        if tags is None:
            raise SystemExit("Error: --tags is required")
        set_nested(json_data, ['tags'], tags)
        if json_data:
            from immich.client.models.tag_upsert_dto import TagUpsertDto
            tag_upsert_dto = deserialize_request_body(json_data, TagUpsertDto)
            kwargs['tag_upsert_dto'] = tag_upsert_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'upsert_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
