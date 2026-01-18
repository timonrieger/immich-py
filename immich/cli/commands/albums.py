"""Generated CLI commands for Albums tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""An album is a collection of assets that can be shared with other users or via shared links.\n\nDocs: https://api.immich.app/endpoints/albums"""
)


@app.command("add-assets-to-album", deprecated=False)
def add_assets_to_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Add assets to an album

    Docs: https://api.immich.app/endpoints/albums/addAssetsToAlbum
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_assets_to_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("add-assets-to-albums", deprecated=False)
def add_assets_to_albums(
    ctx: typer.Context,
    album_ids: list[str] = typer.Option(..., "--album-ids", help=""""""),
    asset_ids: list[str] = typer.Option(..., "--asset-ids", help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
) -> None:
    """Add assets to albums

    Docs: https://api.immich.app/endpoints/albums/addAssetsToAlbums
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["album_ids"], album_ids)
    set_nested(json_data, ["asset_ids"], asset_ids)
    from immich.client.models.albums_add_assets_dto import AlbumsAddAssetsDto

    albums_add_assets_dto = AlbumsAddAssetsDto.model_validate(json_data)
    kwargs["albums_add_assets_dto"] = albums_add_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_assets_to_albums", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("add-users-to-album", deprecated=False)
def add_users_to_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    album_users: list[str] = typer.Option(
        ..., "--album-users", help="""As a JSON string"""
    ),
) -> None:
    """Share album with users

    Docs: https://api.immich.app/endpoints/albums/addUsersToAlbum
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_album_users = [json.loads(i) for i in album_users]
    set_nested(json_data, ["album_users"], value_album_users)
    from immich.client.models.add_users_dto import AddUsersDto

    add_users_dto = AddUsersDto.model_validate(json_data)
    kwargs["add_users_dto"] = add_users_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_users_to_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("create-album", deprecated=False)
def create_album(
    ctx: typer.Context,
    album_name: str = typer.Option(..., "--album-name", help=""""""),
    album_users: list[str] | None = typer.Option(
        None, "--album-users", help="""As a JSON string"""
    ),
    asset_ids: list[str] | None = typer.Option(None, "--asset-ids", help=""""""),
    description: str | None = typer.Option(None, "--description", help=""""""),
) -> None:
    """Create an album

    Docs: https://api.immich.app/endpoints/albums/createAlbum
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["album_name"], album_name)
    if album_users is not None:
        value_album_users = [json.loads(i) for i in album_users]
        set_nested(json_data, ["album_users"], value_album_users)
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    if description is not None:
        set_nested(json_data, ["description"], description)
    from immich.client.models.create_album_dto import CreateAlbumDto

    create_album_dto = CreateAlbumDto.model_validate(json_data)
    kwargs["create_album_dto"] = create_album_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "create_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-album", deprecated=False)
def delete_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete an album

    Docs: https://api.immich.app/endpoints/albums/deleteAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "delete_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-album-info", deprecated=False)
def get_album_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    key: str | None = typer.Option(None, "--key", help=""""""),
    slug: str | None = typer.Option(None, "--slug", help=""""""),
    without_assets: Literal["true", "false"] | None = typer.Option(
        None, "--without-assets", help=""""""
    ),
) -> None:
    """Retrieve an album

    Docs: https://api.immich.app/endpoints/albums/getAlbumInfo
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    if without_assets is not None:
        kwargs["without_assets"] = without_assets.lower() == "true"
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "get_album_info", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-album-statistics", deprecated=False)
def get_album_statistics(
    ctx: typer.Context,
) -> None:
    """Retrieve album statistics

    Docs: https://api.immich.app/endpoints/albums/getAlbumStatistics
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "get_album_statistics", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-all-albums", deprecated=False)
def get_all_albums(
    ctx: typer.Context,
    asset_id: str | None = typer.Option(
        None,
        "--asset-id",
        help="""Only returns albums that contain the asset
Ignores the shared parameter
undefined: get all albums""",
    ),
    shared: Literal["true", "false"] | None = typer.Option(
        None, "--shared", help=""""""
    ),
) -> None:
    """List all albums

    Docs: https://api.immich.app/endpoints/albums/getAllAlbums
    """
    kwargs = {}
    if asset_id is not None:
        kwargs["asset_id"] = asset_id
    if shared is not None:
        kwargs["shared"] = shared.lower() == "true"
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "get_all_albums", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-asset-from-album", deprecated=False)
def remove_asset_from_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    ids: list[str] = typer.Option(..., "--ids", help=""""""),
) -> None:
    """Remove assets from an album

    Docs: https://api.immich.app/endpoints/albums/removeAssetFromAlbum
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    from immich.client.models.bulk_ids_dto import BulkIdsDto

    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "remove_asset_from_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-user-from-album", deprecated=False)
def remove_user_from_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    user_id: str = typer.Argument(..., help=""""""),
) -> None:
    """Remove user from album

    Docs: https://api.immich.app/endpoints/albums/removeUserFromAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "remove_user_from_album", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-album-info", deprecated=False)
def update_album_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    album_name: str | None = typer.Option(None, "--album-name", help=""""""),
    album_thumbnail_asset_id: str | None = typer.Option(
        None, "--album-thumbnail-asset-id", help=""""""
    ),
    description: str | None = typer.Option(None, "--description", help=""""""),
    is_activity_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--is-activity-enabled", help=""""""
    ),
    order: str | None = typer.Option(None, "--order", help=""""""),
) -> None:
    """Update an album

    Docs: https://api.immich.app/endpoints/albums/updateAlbumInfo
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if album_name is not None:
        set_nested(json_data, ["album_name"], album_name)
    if album_thumbnail_asset_id is not None:
        set_nested(json_data, ["album_thumbnail_asset_id"], album_thumbnail_asset_id)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if is_activity_enabled is not None:
        set_nested(
            json_data, ["is_activity_enabled"], is_activity_enabled.lower() == "true"
        )
    if order is not None:
        set_nested(json_data, ["order"], order)
    from immich.client.models.update_album_dto import UpdateAlbumDto

    update_album_dto = UpdateAlbumDto.model_validate(json_data)
    kwargs["update_album_dto"] = update_album_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "update_album_info", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-album-user", deprecated=False)
def update_album_user(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    user_id: str = typer.Argument(..., help=""""""),
    role: str = typer.Option(..., "--role", help=""""""),
) -> None:
    """Update user role

    Docs: https://api.immich.app/endpoints/albums/updateAlbumUser
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    set_nested(json_data, ["role"], role)
    from immich.client.models.update_album_user_dto import UpdateAlbumUserDto

    update_album_user_dto = UpdateAlbumUserDto.model_validate(json_data)
    kwargs["update_album_user_dto"] = update_album_user_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "update_album_user", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
