"""Generated CLI commands for Albums tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='An album is a collection of assets that can be shared with other users or via shared links.. https://api.immich.app/endpoints/albums', context_settings={'help_option_names': ['-h', '--help']})

@app.command("add-assets-to-album")
def add_assets_to_album(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Add assets to an album"""
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'add_assets_to_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("add-assets-to-albums")
def add_assets_to_albums(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Add assets to albums"""
    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.albums_add_assets_dto import AlbumsAddAssetsDto
        albums_add_assets_dto = deserialize_request_body(json_data, AlbumsAddAssetsDto)
        kwargs['albums_add_assets_dto'] = albums_add_assets_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'add_assets_to_albums', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("add-users-to-album")
def add_users_to_album(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Share album with users"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.add_users_dto import AddUsersDto
        add_users_dto = deserialize_request_body(json_data, AddUsersDto)
        kwargs['add_users_dto'] = add_users_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'add_users_to_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-album")
def create_album(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create an album"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.create_album_dto import CreateAlbumDto
        create_album_dto = deserialize_request_body(json_data, CreateAlbumDto)
        kwargs['create_album_dto'] = create_album_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'create_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-album")
def delete_album(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete an album"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'delete_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-album-info")
def get_album_info(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    without_assets: bool | None = typer.Option(None, "--without-assets"),
) -> None:
    """Retrieve an album"""
    kwargs = {}
    kwargs['id'] = id
    if key is not None:
        kwargs['key'] = key
    if slug is not None:
        kwargs['slug'] = slug
    if without_assets is not None:
        kwargs['without_assets'] = without_assets
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'get_album_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-album-statistics")
def get_album_statistics(
    ctx: typer.Context,
) -> None:
    """Retrieve album statistics"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'get_album_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-all-albums")
def get_all_albums(
    ctx: typer.Context,
    asset_id: str | None = typer.Option(None, "--asset-id"),
    shared: bool | None = typer.Option(None, "--shared"),
) -> None:
    """List all albums"""
    kwargs = {}
    if asset_id is not None:
        kwargs['asset_id'] = asset_id
    if shared is not None:
        kwargs['shared'] = shared
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'get_all_albums', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-asset-from-album")
def remove_asset_from_album(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Remove assets from an album"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto
        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs['bulk_ids_dto'] = bulk_ids_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'remove_asset_from_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-user-from-album")
def remove_user_from_album(
    ctx: typer.Context,
    id: str,
    user_id: str,
) -> None:
    """Remove user from album"""
    kwargs = {}
    kwargs['id'] = id
    kwargs['user_id'] = user_id
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'remove_user_from_album', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-album-info")
def update_album_info(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update an album"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.update_album_dto import UpdateAlbumDto
        update_album_dto = deserialize_request_body(json_data, UpdateAlbumDto)
        kwargs['update_album_dto'] = update_album_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'update_album_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-album-user")
def update_album_user(
    ctx: typer.Context,
    id: str,
    user_id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update user role"""
    kwargs = {}
    kwargs['id'] = id
    kwargs['user_id'] = user_id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.update_album_user_dto import UpdateAlbumUserDto
        update_album_user_dto = deserialize_request_body(json_data, UpdateAlbumUserDto)
        kwargs['update_album_user_dto'] = update_album_user_dto
    client = ctx.obj['client']
    api_group = client.albums
    result = run_command(client, api_group, 'update_album_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
