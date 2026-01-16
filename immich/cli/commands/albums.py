"""Generated CLI commands for Albums tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    parse_complex_list,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""An album is a collection of assets that can be shared with other users or via shared links.

Docs: https://api.immich.app/endpoints/albums""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("add-assets-to-album")
def add_assets_to_album(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Add assets to an album

    Docs: https://api.immich.app/endpoints/albums/addAssetsToAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_assets_to_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("add-assets-to-albums")
def add_assets_to_albums(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    album_ids: list[str] = typer.Option(..., "--albumIds"),
    asset_ids: list[str] = typer.Option(..., "--assetIds"),
) -> None:
    """Add assets to albums

    Docs: https://api.immich.app/endpoints/albums/addAssetsToAlbums
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    has_flags = any([album_ids, asset_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            album_ids,
            asset_ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["albumIds"], album_ids)
        set_nested(json_data, ["assetIds"], asset_ids)
        from immich.client.models.albums_add_assets_dto import AlbumsAddAssetsDto

        albums_add_assets_dto = deserialize_request_body(json_data, AlbumsAddAssetsDto)
        kwargs["albums_add_assets_dto"] = albums_add_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_assets_to_albums", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("add-users-to-album")
def add_users_to_album(
    ctx: typer.Context,
    id: str,
    album_users: list[str] = typer.Option(
        ...,
        "--albumUsers",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
) -> None:
    """Share album with users

    Docs: https://api.immich.app/endpoints/albums/addUsersToAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([album_users])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            album_users,
        ]
    ):
        json_data = {}
        value_album_users = parse_complex_list(album_users)
        set_nested(json_data, ["albumUsers"], value_album_users)
        from immich.client.models.add_users_dto import AddUsersDto

        add_users_dto = deserialize_request_body(json_data, AddUsersDto)
        kwargs["add_users_dto"] = add_users_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "add_users_to_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("create-album")
def create_album(
    ctx: typer.Context,
    album_name: str = typer.Option(..., "--albumName"),
    album_users: list[str] | None = typer.Option(
        None,
        "--albumUsers",
        help="key=value pairs (repeatable); e.g. key1=value1,key2=value2",
    ),
    asset_ids: list[str] | None = typer.Option(None, "--assetIds"),
    description: str | None = typer.Option(None, "--description"),
) -> None:
    """Create an album

    Docs: https://api.immich.app/endpoints/albums/createAlbum
    """
    kwargs = {}
    has_flags = any([album_name, album_users, asset_ids, description])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            album_name,
            album_users,
            asset_ids,
            description,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["albumName"], album_name)
        if album_users is not None:
            value_album_users = parse_complex_list(album_users)
            set_nested(json_data, ["albumUsers"], value_album_users)
        if asset_ids is not None:
            set_nested(json_data, ["assetIds"], asset_ids)
        if description is not None:
            set_nested(json_data, ["description"], description)
        from immich.client.models.create_album_dto import CreateAlbumDto

        create_album_dto = deserialize_request_body(json_data, CreateAlbumDto)
        kwargs["create_album_dto"] = create_album_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "create_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-album")
def delete_album(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete an album

    Docs: https://api.immich.app/endpoints/albums/deleteAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "delete_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-album-info")
def get_album_info(
    ctx: typer.Context,
    id: str,
    key: str | None = typer.Option(None, "--key"),
    slug: str | None = typer.Option(None, "--slug"),
    without_assets: str | None = typer.Option(None, "--without-assets"),
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-album-statistics")
def get_album_statistics(
    ctx: typer.Context,
) -> None:
    """Retrieve album statistics

    Docs: https://api.immich.app/endpoints/albums/getAlbumStatistics
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "get_album_statistics", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-albums")
def get_all_albums(
    ctx: typer.Context,
    asset_id: str | None = typer.Option(
        None,
        "--asset-id",
        help="""Only returns albums that contain the asset
Ignores the shared parameter
undefined: get all albums""",
    ),
    shared: str | None = typer.Option(None, "--shared"),
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-asset-from-album")
def remove_asset_from_album(
    ctx: typer.Context,
    id: str,
    ids: list[str] = typer.Option(..., "--ids"),
) -> None:
    """Remove assets from an album

    Docs: https://api.immich.app/endpoints/albums/removeAssetFromAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            ids,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "remove_asset_from_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-user-from-album")
def remove_user_from_album(
    ctx: typer.Context,
    id: str,
    user_id: str,
) -> None:
    """Remove user from album

    Docs: https://api.immich.app/endpoints/albums/removeUserFromAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "remove_user_from_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-album-info")
def update_album_info(
    ctx: typer.Context,
    id: str,
    album_name: str | None = typer.Option(None, "--albumName"),
    album_thumbnail_asset_id: str | None = typer.Option(
        None, "--albumThumbnailAssetId"
    ),
    description: str | None = typer.Option(None, "--description"),
    is_activity_enabled: bool | None = typer.Option(None, "--isActivityEnabled"),
    order: str | None = typer.Option(None, "--order"),
) -> None:
    """Update an album

    Docs: https://api.immich.app/endpoints/albums/updateAlbumInfo
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any(
        [album_name, album_thumbnail_asset_id, description, is_activity_enabled, order]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            album_name,
            album_thumbnail_asset_id,
            description,
            is_activity_enabled,
            order,
        ]
    ):
        json_data = {}
        if album_name is not None:
            set_nested(json_data, ["albumName"], album_name)
        if album_thumbnail_asset_id is not None:
            set_nested(json_data, ["albumThumbnailAssetId"], album_thumbnail_asset_id)
        if description is not None:
            set_nested(json_data, ["description"], description)
        if is_activity_enabled is not None:
            set_nested(json_data, ["isActivityEnabled"], is_activity_enabled)
        if order is not None:
            set_nested(json_data, ["order"], order)
        from immich.client.models.update_album_dto import UpdateAlbumDto

        update_album_dto = deserialize_request_body(json_data, UpdateAlbumDto)
        kwargs["update_album_dto"] = update_album_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "update_album_info", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-album-user")
def update_album_user(
    ctx: typer.Context,
    id: str,
    user_id: str,
    role: str = typer.Option(..., "--role"),
) -> None:
    """Update user role

    Docs: https://api.immich.app/endpoints/albums/updateAlbumUser
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    has_flags = any([role])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            role,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["role"], role)
        from immich.client.models.update_album_user_dto import UpdateAlbumUserDto

        update_album_user_dto = deserialize_request_body(json_data, UpdateAlbumUserDto)
        kwargs["update_album_user_dto"] = update_album_user_dto
    client = ctx.obj["client"]
    result = run_command(client, client.albums, "update_album_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
