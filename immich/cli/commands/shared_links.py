"""Generated CLI commands for Shared links tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.. https://api.immich.app/endpoints/shared-links', context_settings={'help_option_names': ['-h', '--help']})

@app.command("add-shared-link-assets")
def add_shared_link_assets(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Add assets to a shared link"""
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_ids_dto import AssetIdsDto
        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs['asset_ids_dto'] = asset_ids_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'add_shared_link_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-shared-link")
def create_shared_link(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a shared link"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.shared_link_create_dto import SharedLinkCreateDto
        shared_link_create_dto = deserialize_request_body(json_data, SharedLinkCreateDto)
        kwargs['shared_link_create_dto'] = shared_link_create_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'create_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-shared-links")
def get_all_shared_links(
    ctx: typer.Context,
    album_id: str | None = typer.Option(None, "--album-id"),
    id: str | None = typer.Option(None, "--id"),
) -> None:
    """Retrieve all shared links"""
    kwargs = {}
    if album_id is not None:
        kwargs['album_id'] = album_id
    if id is not None:
        kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_all_shared_links', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-shared-link")
def get_my_shared_link(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    password: str | None = typer.Option(None, "--password"),
    slug: str | None = typer.Option(None, "--slug"),
    token: str | None = typer.Option(None, "--token"),
) -> None:
    """Retrieve current shared link"""
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if password is not None:
        kwargs['password'] = password
    if slug is not None:
        kwargs['slug'] = slug
    if token is not None:
        kwargs['token'] = token
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_my_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-shared-link-by-id")
def get_shared_link_by_id(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a shared link"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'get_shared_link_by_id', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-shared-link")
def remove_shared_link(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a shared link"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'remove_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-shared-link-assets")
def remove_shared_link_assets(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Remove assets from a shared link"""
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.asset_ids_dto import AssetIdsDto
        asset_ids_dto = deserialize_request_body(json_data, AssetIdsDto)
        kwargs['asset_ids_dto'] = asset_ids_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'remove_shared_link_assets', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-shared-link")
def update_shared_link(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update a shared link"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.shared_link_edit_dto import SharedLinkEditDto
        shared_link_edit_dto = deserialize_request_body(json_data, SharedLinkEditDto)
        kwargs['shared_link_edit_dto'] = shared_link_edit_dto
    client = ctx.obj['client']
    api_group = client.shared_links
    result = run_command(client, api_group, 'update_shared_link', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
