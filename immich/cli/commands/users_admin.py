"""Generated CLI commands for Users (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Administrative endpoints for managing users, including creating, updating, deleting, and restoring users. Also includes endpoints for resetting passwords and PIN codes.

Docs: https://api.immich.app/endpoints/users-admin""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-user-admin")
def create_user_admin(
    ctx: typer.Context,
    avatar_color: str | None = typer.Option(None, "--avatarColor"),
    email: str = typer.Option(..., "--email"),
    is_admin: bool | None = typer.Option(None, "--isAdmin"),
    name: str = typer.Option(..., "--name"),
    notify: bool | None = typer.Option(None, "--notify"),
    password: str = typer.Option(..., "--password"),
    quota_size_in_bytes: int | None = typer.Option(None, "--quotaSizeInBytes"),
    should_change_password: bool | None = typer.Option(None, "--shouldChangePassword"),
    storage_label: str | None = typer.Option(None, "--storageLabel"),
) -> None:
    """Create a user

    Docs: https://api.immich.app/endpoints/users-admin/createUserAdmin
    """
    kwargs = {}
    has_flags = any(
        [
            avatar_color,
            email,
            is_admin,
            name,
            notify,
            password,
            quota_size_in_bytes,
            should_change_password,
            storage_label,
        ]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            avatar_color,
            email,
            is_admin,
            name,
            notify,
            password,
            quota_size_in_bytes,
            should_change_password,
            storage_label,
        ]
    ):
        json_data = {}
        if avatar_color is not None:
            set_nested(json_data, ["avatarColor"], avatar_color)
        set_nested(json_data, ["email"], email)
        if is_admin is not None:
            set_nested(json_data, ["isAdmin"], is_admin)
        set_nested(json_data, ["name"], name)
        if notify is not None:
            set_nested(json_data, ["notify"], notify)
        set_nested(json_data, ["password"], password)
        if quota_size_in_bytes is not None:
            set_nested(json_data, ["quotaSizeInBytes"], quota_size_in_bytes)
        if should_change_password is not None:
            set_nested(json_data, ["shouldChangePassword"], should_change_password)
        if storage_label is not None:
            set_nested(json_data, ["storageLabel"], storage_label)
        from immich.client.models.user_admin_create_dto import UserAdminCreateDto

        user_admin_create_dto = deserialize_request_body(json_data, UserAdminCreateDto)
        kwargs["user_admin_create_dto"] = user_admin_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "create_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-user-admin")
def delete_user_admin(
    ctx: typer.Context,
    id: str,
    force: bool | None = typer.Option(None, "--force"),
) -> None:
    """Delete a user

    Docs: https://api.immich.app/endpoints/users-admin/deleteUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([force])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            force,
        ]
    ):
        json_data = {}
        if force is not None:
            set_nested(json_data, ["force"], force)
        from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto

        user_admin_delete_dto = deserialize_request_body(json_data, UserAdminDeleteDto)
        kwargs["user_admin_delete_dto"] = user_admin_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "delete_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-admin")
def get_user_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a user

    Docs: https://api.immich.app/endpoints/users-admin/getUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "get_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-preferences-admin")
def get_user_preferences_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user preferences

    Docs: https://api.immich.app/endpoints/users-admin/getUserPreferencesAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(
        client, client.users_admin, "get_user_preferences_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-sessions-admin")
def get_user_sessions_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user sessions

    Docs: https://api.immich.app/endpoints/users-admin/getUserSessionsAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(
        client, client.users_admin, "get_user_sessions_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-statistics-admin")
def get_user_statistics_admin(
    ctx: typer.Context,
    id: str,
    is_favorite: str | None = typer.Option(None, "--is-favorite"),
    is_trashed: str | None = typer.Option(None, "--is-trashed"),
    visibility: str | None = typer.Option(None, "--visibility"),
) -> None:
    """Retrieve user statistics

    Docs: https://api.immich.app/endpoints/users-admin/getUserStatisticsAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if visibility is not None:
        kwargs["visibility"] = visibility
    client = ctx.obj["client"]
    result = run_command(
        client, client.users_admin, "get_user_statistics_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("restore-user-admin")
def restore_user_admin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Restore a deleted user

    Docs: https://api.immich.app/endpoints/users-admin/restoreUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "restore_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("search-users-admin")
def search_users_admin(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id"),
    with_deleted: str | None = typer.Option(None, "--with-deleted"),
) -> None:
    """Search users

    Docs: https://api.immich.app/endpoints/users-admin/searchUsersAdmin
    """
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    if with_deleted is not None:
        kwargs["with_deleted"] = with_deleted.lower() == "true"
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "search_users_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-user-admin")
def update_user_admin(
    ctx: typer.Context,
    id: str,
    avatar_color: str | None = typer.Option(None, "--avatarColor"),
    email: str | None = typer.Option(None, "--email"),
    is_admin: bool | None = typer.Option(None, "--isAdmin"),
    name: str | None = typer.Option(None, "--name"),
    password: str | None = typer.Option(None, "--password"),
    pin_code: str | None = typer.Option(None, "--pinCode"),
    quota_size_in_bytes: int | None = typer.Option(None, "--quotaSizeInBytes"),
    should_change_password: bool | None = typer.Option(None, "--shouldChangePassword"),
    storage_label: str | None = typer.Option(None, "--storageLabel"),
) -> None:
    """Update a user

    Docs: https://api.immich.app/endpoints/users-admin/updateUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any(
        [
            avatar_color,
            email,
            is_admin,
            name,
            password,
            pin_code,
            quota_size_in_bytes,
            should_change_password,
            storage_label,
        ]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            avatar_color,
            email,
            is_admin,
            name,
            password,
            pin_code,
            quota_size_in_bytes,
            should_change_password,
            storage_label,
        ]
    ):
        json_data = {}
        if avatar_color is not None:
            set_nested(json_data, ["avatarColor"], avatar_color)
        if email is not None:
            set_nested(json_data, ["email"], email)
        if is_admin is not None:
            set_nested(json_data, ["isAdmin"], is_admin)
        if name is not None:
            set_nested(json_data, ["name"], name)
        if password is not None:
            set_nested(json_data, ["password"], password)
        if pin_code is not None:
            set_nested(json_data, ["pinCode"], pin_code)
        if quota_size_in_bytes is not None:
            set_nested(json_data, ["quotaSizeInBytes"], quota_size_in_bytes)
        if should_change_password is not None:
            set_nested(json_data, ["shouldChangePassword"], should_change_password)
        if storage_label is not None:
            set_nested(json_data, ["storageLabel"], storage_label)
        from immich.client.models.user_admin_update_dto import UserAdminUpdateDto

        user_admin_update_dto = deserialize_request_body(json_data, UserAdminUpdateDto)
        kwargs["user_admin_update_dto"] = user_admin_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "update_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-user-preferences-admin")
def update_user_preferences_admin(
    ctx: typer.Context,
    id: str,
    albums_default_asset_order: str | None = typer.Option(
        None, "--albums.defaultAssetOrder"
    ),
    avatar_color: str | None = typer.Option(None, "--avatar.color"),
    cast_g_cast_enabled: bool | None = typer.Option(None, "--cast.gCastEnabled"),
    download_archive_size: int | None = typer.Option(None, "--download.archiveSize"),
    download_include_embedded_videos: bool | None = typer.Option(
        None, "--download.includeEmbeddedVideos"
    ),
    email_notifications_album_invite: bool | None = typer.Option(
        None, "--emailNotifications.albumInvite"
    ),
    email_notifications_album_update: bool | None = typer.Option(
        None, "--emailNotifications.albumUpdate"
    ),
    email_notifications_enabled: bool | None = typer.Option(
        None, "--emailNotifications.enabled"
    ),
    folders_enabled: bool | None = typer.Option(None, "--folders.enabled"),
    folders_sidebar_web: bool | None = typer.Option(None, "--folders.sidebarWeb"),
    memories_duration: int | None = typer.Option(None, "--memories.duration"),
    memories_enabled: bool | None = typer.Option(None, "--memories.enabled"),
    people_enabled: bool | None = typer.Option(None, "--people.enabled"),
    people_sidebar_web: bool | None = typer.Option(None, "--people.sidebarWeb"),
    purchase_hide_buy_button_until: str | None = typer.Option(
        None, "--purchase.hideBuyButtonUntil"
    ),
    purchase_show_support_badge: bool | None = typer.Option(
        None, "--purchase.showSupportBadge"
    ),
    ratings_enabled: bool | None = typer.Option(None, "--ratings.enabled"),
    shared_links_enabled: bool | None = typer.Option(None, "--sharedLinks.enabled"),
    shared_links_sidebar_web: bool | None = typer.Option(
        None, "--sharedLinks.sidebarWeb"
    ),
    tags_enabled: bool | None = typer.Option(None, "--tags.enabled"),
    tags_sidebar_web: bool | None = typer.Option(None, "--tags.sidebarWeb"),
) -> None:
    """Update user preferences

    Docs: https://api.immich.app/endpoints/users-admin/updateUserPreferencesAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any(
        [
            albums_default_asset_order,
            avatar_color,
            cast_g_cast_enabled,
            download_archive_size,
            download_include_embedded_videos,
            email_notifications_album_invite,
            email_notifications_album_update,
            email_notifications_enabled,
            folders_enabled,
            folders_sidebar_web,
            memories_duration,
            memories_enabled,
            people_enabled,
            people_sidebar_web,
            purchase_hide_buy_button_until,
            purchase_show_support_badge,
            ratings_enabled,
            shared_links_enabled,
            shared_links_sidebar_web,
            tags_enabled,
            tags_sidebar_web,
        ]
    )
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            albums_default_asset_order,
            avatar_color,
            cast_g_cast_enabled,
            download_archive_size,
            download_include_embedded_videos,
            email_notifications_album_invite,
            email_notifications_album_update,
            email_notifications_enabled,
            folders_enabled,
            folders_sidebar_web,
            memories_duration,
            memories_enabled,
            people_enabled,
            people_sidebar_web,
            purchase_hide_buy_button_until,
            purchase_show_support_badge,
            ratings_enabled,
            shared_links_enabled,
            shared_links_sidebar_web,
            tags_enabled,
            tags_sidebar_web,
        ]
    ):
        json_data = {}
        if albums_default_asset_order is not None:
            set_nested(
                json_data, ["albums", "defaultAssetOrder"], albums_default_asset_order
            )
        if avatar_color is not None:
            set_nested(json_data, ["avatar", "color"], avatar_color)
        if cast_g_cast_enabled is not None:
            set_nested(json_data, ["cast", "gCastEnabled"], cast_g_cast_enabled)
        if download_archive_size is not None:
            set_nested(json_data, ["download", "archiveSize"], download_archive_size)
        if download_include_embedded_videos is not None:
            set_nested(
                json_data,
                ["download", "includeEmbeddedVideos"],
                download_include_embedded_videos,
            )
        if email_notifications_album_invite is not None:
            set_nested(
                json_data,
                ["emailNotifications", "albumInvite"],
                email_notifications_album_invite,
            )
        if email_notifications_album_update is not None:
            set_nested(
                json_data,
                ["emailNotifications", "albumUpdate"],
                email_notifications_album_update,
            )
        if email_notifications_enabled is not None:
            set_nested(
                json_data,
                ["emailNotifications", "enabled"],
                email_notifications_enabled,
            )
        if folders_enabled is not None:
            set_nested(json_data, ["folders", "enabled"], folders_enabled)
        if folders_sidebar_web is not None:
            set_nested(json_data, ["folders", "sidebarWeb"], folders_sidebar_web)
        if memories_duration is not None:
            set_nested(json_data, ["memories", "duration"], memories_duration)
        if memories_enabled is not None:
            set_nested(json_data, ["memories", "enabled"], memories_enabled)
        if people_enabled is not None:
            set_nested(json_data, ["people", "enabled"], people_enabled)
        if people_sidebar_web is not None:
            set_nested(json_data, ["people", "sidebarWeb"], people_sidebar_web)
        if purchase_hide_buy_button_until is not None:
            set_nested(
                json_data,
                ["purchase", "hideBuyButtonUntil"],
                purchase_hide_buy_button_until,
            )
        if purchase_show_support_badge is not None:
            set_nested(
                json_data, ["purchase", "showSupportBadge"], purchase_show_support_badge
            )
        if ratings_enabled is not None:
            set_nested(json_data, ["ratings", "enabled"], ratings_enabled)
        if shared_links_enabled is not None:
            set_nested(json_data, ["sharedLinks", "enabled"], shared_links_enabled)
        if shared_links_sidebar_web is not None:
            set_nested(
                json_data, ["sharedLinks", "sidebarWeb"], shared_links_sidebar_web
            )
        if tags_enabled is not None:
            set_nested(json_data, ["tags", "enabled"], tags_enabled)
        if tags_sidebar_web is not None:
            set_nested(json_data, ["tags", "sidebarWeb"], tags_sidebar_web)
        from immich.client.models.user_preferences_update_dto import (
            UserPreferencesUpdateDto,
        )

        user_preferences_update_dto = deserialize_request_body(
            json_data, UserPreferencesUpdateDto
        )
        kwargs["user_preferences_update_dto"] = user_preferences_update_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.users_admin, "update_user_preferences_admin", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
