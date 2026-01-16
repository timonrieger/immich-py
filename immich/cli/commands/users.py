"""Generated CLI commands for Users tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer

from immich.cli.runtime import (
    load_file_bytes,
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.

Docs: https://api.immich.app/endpoints/users""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-profile-image")
def create_profile_image(
    ctx: typer.Context,
    file: Path = typer.Option(..., "--file", help="File to upload for file"),
) -> None:
    """Create user profile image

    Docs: https://api.immich.app/endpoints/users/createProfileImage
    """
    kwargs = {}
    json_data = {}  # noqa: F841
    missing: list[str] = []
    kwargs["file"] = load_file_bytes(file)
    if missing:
        raise SystemExit(
            "Error: missing required multipart fields: "
            + ", ".join(missing)
            + ". Provide them via file options."
        )
    client = ctx.obj["client"]
    result = run_command(client, client.users, "create_profile_image", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-profile-image")
def delete_profile_image(
    ctx: typer.Context,
) -> None:
    """Delete user profile image

    Docs: https://api.immich.app/endpoints/users/deleteProfileImage
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "delete_profile_image", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-user-license")
def delete_user_license(
    ctx: typer.Context,
) -> None:
    """Delete user product key

    Docs: https://api.immich.app/endpoints/users/deleteUserLicense
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "delete_user_license", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-user-onboarding")
def delete_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Delete user onboarding

    Docs: https://api.immich.app/endpoints/users/deleteUserOnboarding
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "delete_user_onboarding", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-my-preferences")
def get_my_preferences(
    ctx: typer.Context,
) -> None:
    """Get my preferences

    Docs: https://api.immich.app/endpoints/users/getMyPreferences
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_my_preferences", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-my-user")
def get_my_user(
    ctx: typer.Context,
) -> None:
    """Get current user

    Docs: https://api.immich.app/endpoints/users/getMyUser
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_my_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-profile-image")
def get_profile_image(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve user profile image

    Docs: https://api.immich.app/endpoints/users/getProfileImage
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_profile_image", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user")
def get_user(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a user

    Docs: https://api.immich.app/endpoints/users/getUser
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-license")
def get_user_license(
    ctx: typer.Context,
) -> None:
    """Retrieve user product key

    Docs: https://api.immich.app/endpoints/users/getUserLicense
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_user_license", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-user-onboarding")
def get_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve user onboarding

    Docs: https://api.immich.app/endpoints/users/getUserOnboarding
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_user_onboarding", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("search-users")
def search_users(
    ctx: typer.Context,
) -> None:
    """Get all users

    Docs: https://api.immich.app/endpoints/users/searchUsers
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.users, "search_users", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("set-user-license")
def set_user_license(
    ctx: typer.Context,
    activation_key: str = typer.Option(..., "--activationKey"),
    license_key: str = typer.Option(..., "--licenseKey"),
) -> None:
    """Set user product key

    Docs: https://api.immich.app/endpoints/users/setUserLicense
    """
    kwargs = {}
    has_flags = any([activation_key, license_key])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            activation_key,
            license_key,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["activationKey"], activation_key)
        set_nested(json_data, ["licenseKey"], license_key)
        from immich.client.models.license_key_dto import LicenseKeyDto

        license_key_dto = deserialize_request_body(json_data, LicenseKeyDto)
        kwargs["license_key_dto"] = license_key_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users, "set_user_license", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("set-user-onboarding")
def set_user_onboarding(
    ctx: typer.Context,
    is_onboarded: bool = typer.Option(..., "--isOnboarded"),
) -> None:
    """Update user onboarding

    Docs: https://api.immich.app/endpoints/users/setUserOnboarding
    """
    kwargs = {}
    has_flags = any([is_onboarded])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            is_onboarded,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["isOnboarded"], is_onboarded)
        from immich.client.models.onboarding_dto import OnboardingDto

        onboarding_dto = deserialize_request_body(json_data, OnboardingDto)
        kwargs["onboarding_dto"] = onboarding_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users, "set_user_onboarding", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-my-preferences")
def update_my_preferences(
    ctx: typer.Context,
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
    """Update my preferences

    Docs: https://api.immich.app/endpoints/users/updateMyPreferences
    """
    kwargs = {}
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
    result = run_command(client, client.users, "update_my_preferences", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-my-user")
def update_my_user(
    ctx: typer.Context,
    avatar_color: str | None = typer.Option(None, "--avatarColor"),
    email: str | None = typer.Option(None, "--email"),
    name: str | None = typer.Option(None, "--name"),
    password: str | None = typer.Option(None, "--password"),
) -> None:
    """Update current user

    Docs: https://api.immich.app/endpoints/users/updateMyUser
    """
    kwargs = {}
    has_flags = any([avatar_color, email, name, password])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            avatar_color,
            email,
            name,
            password,
        ]
    ):
        json_data = {}
        if avatar_color is not None:
            set_nested(json_data, ["avatarColor"], avatar_color)
        if email is not None:
            set_nested(json_data, ["email"], email)
        if name is not None:
            set_nested(json_data, ["name"], name)
        if password is not None:
            set_nested(json_data, ["password"], password)
        from immich.client.models.user_update_me_dto import UserUpdateMeDto

        user_update_me_dto = deserialize_request_body(json_data, UserUpdateMeDto)
        kwargs["user_update_me_dto"] = user_update_me_dto
    client = ctx.obj["client"]
    result = run_command(client, client.users, "update_my_user", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
