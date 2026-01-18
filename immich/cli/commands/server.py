"""Generated CLI commands for Server tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Information about the current server deployment, including version and build information, available features, supported media types, and more.\n\nDocs: https://api.immich.app/endpoints/server"""
)


@app.command("delete-server-license", deprecated=False)
def delete_server_license(
    ctx: typer.Context,
) -> None:
    """Delete server product key

    Docs: https://api.immich.app/endpoints/server/deleteServerLicense
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "delete_server_license", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-about-info", deprecated=False)
def get_about_info(
    ctx: typer.Context,
) -> None:
    """Get server information

    Docs: https://api.immich.app/endpoints/server/getAboutInfo
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_about_info", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-apk-links", deprecated=False)
def get_apk_links(
    ctx: typer.Context,
) -> None:
    """Get APK links

    Docs: https://api.immich.app/endpoints/server/getApkLinks
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_apk_links", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-server-config", deprecated=False)
def get_server_config(
    ctx: typer.Context,
) -> None:
    """Get config

    Docs: https://api.immich.app/endpoints/server/getServerConfig
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_config", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-server-features", deprecated=False)
def get_server_features(
    ctx: typer.Context,
) -> None:
    """Get features

    Docs: https://api.immich.app/endpoints/server/getServerFeatures
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_features", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-server-license", deprecated=False)
def get_server_license(
    ctx: typer.Context,
) -> None:
    """Get product key

    Docs: https://api.immich.app/endpoints/server/getServerLicense
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_license", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-server-statistics", deprecated=False)
def get_server_statistics(
    ctx: typer.Context,
) -> None:
    """Get statistics

    Docs: https://api.immich.app/endpoints/server/getServerStatistics
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_statistics", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-server-version", deprecated=False)
def get_server_version(
    ctx: typer.Context,
) -> None:
    """Get server version

    Docs: https://api.immich.app/endpoints/server/getServerVersion
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_version", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-storage", deprecated=False)
def get_storage(
    ctx: typer.Context,
) -> None:
    """Get storage

    Docs: https://api.immich.app/endpoints/server/getStorage
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_storage", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-supported-media-types", deprecated=False)
def get_supported_media_types(
    ctx: typer.Context,
) -> None:
    """Get supported media types

    Docs: https://api.immich.app/endpoints/server/getSupportedMediaTypes
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_supported_media_types", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-theme", deprecated=False)
def get_theme(
    ctx: typer.Context,
) -> None:
    """Get theme

    Docs: https://api.immich.app/endpoints/server/getTheme
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_theme", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-version-check", deprecated=False)
def get_version_check(
    ctx: typer.Context,
) -> None:
    """Get version check status

    Docs: https://api.immich.app/endpoints/server/getVersionCheck
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_check", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-version-history", deprecated=False)
def get_version_history(
    ctx: typer.Context,
) -> None:
    """Get version history

    Docs: https://api.immich.app/endpoints/server/getVersionHistory
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_history", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("ping-server", deprecated=False)
def ping_server(
    ctx: typer.Context,
) -> None:
    """Ping

    Docs: https://api.immich.app/endpoints/server/pingServer
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.server, "ping_server", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("set-server-license", deprecated=False)
def set_server_license(
    ctx: typer.Context,
    activation_key: str = typer.Option(..., "--activation-key", help=""""""),
    license_key: str = typer.Option(..., "--license-key", help=""""""),
) -> None:
    """Set server product key

    Docs: https://api.immich.app/endpoints/server/setServerLicense
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["activation_key"], activation_key)
    set_nested(json_data, ["license_key"], license_key)
    from immich.client.models.license_key_dto import LicenseKeyDto

    license_key_dto = LicenseKeyDto.model_validate(json_data)
    kwargs["license_key_dto"] = license_key_dto
    client = ctx.obj["client"]
    result = run_command(client, client.server, "set_server_license", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
