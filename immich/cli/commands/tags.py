"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.. https://api.immich.app/endpoints/tags', context_settings={'help_option_names': ['-h', '--help']})

@app.command("bulk-tag-assets")
def bulk_tag_assets(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Tag assets"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
) -> None:
    """Create a tag"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
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
    id: str,
) -> None:
    """Delete a tag"""
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
    """Retrieve tags"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'get_all_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-tag-by-id")
def get_tag_by_id(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a tag"""
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
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Tag assets"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
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
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Untag assets"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
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
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update a tag"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
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
) -> None:
    """Upsert tags"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.tag_upsert_dto import TagUpsertDto
        tag_upsert_dto = deserialize_request_body(json_data, TagUpsertDto)
        kwargs['tag_upsert_dto'] = tag_upsert_dto
    client = ctx.obj['client']
    api_group = client.tags
    result = run_command(client, api_group, 'upsert_tags', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
