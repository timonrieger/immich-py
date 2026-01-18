"""Generated CLI commands for Users (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Administrative endpoints for managing users, including creating, updating, deleting, and restoring users. Also includes endpoints for resetting passwords and PIN codes.\n\nDocs: https://api.immich.app/endpoints/users-admin"""
)


@app.command("create-user-admin", deprecated=False)
def create_user_admin(
    ctx: typer.Context,
    avatar_color: str | None = typer.Option(None, "--avatar-color", help=""""""),
    email: str = typer.Option(..., "--email", help=""""""),
    is_admin: Literal["true", "false"] | None = typer.Option(
        None, "--is-admin", help=""""""
    ),
    name: str = typer.Option(..., "--name", help=""""""),
    notify: Literal["true", "false"] | None = typer.Option(
        None, "--notify", help=""""""
    ),
    password: str = typer.Option(..., "--password", help=""""""),
    quota_size_in_bytes: int | None = typer.Option(
        None, "--quota-size-in-bytes", help="""""", min=0
    ),
    should_change_password: Literal["true", "false"] | None = typer.Option(
        None, "--should-change-password", help=""""""
    ),
    storage_label: str | None = typer.Option(None, "--storage-label", help=""""""),
) -> None:
    """Create a user

    Docs: https://api.immich.app/endpoints/users-admin/createUserAdmin
    """
    kwargs = {}
    json_data = {}
    if avatar_color is not None:
        set_nested(json_data, ["avatar_color"], avatar_color)
    set_nested(json_data, ["email"], email)
    if is_admin is not None:
        set_nested(json_data, ["is_admin"], is_admin.lower() == "true")
    set_nested(json_data, ["name"], name)
    if notify is not None:
        set_nested(json_data, ["notify"], notify.lower() == "true")
    set_nested(json_data, ["password"], password)
    if quota_size_in_bytes is not None:
        set_nested(json_data, ["quota_size_in_bytes"], quota_size_in_bytes)
    if should_change_password is not None:
        set_nested(
            json_data,
            ["should_change_password"],
            should_change_password.lower() == "true",
        )
    if storage_label is not None:
        set_nested(json_data, ["storage_label"], storage_label)
    from immich.client.models.user_admin_create_dto import UserAdminCreateDto

    user_admin_create_dto = UserAdminCreateDto.model_validate(json_data)
    kwargs["user_admin_create_dto"] = user_admin_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "create_user_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("delete-user-admin", deprecated=False)
def delete_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    force: Literal["true", "false"] | None = typer.Option(None, "--force", help=""""""),
) -> None:
    """Delete a user

    Docs: https://api.immich.app/endpoints/users-admin/deleteUserAdmin
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    from immich.client.models.user_admin_delete_dto import UserAdminDeleteDto

    user_admin_delete_dto = UserAdminDeleteDto.model_validate(json_data)
    kwargs["user_admin_delete_dto"] = user_admin_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "delete_user_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-user-admin", deprecated=False)
def get_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a user

    Docs: https://api.immich.app/endpoints/users-admin/getUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "get_user_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-user-preferences-admin", deprecated=False)
def get_user_preferences_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
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
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-user-sessions-admin", deprecated=False)
def get_user_sessions_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
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
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-user-statistics-admin", deprecated=False)
def get_user_statistics_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=""""""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help=""""""
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=""""""
    ),
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
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("restore-user-admin", deprecated=False)
def restore_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Restore a deleted user

    Docs: https://api.immich.app/endpoints/users-admin/restoreUserAdmin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "restore_user_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("search-users-admin", deprecated=False)
def search_users_admin(
    ctx: typer.Context,
    id: str | None = typer.Option(None, "--id", help=""""""),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help=""""""
    ),
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
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-user-admin", deprecated=False)
def update_user_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    avatar_color: str | None = typer.Option(None, "--avatar-color", help=""""""),
    email: str | None = typer.Option(None, "--email", help=""""""),
    is_admin: Literal["true", "false"] | None = typer.Option(
        None, "--is-admin", help=""""""
    ),
    name: str | None = typer.Option(None, "--name", help=""""""),
    password: str | None = typer.Option(None, "--password", help=""""""),
    pin_code: str | None = typer.Option(None, "--pin-code", help="""Example: 123456"""),
    quota_size_in_bytes: int | None = typer.Option(
        None, "--quota-size-in-bytes", help="""""", min=0
    ),
    should_change_password: Literal["true", "false"] | None = typer.Option(
        None, "--should-change-password", help=""""""
    ),
    storage_label: str | None = typer.Option(None, "--storage-label", help=""""""),
) -> None:
    """Update a user

    Docs: https://api.immich.app/endpoints/users-admin/updateUserAdmin
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if avatar_color is not None:
        set_nested(json_data, ["avatar_color"], avatar_color)
    if email is not None:
        set_nested(json_data, ["email"], email)
    if is_admin is not None:
        set_nested(json_data, ["is_admin"], is_admin.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if pin_code is not None:
        set_nested(json_data, ["pin_code"], pin_code)
    if quota_size_in_bytes is not None:
        set_nested(json_data, ["quota_size_in_bytes"], quota_size_in_bytes)
    if should_change_password is not None:
        set_nested(
            json_data,
            ["should_change_password"],
            should_change_password.lower() == "true",
        )
    if storage_label is not None:
        set_nested(json_data, ["storage_label"], storage_label)
    from immich.client.models.user_admin_update_dto import UserAdminUpdateDto

    user_admin_update_dto = UserAdminUpdateDto.model_validate(json_data)
    kwargs["user_admin_update_dto"] = user_admin_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users_admin, "update_user_admin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-user-preferences-admin", deprecated=False)
def update_user_preferences_admin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    albums_default_asset_order: str | None = typer.Option(
        None, "--albums-default-asset-order", help=""""""
    ),
    avatar_color: str | None = typer.Option(None, "--avatar-color", help=""""""),
    cast_g_cast_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--cast-g-cast-enabled", help=""""""
    ),
    download_archive_size: int | None = typer.Option(
        None, "--download-archive-size", help="""""", min=1
    ),
    download_include_embedded_videos: Literal["true", "false"] | None = typer.Option(
        None, "--download-include-embedded-videos", help=""""""
    ),
    email_notifications_album_invite: Literal["true", "false"] | None = typer.Option(
        None, "--email-notifications-album-invite", help=""""""
    ),
    email_notifications_album_update: Literal["true", "false"] | None = typer.Option(
        None, "--email-notifications-album-update", help=""""""
    ),
    email_notifications_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--email-notifications-enabled", help=""""""
    ),
    folders_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--folders-enabled", help=""""""
    ),
    folders_sidebar_web: Literal["true", "false"] | None = typer.Option(
        None, "--folders-sidebar-web", help=""""""
    ),
    memories_duration: int | None = typer.Option(
        None, "--memories-duration", help="""""", min=1
    ),
    memories_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--memories-enabled", help=""""""
    ),
    people_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--people-enabled", help=""""""
    ),
    people_sidebar_web: Literal["true", "false"] | None = typer.Option(
        None, "--people-sidebar-web", help=""""""
    ),
    purchase_hide_buy_button_until: str | None = typer.Option(
        None, "--purchase-hide-buy-button-until", help=""""""
    ),
    purchase_show_support_badge: Literal["true", "false"] | None = typer.Option(
        None, "--purchase-show-support-badge", help=""""""
    ),
    ratings_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--ratings-enabled", help=""""""
    ),
    shared_links_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--shared-links-enabled", help=""""""
    ),
    shared_links_sidebar_web: Literal["true", "false"] | None = typer.Option(
        None, "--shared-links-sidebar-web", help=""""""
    ),
    tags_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--tags-enabled", help=""""""
    ),
    tags_sidebar_web: Literal["true", "false"] | None = typer.Option(
        None, "--tags-sidebar-web", help=""""""
    ),
) -> None:
    """Update user preferences

    Docs: https://api.immich.app/endpoints/users-admin/updateUserPreferencesAdmin
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if albums_default_asset_order is not None:
        set_nested(
            json_data, ["albums_default_asset_order"], albums_default_asset_order
        )
    if avatar_color is not None:
        set_nested(json_data, ["avatar_color"], avatar_color)
    if cast_g_cast_enabled is not None:
        set_nested(
            json_data, ["cast_g_cast_enabled"], cast_g_cast_enabled.lower() == "true"
        )
    if download_archive_size is not None:
        set_nested(json_data, ["download_archive_size"], download_archive_size)
    if download_include_embedded_videos is not None:
        set_nested(
            json_data,
            ["download_include_embedded_videos"],
            download_include_embedded_videos.lower() == "true",
        )
    if email_notifications_album_invite is not None:
        set_nested(
            json_data,
            ["email_notifications_album_invite"],
            email_notifications_album_invite.lower() == "true",
        )
    if email_notifications_album_update is not None:
        set_nested(
            json_data,
            ["email_notifications_album_update"],
            email_notifications_album_update.lower() == "true",
        )
    if email_notifications_enabled is not None:
        set_nested(
            json_data,
            ["email_notifications_enabled"],
            email_notifications_enabled.lower() == "true",
        )
    if folders_enabled is not None:
        set_nested(json_data, ["folders_enabled"], folders_enabled.lower() == "true")
    if folders_sidebar_web is not None:
        set_nested(
            json_data, ["folders_sidebar_web"], folders_sidebar_web.lower() == "true"
        )
    if memories_duration is not None:
        set_nested(json_data, ["memories_duration"], memories_duration)
    if memories_enabled is not None:
        set_nested(json_data, ["memories_enabled"], memories_enabled.lower() == "true")
    if people_enabled is not None:
        set_nested(json_data, ["people_enabled"], people_enabled.lower() == "true")
    if people_sidebar_web is not None:
        set_nested(
            json_data, ["people_sidebar_web"], people_sidebar_web.lower() == "true"
        )
    if purchase_hide_buy_button_until is not None:
        set_nested(
            json_data,
            ["purchase_hide_buy_button_until"],
            purchase_hide_buy_button_until,
        )
    if purchase_show_support_badge is not None:
        set_nested(
            json_data,
            ["purchase_show_support_badge"],
            purchase_show_support_badge.lower() == "true",
        )
    if ratings_enabled is not None:
        set_nested(json_data, ["ratings_enabled"], ratings_enabled.lower() == "true")
    if shared_links_enabled is not None:
        set_nested(
            json_data, ["shared_links_enabled"], shared_links_enabled.lower() == "true"
        )
    if shared_links_sidebar_web is not None:
        set_nested(
            json_data,
            ["shared_links_sidebar_web"],
            shared_links_sidebar_web.lower() == "true",
        )
    if tags_enabled is not None:
        set_nested(json_data, ["tags_enabled"], tags_enabled.lower() == "true")
    if tags_sidebar_web is not None:
        set_nested(json_data, ["tags_sidebar_web"], tags_sidebar_web.lower() == "true")
    from immich.client.models.user_preferences_update_dto import (
        UserPreferencesUpdateDto,
    )

    user_preferences_update_dto = UserPreferencesUpdateDto.model_validate(json_data)
    kwargs["user_preferences_update_dto"] = user_preferences_update_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.users_admin, "update_user_preferences_admin", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
