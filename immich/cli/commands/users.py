"""Generated CLI commands for Users tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from pathlib import Path
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.\n\n[link=https://api.immich.app/endpoints/users]Immich API documentation[/link]"""
)


@app.command("create-profile-image", deprecated=False, rich_help_panel="API commands")
def create_profile_image(
    ctx: typer.Context,
    file: Path = typer.Option(..., "--file", help="""""", exists=True),
) -> None:
    """Create user profile image

    [link=https://api.immich.app/endpoints/users/createProfileImage]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["file"] = (file.name, file.read_bytes())
    kwargs.update(json_data)
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "create_profile_image", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-profile-image", deprecated=False, rich_help_panel="API commands")
def delete_profile_image(
    ctx: typer.Context,
) -> None:
    """Delete user profile image

    [link=https://api.immich.app/endpoints/users/deleteProfileImage]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "delete_profile_image", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-user-license", deprecated=False, rich_help_panel="API commands")
def delete_user_license(
    ctx: typer.Context,
) -> None:
    """Delete user product key

    [link=https://api.immich.app/endpoints/users/deleteUserLicense]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "delete_user_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-user-onboarding", deprecated=False, rich_help_panel="API commands")
def delete_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Delete user onboarding

    [link=https://api.immich.app/endpoints/users/deleteUserOnboarding]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "delete_user_onboarding", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-my-preferences", deprecated=False, rich_help_panel="API commands")
def get_my_preferences(
    ctx: typer.Context,
) -> None:
    """Get my preferences

    [link=https://api.immich.app/endpoints/users/getMyPreferences]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_my_preferences", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-my-user", deprecated=False, rich_help_panel="API commands")
def get_my_user(
    ctx: typer.Context,
) -> None:
    """Get current user

    [link=https://api.immich.app/endpoints/users/getMyUser]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_my_user", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-profile-image", deprecated=False, rich_help_panel="API commands")
def get_profile_image(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve user profile image

    [link=https://api.immich.app/endpoints/users/getProfileImage]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_profile_image", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-user", deprecated=False, rich_help_panel="API commands")
def get_user(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a user

    [link=https://api.immich.app/endpoints/users/getUser]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_user", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-user-license", deprecated=False, rich_help_panel="API commands")
def get_user_license(
    ctx: typer.Context,
) -> None:
    """Retrieve user product key

    [link=https://api.immich.app/endpoints/users/getUserLicense]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_user_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-user-onboarding", deprecated=False, rich_help_panel="API commands")
def get_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve user onboarding

    [link=https://api.immich.app/endpoints/users/getUserOnboarding]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "get_user_onboarding", ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-users", deprecated=False, rich_help_panel="API commands")
def search_users(
    ctx: typer.Context,
) -> None:
    """Get all users

    [link=https://api.immich.app/endpoints/users/searchUsers]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "search_users", ctx, **kwargs)
    print_response(result, ctx)


@app.command("set-user-license", deprecated=False, rich_help_panel="API commands")
def set_user_license(
    ctx: typer.Context,
    activation_key: str = typer.Option(..., "--activation-key", help=""""""),
    license_key: str = typer.Option(..., "--license-key", help=""""""),
) -> None:
    """Set user product key

    [link=https://api.immich.app/endpoints/users/setUserLicense]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["activation_key"], activation_key)
    set_nested(json_data, ["license_key"], license_key)
    license_key_dto = LicenseKeyDto.model_validate(json_data)
    kwargs["license_key_dto"] = license_key_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "set_user_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("set-user-onboarding", deprecated=False, rich_help_panel="API commands")
def set_user_onboarding(
    ctx: typer.Context,
    is_onboarded: bool = typer.Option(..., "--is-onboarded", help=""""""),
) -> None:
    """Update user onboarding

    [link=https://api.immich.app/endpoints/users/setUserOnboarding]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["is_onboarded"], is_onboarded)
    onboarding_dto = OnboardingDto.model_validate(json_data)
    kwargs["onboarding_dto"] = onboarding_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "set_user_onboarding", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-my-preferences", deprecated=False, rich_help_panel="API commands")
def update_my_preferences(
    ctx: typer.Context,
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
    """Update my preferences

    [link=https://api.immich.app/endpoints/users/updateMyPreferences]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
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
    user_preferences_update_dto = UserPreferencesUpdateDto.model_validate(json_data)
    kwargs["user_preferences_update_dto"] = user_preferences_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "update_my_preferences", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-my-user", deprecated=False, rich_help_panel="API commands")
def update_my_user(
    ctx: typer.Context,
    avatar_color: str | None = typer.Option(None, "--avatar-color", help=""""""),
    email: str | None = typer.Option(None, "--email", help=""""""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    password: str | None = typer.Option(None, "--password", help=""""""),
) -> None:
    """Update current user

    [link=https://api.immich.app/endpoints/users/updateMyUser]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if avatar_color is not None:
        set_nested(json_data, ["avatar_color"], avatar_color)
    if email is not None:
        set_nested(json_data, ["email"], email)
    if name is not None:
        set_nested(json_data, ["name"], name)
    if password is not None:
        set_nested(json_data, ["password"], password)
    user_update_me_dto = UserUpdateMeDto.model_validate(json_data)
    kwargs["user_update_me_dto"] = user_update_me_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.users, "update_my_user", ctx, **kwargs)
    print_response(result, ctx)
