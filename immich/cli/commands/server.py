"""Generated CLI commands for Server tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Information about the current server deployment, including version and build information, available features, supported media types, and more.\n\n[link=https://api.immich.app/endpoints/server]Immich API documentation[/link]"""
)


@app.command("delete-server-license", deprecated=False, rich_help_panel="API commands")
def delete_server_license(
    ctx: typer.Context,
) -> None:
    """Delete server product key

    [link=https://api.immich.app/endpoints/server/deleteServerLicense]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "delete_server_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-about-info", deprecated=False, rich_help_panel="API commands")
def get_about_info(
    ctx: typer.Context,
) -> None:
    """Get server information

    [link=https://api.immich.app/endpoints/server/getAboutInfo]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_about_info", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-apk-links", deprecated=False, rich_help_panel="API commands")
def get_apk_links(
    ctx: typer.Context,
) -> None:
    """Get APK links

    [link=https://api.immich.app/endpoints/server/getApkLinks]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_apk_links", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-config", deprecated=False, rich_help_panel="API commands")
def get_server_config(
    ctx: typer.Context,
) -> None:
    """Get config

    [link=https://api.immich.app/endpoints/server/getServerConfig]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_config", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-features", deprecated=False, rich_help_panel="API commands")
def get_server_features(
    ctx: typer.Context,
) -> None:
    """Get features

    [link=https://api.immich.app/endpoints/server/getServerFeatures]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_features", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-license", deprecated=False, rich_help_panel="API commands")
def get_server_license(
    ctx: typer.Context,
) -> None:
    """Get product key

    [link=https://api.immich.app/endpoints/server/getServerLicense]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-statistics", deprecated=False, rich_help_panel="API commands")
def get_server_statistics(
    ctx: typer.Context,
) -> None:
    """Get statistics

    [link=https://api.immich.app/endpoints/server/getServerStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_statistics", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-version", deprecated=False, rich_help_panel="API commands")
def get_server_version(
    ctx: typer.Context,
) -> None:
    """Get server version

    [link=https://api.immich.app/endpoints/server/getServerVersion]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_version", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-storage", deprecated=False, rich_help_panel="API commands")
def get_storage(
    ctx: typer.Context,
) -> None:
    """Get storage

    [link=https://api.immich.app/endpoints/server/getStorage]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_storage", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "get-supported-media-types", deprecated=False, rich_help_panel="API commands"
)
def get_supported_media_types(
    ctx: typer.Context,
) -> None:
    """Get supported media types

    [link=https://api.immich.app/endpoints/server/getSupportedMediaTypes]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.server, "get_supported_media_types", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("get-theme", deprecated=False, rich_help_panel="API commands")
def get_theme(
    ctx: typer.Context,
) -> None:
    """Get theme

    [link=https://api.immich.app/endpoints/server/getTheme]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_theme", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-version-check", deprecated=False, rich_help_panel="API commands")
def get_version_check(
    ctx: typer.Context,
) -> None:
    """Get version check status

    [link=https://api.immich.app/endpoints/server/getVersionCheck]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_check", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-version-history", deprecated=False, rich_help_panel="API commands")
def get_version_history(
    ctx: typer.Context,
) -> None:
    """Get version history

    [link=https://api.immich.app/endpoints/server/getVersionHistory]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_history", ctx, **kwargs)
    print_response(result, ctx)


@app.command("ping-server", deprecated=False, rich_help_panel="API commands")
def ping_server(
    ctx: typer.Context,
) -> None:
    """Ping

    [link=https://api.immich.app/endpoints/server/pingServer]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "ping_server", ctx, **kwargs)
    print_response(result, ctx)


@app.command("set-server-license", deprecated=False, rich_help_panel="API commands")
def set_server_license(
    ctx: typer.Context,
    activation_key: str = typer.Option(..., "--activation-key", help=""""""),
    license_key: str = typer.Option(..., "--license-key", help=""""""),
) -> None:
    """Set server product key

    [link=https://api.immich.app/endpoints/server/setServerLicense]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["activation_key"], activation_key)
    set_nested(json_data, ["license_key"], license_key)
    license_key_dto = LicenseKeyDto.model_validate(json_data)
    kwargs["license_key_dto"] = license_key_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "set_server_license", ctx, **kwargs)
    print_response(result, ctx)
