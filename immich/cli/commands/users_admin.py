"""Generated CLI commands for Users (admin) tag (auto-generated, do not edit)."""

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
    help="""Administrative endpoints for managing users, including creating, updating, deleting, and restoring users. Also includes endpoints for resetting passwords and PIN codes.

Docs: https://api.immich.app/endpoints/users-admin""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-user-admin")
def create_user_admin(
    ctx: typer.Context,
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    avatar_color: str | None = typer.Option(
        None, "--avatarColor", help="""Avatar color"""
    ),
    email: str = typer.Option(..., "--email", help="""User email"""),
    is_admin: bool | None = typer.Option(
        None, "--isAdmin", help="""Grant admin privileges"""
    ),
    name: str = typer.Option(..., "--name", help="""User name"""),
    notify: bool | None = typer.Option(
        None, "--notify", help="""Send notification email"""
    ),
    password: str = typer.Option(..., "--password", help="""User password"""),
    quota_size_in_bytes: int | None = typer.Option(
        None, "--quotaSizeInBytes", help="""Storage quota in bytes"""
    ),
    should_change_password: bool | None = typer.Option(
        None, "--shouldChangePassword", help="""Require password change on next login"""
    ),
    storage_label: str | None = typer.Option(
        None, "--storageLabel", help="""Storage label"""
    ),
) -> None:
    """Create a user

    Docs: https://api.immich.app/endpoints/users-admin/createUserAdmin
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
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
        from immich.client.models.user_admin_create_dto import UserAdminCreateDto

        user_admin_create_dto = deserialize_request_body(json_data, UserAdminCreateDto)
        kwargs["user_admin_create_dto"] = user_admin_create_dto
    elif any(
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
        # Build body from dotted flags
        json_data = {}
        if avatar_color is not None:
            set_nested(json_data, ["avatarColor"], avatar_color)
        if email is None:
            raise SystemExit("Error: --email is required")
        set_nested(json_data, ["email"], email)
        if is_admin is not None:
            set_nested(json_data, ["isAdmin"], is_admin)
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ["name"], name)
        if notify is not None:
            set_nested(json_data, ["notify"], notify)
        if password is None:
            raise SystemExit("Error: --password is required")
        set_nested(json_data, ["password"], password)
        if quota_size_in_bytes is not None:
            set_nested(json_data, ["quotaSizeInBytes"], quota_size_in_bytes)
        if should_change_password is not None:
            set_nested(json_data, ["shouldChangePassword"], should_change_password)
        if storage_label is not None:
            set_nested(json_data, ["storageLabel"], storage_label)
        if json_data:
            from immich.client.models.user_admin_create_dto import UserAdminCreateDto

            user_admin_create_dto = deserialize_request_body(
                json_data, UserAdminCreateDto
            )
            kwargs["user_admin_create_dto"] = user_admin_create_dto
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "create_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-user-admin")
def delete_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    force: bool | None = typer.Option(
        None, "--force", help="""Force delete even if user has assets"""
    ),
) -> None:
    """Delete a user

    Docs: https://api.immich.app/endpoints/users-admin/deleteUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([force])
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
        from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto

        user_admin_delete_dto = deserialize_request_body(json_data, UserAdminDeleteDto)
        kwargs["user_admin_delete_dto"] = user_admin_delete_dto
    elif any(
        [
            force,
        ]
    ):
        # Build body from dotted flags
        json_data = {}
        if force is not None:
            set_nested(json_data, ["force"], force)
        if json_data:
            from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto

            user_admin_delete_dto = deserialize_request_body(
                json_data, UserAdminDeleteDto
            )
            kwargs["user_admin_delete_dto"] = user_admin_delete_dto
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "delete_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-admin")
def get_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Retrieve a user

    Docs: https://api.immich.app/endpoints/users-admin/getUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "get_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-preferences-admin")
def get_user_preferences_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Retrieve user preferences

    Docs: https://api.immich.app/endpoints/users-admin/getUserPreferencesAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "get_user_preferences_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-sessions-admin")
def get_user_sessions_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Retrieve user sessions

    Docs: https://api.immich.app/endpoints/users-admin/getUserSessionsAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "get_user_sessions_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-statistics-admin")
def get_user_statistics_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
    is_favorite: bool | None = typer.Option(
        None, "--is-favorite", help="""Filter by favorite status"""
    ),
    is_trashed: bool | None = typer.Option(
        None, "--is-trashed", help="""Filter by trash status"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help="""Filter by visibility"""
    ),
) -> None:
    """Retrieve user statistics

    Docs: https://api.immich.app/endpoints/users-admin/getUserStatisticsAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed
    if visibility is not None:
        kwargs["visibility"] = visibility
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "get_user_statistics_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("restore-user-admin")
def restore_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Restore a deleted user

    Docs: https://api.immich.app/endpoints/users-admin/restoreUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "restore_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("search-users-admin")
def search_users_admin(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id", help="""User ID filter"""),
    with_deleted: bool | None = typer.Option(
        None, "--with-deleted", help="""Include deleted users"""
    ),
) -> None:
    """Search users

    Docs: https://api.immich.app/endpoints/users-admin/searchUsersAdmin
    """
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    if with_deleted is not None:
        kwargs["with_deleted"] = with_deleted
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "search_users_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-user-admin")
def update_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    avatar_color: str | None = typer.Option(
        None, "--avatarColor", help="""Avatar color"""
    ),
    email: str | None = typer.Option(None, "--email", help="""User email"""),
    is_admin: bool | None = typer.Option(
        None, "--isAdmin", help="""Grant admin privileges"""
    ),
    name: str | None = typer.Option(None, "--name", help="""User name"""),
    password: str | None = typer.Option(None, "--password", help="""User password"""),
    pin_code: str | None = typer.Option(None, "--pinCode", help="""PIN code"""),
    quota_size_in_bytes: int | None = typer.Option(
        None, "--quotaSizeInBytes", help="""Storage quota in bytes"""
    ),
    should_change_password: bool | None = typer.Option(
        None, "--shouldChangePassword", help="""Require password change on next login"""
    ),
    storage_label: str | None = typer.Option(
        None, "--storageLabel", help="""Storage label"""
    ),
) -> None:
    """Update a user

    Docs: https://api.immich.app/endpoints/users-admin/updateUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
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
        from immich.client.models.user_admin_update_dto import UserAdminUpdateDto

        user_admin_update_dto = deserialize_request_body(json_data, UserAdminUpdateDto)
        kwargs["user_admin_update_dto"] = user_admin_update_dto
    elif any(
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
        # Build body from dotted flags
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
        if json_data:
            from immich.client.models.user_admin_update_dto import UserAdminUpdateDto

            user_admin_update_dto = deserialize_request_body(
                json_data, UserAdminUpdateDto
            )
            kwargs["user_admin_update_dto"] = user_admin_update_dto
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "update_user_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-user-preferences-admin")
def update_user_preferences_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
    json_str: str | None = typer.Option(
        None, "--json", help="Inline JSON request body"
    ),
    albums_default_asset_order: str | None = typer.Option(
        None, "--albums.defaultAssetOrder", help="""Asset sort order"""
    ),
    avatar_color: str | None = typer.Option(
        None, "--avatar.color", help="""Avatar color"""
    ),
    cast_g_cast_enabled: bool | None = typer.Option(
        None, "--cast.gCastEnabled", help="""Whether Google Cast is enabled"""
    ),
    download_archive_size: int | None = typer.Option(
        None, "--download.archiveSize", help="""Maximum archive size in bytes"""
    ),
    download_include_embedded_videos: bool | None = typer.Option(
        None,
        "--download.includeEmbeddedVideos",
        help="""Whether to include embedded videos in downloads""",
    ),
    email_notifications_album_invite: bool | None = typer.Option(
        None,
        "--emailNotifications.albumInvite",
        help="""Whether to receive email notifications for album invites""",
    ),
    email_notifications_album_update: bool | None = typer.Option(
        None,
        "--emailNotifications.albumUpdate",
        help="""Whether to receive email notifications for album updates""",
    ),
    email_notifications_enabled: bool | None = typer.Option(
        None,
        "--emailNotifications.enabled",
        help="""Whether email notifications are enabled""",
    ),
    folders_enabled: bool | None = typer.Option(
        None, "--folders.enabled", help="""Whether folders are enabled"""
    ),
    folders_sidebar_web: bool | None = typer.Option(
        None, "--folders.sidebarWeb", help="""Whether folders appear in web sidebar"""
    ),
    memories_duration: int | None = typer.Option(
        None, "--memories.duration", help="""Memory duration in seconds"""
    ),
    memories_enabled: bool | None = typer.Option(
        None, "--memories.enabled", help="""Whether memories are enabled"""
    ),
    people_enabled: bool | None = typer.Option(
        None, "--people.enabled", help="""Whether people are enabled"""
    ),
    people_sidebar_web: bool | None = typer.Option(
        None, "--people.sidebarWeb", help="""Whether people appear in web sidebar"""
    ),
    purchase_hide_buy_button_until: str | None = typer.Option(
        None,
        "--purchase.hideBuyButtonUntil",
        help="""Date until which to hide buy button""",
    ),
    purchase_show_support_badge: bool | None = typer.Option(
        None, "--purchase.showSupportBadge", help="""Whether to show support badge"""
    ),
    ratings_enabled: bool | None = typer.Option(
        None, "--ratings.enabled", help="""Whether ratings are enabled"""
    ),
    shared_links_enabled: bool | None = typer.Option(
        None, "--sharedLinks.enabled", help="""Whether shared links are enabled"""
    ),
    shared_links_sidebar_web: bool | None = typer.Option(
        None,
        "--sharedLinks.sidebarWeb",
        help="""Whether shared links appear in web sidebar""",
    ),
    tags_enabled: bool | None = typer.Option(
        None, "--tags.enabled", help="""Whether tags are enabled"""
    ),
    tags_sidebar_web: bool | None = typer.Option(
        None, "--tags.sidebarWeb", help="""Whether tags appear in web sidebar"""
    ),
) -> None:
    """Update user preferences

    Docs: https://api.immich.app/endpoints/users-admin/updateUserPreferencesAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
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
        from immich.client.models.user_preferences_update_dto import (
            UserPreferencesUpdateDto,
        )

        user_preferences_update_dto = deserialize_request_body(
            json_data, UserPreferencesUpdateDto
        )
        kwargs["user_preferences_update_dto"] = user_preferences_update_dto
    elif any(
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
        # Build body from dotted flags
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
        if json_data:
            from immich.client.models.user_preferences_update_dto import (
                UserPreferencesUpdateDto,
            )

            user_preferences_update_dto = deserialize_request_body(
                json_data, UserPreferencesUpdateDto
            )
            kwargs["user_preferences_update_dto"] = user_preferences_update_dto
    client = ctx.obj["client"]
    api_group = client.users_admin
    result = run_command(client, api_group, "update_user_preferences_admin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
