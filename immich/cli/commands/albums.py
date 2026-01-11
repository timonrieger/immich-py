"""Generated CLI commands for Albums tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
import typer

from immich.cli.runtime import (
    deserialize_request_body,
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
    id: str = typer.Argument(..., help="""Album ID"""),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
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
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    elif any(
        [
            ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ["ids"], ids)
        if json_data:
            from immich.client.models.bulk_ids_dto import BulkIdsDto

            bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
            kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "add_assets_to_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("add-assets-to-albums")
def add_assets_to_albums(
    ctx: typer.Context,
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    album_ids: list[str] = typer.Option(..., "--albumIds", help="""Album IDs"""),
    asset_ids: list[str] = typer.Option(..., "--assetIds", help="""Asset IDs"""),
) -> None:
    """Add assets to albums

    Docs: https://api.immich.app/endpoints/albums/addAssetsToAlbums
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([album_ids, asset_ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.albums_add_assets_dto import AlbumsAddAssetsDto

        albums_add_assets_dto = deserialize_request_body(json_data, AlbumsAddAssetsDto)
        kwargs["albums_add_assets_dto"] = albums_add_assets_dto
    elif any(
        [
            album_ids,
            asset_ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if album_ids is None:
            raise SystemExit("Error: --albumIds is required")
        set_nested(json_data, ["albumIds"], album_ids)
        if asset_ids is None:
            raise SystemExit("Error: --assetIds is required")
        set_nested(json_data, ["assetIds"], asset_ids)
        if json_data:
            from immich.client.models.albums_add_assets_dto import AlbumsAddAssetsDto

            albums_add_assets_dto = deserialize_request_body(
                json_data, AlbumsAddAssetsDto
            )
            kwargs["albums_add_assets_dto"] = albums_add_assets_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "add_assets_to_albums", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("add-users-to-album")
def add_users_to_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    album_users: list[str] = typer.Option(
        ..., "--albumUsers", help="""Album users to add"""
    ),
) -> None:
    """Share album with users

    Docs: https://api.immich.app/endpoints/albums/addUsersToAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([album_users])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.add_users_dto import AddUsersDto

        add_users_dto = deserialize_request_body(json_data, AddUsersDto)
        kwargs["add_users_dto"] = add_users_dto
    elif any(
        [
            album_users,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if album_users is None:
            raise SystemExit("Error: --albumUsers is required")
        value_album_users = json.loads(album_users)
        set_nested(json_data, ["albumUsers"], value_album_users)
        if json_data:
            from immich.client.models.add_users_dto import AddUsersDto

            add_users_dto = deserialize_request_body(json_data, AddUsersDto)
            kwargs["add_users_dto"] = add_users_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "add_users_to_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("create-album")
def create_album(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    album_name: str = typer.Option(..., "--albumName", help="""Album name"""),
    album_users: list[str] | None = typer.Option(
        None, "--albumUsers", help="""Album users"""
    ),
    asset_ids: list[str] | None = typer.Option(
        None, "--assetIds", help="""Initial asset IDs"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Album description"""
    ),
) -> None:
    """Create an album

    Docs: https://api.immich.app/endpoints/albums/createAlbum
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([album_name, album_users, asset_ids, description])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.create_album_dto import CreateAlbumDto

        create_album_dto = deserialize_request_body(json_data, CreateAlbumDto)
        kwargs["create_album_dto"] = create_album_dto
    elif any(
        [
            album_name,
            album_users,
            asset_ids,
            description,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if album_name is None:
            raise SystemExit("Error: --albumName is required")
        set_nested(json_data, ["albumName"], album_name)
        if album_users is not None:
            value_album_users = json.loads(album_users)
            set_nested(json_data, ["albumUsers"], value_album_users)
        if asset_ids is not None:
            set_nested(json_data, ["assetIds"], asset_ids)
        if description is not None:
            set_nested(json_data, ["description"], description)
        if json_data:
            from immich.client.models.create_album_dto import CreateAlbumDto

            create_album_dto = deserialize_request_body(json_data, CreateAlbumDto)
            kwargs["create_album_dto"] = create_album_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "create_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-album")
def delete_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
) -> None:
    """Delete an album

    Docs: https://api.immich.app/endpoints/albums/deleteAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "delete_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-album-info")
def get_album_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    key: str | None = typer.Option(
        None, "--key", help="""Access key for shared links"""
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="""Access slug for shared links"""
    ),
    without_assets: bool | None = typer.Option(
        None, "--without-assets", help="""Exclude assets from response"""
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
        kwargs["without_assets"] = without_assets
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "get_album_info", **kwargs)
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
    api_group = client.albums
    result = run_command(client, api_group, "get_album_statistics", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-albums")
def get_all_albums(
    ctx: typer.Context,
    asset_id: str | None = typer.Option(
        None,
        "--asset-id",
        help="""Filter albums containing this asset ID (ignores shared parameter)""",
    ),
    shared: bool | None = typer.Option(
        None,
        "--shared",
        help="""Filter by shared status: true = only shared, false = only own, undefined = all""",
    ),
) -> None:
    """List all albums

    Docs: https://api.immich.app/endpoints/albums/getAllAlbums
    """
    kwargs = {}
    if asset_id is not None:
        kwargs["asset_id"] = asset_id
    if shared is not None:
        kwargs["shared"] = shared
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "get_all_albums", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-asset-from-album")
def remove_asset_from_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Remove assets from an album

    Docs: https://api.immich.app/endpoints/albums/removeAssetFromAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([ids])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    elif any(
        [
            ids,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if ids is None:
            raise SystemExit("Error: --ids is required")
        set_nested(json_data, ["ids"], ids)
        if json_data:
            from immich.client.models.bulk_ids_dto import BulkIdsDto

            bulk_ids_dto = deserialize_request_body(json_data, BulkIdsDto)
            kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "remove_asset_from_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-user-from-album")
def remove_user_from_album(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    user_id: str = typer.Argument(
        ..., help="""User ID (use "me" to leave shared album)"""
    ),
) -> None:
    """Remove user from album

    Docs: https://api.immich.app/endpoints/albums/removeUserFromAlbum
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "remove_user_from_album", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-album-info")
def update_album_info(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    album_name: str | None = typer.Option(None, "--albumName", help="""Album name"""),
    album_thumbnail_asset_id: str | None = typer.Option(
        None, "--albumThumbnailAssetId", help="""Album thumbnail asset ID"""
    ),
    description: str | None = typer.Option(
        None, "--description", help="""Album description"""
    ),
    is_activity_enabled: bool | None = typer.Option(
        None, "--isActivityEnabled", help="""Enable activity feed"""
    ),
    order: str | None = typer.Option(None, "--order", help="""Asset sort order"""),
) -> None:
    """Update an album

    Docs: https://api.immich.app/endpoints/albums/updateAlbumInfo
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any(
        [album_name, album_thumbnail_asset_id, description, is_activity_enabled, order]
    )
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.update_album_dto import UpdateAlbumDto

        update_album_dto = deserialize_request_body(json_data, UpdateAlbumDto)
        kwargs["update_album_dto"] = update_album_dto
    elif any(
        [
            album_name,
            album_thumbnail_asset_id,
            description,
            is_activity_enabled,
            order,
        ]
    ):
        # Build body from dotted flags
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
        if json_data:
            from immich.client.models.update_album_dto import UpdateAlbumDto

            update_album_dto = deserialize_request_body(json_data, UpdateAlbumDto)
            kwargs["update_album_dto"] = update_album_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "update_album_info", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-album-user")
def update_album_user(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""Album ID"""),
    user_id: str = typer.Argument(..., help="""User ID (use "me" for current user)"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    role: str = typer.Option(..., "--role", help="""Album user role"""),
) -> None:
    """Update user role

    Docs: https://api.immich.app/endpoints/albums/updateAlbumUser
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([role])
    if has_json and has_flags:
        raise SystemExit(
            "Error: Cannot use both --json and dotted body flags together. Use one or the other."
        )
    if not has_json and not has_flags:
        raise SystemExit(
            "Error: Request body is required. Provide --json or use dotted body flags."
        )
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.update_album_user_dto import UpdateAlbumUserDto

        update_album_user_dto = deserialize_request_body(json_data, UpdateAlbumUserDto)
        kwargs["update_album_user_dto"] = update_album_user_dto
    elif any(
        [
            role,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if role is None:
            raise SystemExit("Error: --role is required")
        set_nested(json_data, ["role"], role)
        if json_data:
            from immich.client.models.update_album_user_dto import UpdateAlbumUserDto

            update_album_user_dto = deserialize_request_body(
                json_data, UpdateAlbumUserDto
            )
            kwargs["update_album_user_dto"] = update_album_user_dto
    client = ctx.obj["client"]
    api_group = client.albums
    result = run_command(client, api_group, "update_album_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
