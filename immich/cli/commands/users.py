"""Generated CLI commands for Users tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.

Docs: https://api.immich.app/endpoints/users""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-profile-image")
def create_profile_image(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON with multipart fields (non-file)"),
    file: Path = typer.Option(..., "--file", help="""Profile image file"""),
) -> None:
    """Create user profile image

Docs: https://api.immich.app/endpoints/users/createProfileImage
    """
    kwargs = {}
    json_data = json.loads(json_str) if json_str is not None else {}
    missing: list[str] = []
    kwargs['file'] = load_file_bytes(file)
    if missing:
        raise SystemExit("Error: missing required multipart fields: " + ', '.join(missing) + ". Provide them via --json and/or file options.")
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'create_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-profile-image")
def delete_profile_image(
    ctx: typer.Context,
) -> None:
    """Delete user profile image

Docs: https://api.immich.app/endpoints/users/deleteProfileImage
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-user-license")
def delete_user_license(
    ctx: typer.Context,
) -> None:
    """Delete user product key

Docs: https://api.immich.app/endpoints/users/deleteUserLicense
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("delete-user-onboarding")
def delete_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Delete user onboarding

Docs: https://api.immich.app/endpoints/users/deleteUserOnboarding
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'delete_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-preferences")
def get_my_preferences(
    ctx: typer.Context,
) -> None:
    """Get my preferences

Docs: https://api.immich.app/endpoints/users/getMyPreferences
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_my_preferences', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-my-user")
def get_my_user(
    ctx: typer.Context,
) -> None:
    """Get current user

Docs: https://api.immich.app/endpoints/users/getMyUser
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-profile-image")
def get_profile_image(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Retrieve user profile image

Docs: https://api.immich.app/endpoints/users/getProfileImage
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_profile_image', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user")
def get_user(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="""User ID"""),
) -> None:
    """Retrieve a user

Docs: https://api.immich.app/endpoints/users/getUser
    """
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-license")
def get_user_license(
    ctx: typer.Context,
) -> None:
    """Retrieve user product key

Docs: https://api.immich.app/endpoints/users/getUserLicense
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-user-onboarding")
def get_user_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve user onboarding

Docs: https://api.immich.app/endpoints/users/getUserOnboarding
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'get_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("search-users")
def search_users(
    ctx: typer.Context,
) -> None:
    """Get all users

Docs: https://api.immich.app/endpoints/users/searchUsers
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'search_users', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-user-license")
def set_user_license(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    activation_key: str = typer.Option(..., "--activationKey", help="""Activation key"""),
    license_key: str = typer.Option(..., "--licenseKey", help="""License key (format: IM(SV|CL)(-XXXX){8})"""),
) -> None:
    """Set user product key

Docs: https://api.immich.app/endpoints/users/setUserLicense
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([activation_key, license_key])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.license_key_dto import LicenseKeyDto
        license_key_dto = deserialize_request_body(json_data, LicenseKeyDto)
        kwargs['license_key_dto'] = license_key_dto
    elif any([
        activation_key,
        license_key,
    ]):
        # Build body from dotted flags
        json_data = {}
        if activation_key is None:
            raise SystemExit("Error: --activationKey is required")
        set_nested(json_data, ['activationKey'], activation_key)
        if license_key is None:
            raise SystemExit("Error: --licenseKey is required")
        set_nested(json_data, ['licenseKey'], license_key)
        if json_data:
            from immich.client.models.license_key_dto import LicenseKeyDto
            license_key_dto = deserialize_request_body(json_data, LicenseKeyDto)
            kwargs['license_key_dto'] = license_key_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'set_user_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-user-onboarding")
def set_user_onboarding(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    is_onboarded: bool = typer.Option(..., "--isOnboarded", help="""Is user onboarded"""),
) -> None:
    """Update user onboarding

Docs: https://api.immich.app/endpoints/users/setUserOnboarding
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([is_onboarded])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.onboarding_dto import OnboardingDto
        onboarding_dto = deserialize_request_body(json_data, OnboardingDto)
        kwargs['onboarding_dto'] = onboarding_dto
    elif any([
        is_onboarded,
    ]):
        # Build body from dotted flags
        json_data = {}
        if is_onboarded is None:
            raise SystemExit("Error: --isOnboarded is required")
        set_nested(json_data, ['isOnboarded'], is_onboarded)
        if json_data:
            from immich.client.models.onboarding_dto import OnboardingDto
            onboarding_dto = deserialize_request_body(json_data, OnboardingDto)
            kwargs['onboarding_dto'] = onboarding_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'set_user_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-my-preferences")
def update_my_preferences(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    albums_default_asset_order: str | None = typer.Option(None, "--albums.defaultAssetOrder", help="""Asset sort order"""),
    avatar_color: str | None = typer.Option(None, "--avatar.color", help="""Avatar color"""),
    cast_g_cast_enabled: bool | None = typer.Option(None, "--cast.gCastEnabled", help="""Whether Google Cast is enabled"""),
    download_archive_size: int | None = typer.Option(None, "--download.archiveSize", help="""Maximum archive size in bytes"""),
    download_include_embedded_videos: bool | None = typer.Option(None, "--download.includeEmbeddedVideos", help="""Whether to include embedded videos in downloads"""),
    email_notifications_album_invite: bool | None = typer.Option(None, "--emailNotifications.albumInvite", help="""Whether to receive email notifications for album invites"""),
    email_notifications_album_update: bool | None = typer.Option(None, "--emailNotifications.albumUpdate", help="""Whether to receive email notifications for album updates"""),
    email_notifications_enabled: bool | None = typer.Option(None, "--emailNotifications.enabled", help="""Whether email notifications are enabled"""),
    folders_enabled: bool | None = typer.Option(None, "--folders.enabled", help="""Whether folders are enabled"""),
    folders_sidebar_web: bool | None = typer.Option(None, "--folders.sidebarWeb", help="""Whether folders appear in web sidebar"""),
    memories_duration: int | None = typer.Option(None, "--memories.duration", help="""Memory duration in seconds"""),
    memories_enabled: bool | None = typer.Option(None, "--memories.enabled", help="""Whether memories are enabled"""),
    people_enabled: bool | None = typer.Option(None, "--people.enabled", help="""Whether people are enabled"""),
    people_sidebar_web: bool | None = typer.Option(None, "--people.sidebarWeb", help="""Whether people appear in web sidebar"""),
    purchase_hide_buy_button_until: str | None = typer.Option(None, "--purchase.hideBuyButtonUntil", help="""Date until which to hide buy button"""),
    purchase_show_support_badge: bool | None = typer.Option(None, "--purchase.showSupportBadge", help="""Whether to show support badge"""),
    ratings_enabled: bool | None = typer.Option(None, "--ratings.enabled", help="""Whether ratings are enabled"""),
    shared_links_enabled: bool | None = typer.Option(None, "--sharedLinks.enabled", help="""Whether shared links are enabled"""),
    shared_links_sidebar_web: bool | None = typer.Option(None, "--sharedLinks.sidebarWeb", help="""Whether shared links appear in web sidebar"""),
    tags_enabled: bool | None = typer.Option(None, "--tags.enabled", help="""Whether tags are enabled"""),
    tags_sidebar_web: bool | None = typer.Option(None, "--tags.sidebarWeb", help="""Whether tags appear in web sidebar"""),
) -> None:
    """Update my preferences

Docs: https://api.immich.app/endpoints/users/updateMyPreferences
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([albums_default_asset_order, avatar_color, cast_g_cast_enabled, download_archive_size, download_include_embedded_videos, email_notifications_album_invite, email_notifications_album_update, email_notifications_enabled, folders_enabled, folders_sidebar_web, memories_duration, memories_enabled, people_enabled, people_sidebar_web, purchase_hide_buy_button_until, purchase_show_support_badge, ratings_enabled, shared_links_enabled, shared_links_sidebar_web, tags_enabled, tags_sidebar_web])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.user_preferences_update_dto import UserPreferencesUpdateDto
        user_preferences_update_dto = deserialize_request_body(json_data, UserPreferencesUpdateDto)
        kwargs['user_preferences_update_dto'] = user_preferences_update_dto
    elif any([
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
    ]):
        # Build body from dotted flags
        json_data = {}
        if albums_default_asset_order is not None:
            set_nested(json_data, ['albums', 'defaultAssetOrder'], albums_default_asset_order)
        if avatar_color is not None:
            set_nested(json_data, ['avatar', 'color'], avatar_color)
        if cast_g_cast_enabled is not None:
            set_nested(json_data, ['cast', 'gCastEnabled'], cast_g_cast_enabled)
        if download_archive_size is not None:
            set_nested(json_data, ['download', 'archiveSize'], download_archive_size)
        if download_include_embedded_videos is not None:
            set_nested(json_data, ['download', 'includeEmbeddedVideos'], download_include_embedded_videos)
        if email_notifications_album_invite is not None:
            set_nested(json_data, ['emailNotifications', 'albumInvite'], email_notifications_album_invite)
        if email_notifications_album_update is not None:
            set_nested(json_data, ['emailNotifications', 'albumUpdate'], email_notifications_album_update)
        if email_notifications_enabled is not None:
            set_nested(json_data, ['emailNotifications', 'enabled'], email_notifications_enabled)
        if folders_enabled is not None:
            set_nested(json_data, ['folders', 'enabled'], folders_enabled)
        if folders_sidebar_web is not None:
            set_nested(json_data, ['folders', 'sidebarWeb'], folders_sidebar_web)
        if memories_duration is not None:
            set_nested(json_data, ['memories', 'duration'], memories_duration)
        if memories_enabled is not None:
            set_nested(json_data, ['memories', 'enabled'], memories_enabled)
        if people_enabled is not None:
            set_nested(json_data, ['people', 'enabled'], people_enabled)
        if people_sidebar_web is not None:
            set_nested(json_data, ['people', 'sidebarWeb'], people_sidebar_web)
        if purchase_hide_buy_button_until is not None:
            set_nested(json_data, ['purchase', 'hideBuyButtonUntil'], purchase_hide_buy_button_until)
        if purchase_show_support_badge is not None:
            set_nested(json_data, ['purchase', 'showSupportBadge'], purchase_show_support_badge)
        if ratings_enabled is not None:
            set_nested(json_data, ['ratings', 'enabled'], ratings_enabled)
        if shared_links_enabled is not None:
            set_nested(json_data, ['sharedLinks', 'enabled'], shared_links_enabled)
        if shared_links_sidebar_web is not None:
            set_nested(json_data, ['sharedLinks', 'sidebarWeb'], shared_links_sidebar_web)
        if tags_enabled is not None:
            set_nested(json_data, ['tags', 'enabled'], tags_enabled)
        if tags_sidebar_web is not None:
            set_nested(json_data, ['tags', 'sidebarWeb'], tags_sidebar_web)
        if json_data:
            from immich.client.models.user_preferences_update_dto import UserPreferencesUpdateDto
            user_preferences_update_dto = deserialize_request_body(json_data, UserPreferencesUpdateDto)
            kwargs['user_preferences_update_dto'] = user_preferences_update_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'update_my_preferences', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-my-user")
def update_my_user(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    avatar_color: str | None = typer.Option(None, "--avatarColor", help="""Avatar color"""),
    email: str | None = typer.Option(None, "--email", help="""User email"""),
    name: str | None = typer.Option(None, "--name", help="""User name"""),
    password: str | None = typer.Option(None, "--password", help="""User password (deprecated, use change password endpoint)"""),
) -> None:
    """Update current user

Docs: https://api.immich.app/endpoints/users/updateMyUser
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([avatar_color, email, name, password])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.user_update_me_dto import UserUpdateMeDto
        user_update_me_dto = deserialize_request_body(json_data, UserUpdateMeDto)
        kwargs['user_update_me_dto'] = user_update_me_dto
    elif any([
        avatar_color,
        email,
        name,
        password,
    ]):
        # Build body from dotted flags
        json_data = {}
        if avatar_color is not None:
            set_nested(json_data, ['avatarColor'], avatar_color)
        if email is not None:
            set_nested(json_data, ['email'], email)
        if name is not None:
            set_nested(json_data, ['name'], name)
        if password is not None:
            set_nested(json_data, ['password'], password)
        if json_data:
            from immich.client.models.user_update_me_dto import UserUpdateMeDto
            user_update_me_dto = deserialize_request_body(json_data, UserUpdateMeDto)
            kwargs['user_update_me_dto'] = user_update_me_dto
    client = ctx.obj['client']
    api_group = client.users
    result = run_command(client, api_group, 'update_my_user', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
