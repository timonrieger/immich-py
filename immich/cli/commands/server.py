"""Generated CLI commands for Server tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Information about the current server deployment, including version and build information, available features, supported media types, and more.\n\nDocs: https://api.immich.app/endpoints/server"""
)


@app.command("delete-server-license", deprecated=False, rich_help_panel="API commands")
def delete_server_license(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Delete server product key

    Docs: https://api.immich.app/endpoints/server/deleteServerLicense
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "delete_server_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-about-info", deprecated=False, rich_help_panel="API commands")
def get_about_info(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get server information

    Docs: https://api.immich.app/endpoints/server/getAboutInfo
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_about_info", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-apk-links", deprecated=False, rich_help_panel="API commands")
def get_apk_links(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get APK links

    Docs: https://api.immich.app/endpoints/server/getApkLinks
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_apk_links", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-config", deprecated=False, rich_help_panel="API commands")
def get_server_config(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get config

    Docs: https://api.immich.app/endpoints/server/getServerConfig
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_config", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-features", deprecated=False, rich_help_panel="API commands")
def get_server_features(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get features

    Docs: https://api.immich.app/endpoints/server/getServerFeatures
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_features", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-license", deprecated=False, rich_help_panel="API commands")
def get_server_license(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get product key

    Docs: https://api.immich.app/endpoints/server/getServerLicense
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_license", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-statistics", deprecated=False, rich_help_panel="API commands")
def get_server_statistics(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get statistics

    Docs: https://api.immich.app/endpoints/server/getServerStatistics
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_statistics", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-server-version", deprecated=False, rich_help_panel="API commands")
def get_server_version(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get server version

    Docs: https://api.immich.app/endpoints/server/getServerVersion
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_server_version", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-storage", deprecated=False, rich_help_panel="API commands")
def get_storage(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get storage

    Docs: https://api.immich.app/endpoints/server/getStorage
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
) -> None:  # pragma: no cover
    """Get supported media types

    Docs: https://api.immich.app/endpoints/server/getSupportedMediaTypes
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
) -> None:  # pragma: no cover
    """Get theme

    Docs: https://api.immich.app/endpoints/server/getTheme
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_theme", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-version-check", deprecated=False, rich_help_panel="API commands")
def get_version_check(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get version check status

    Docs: https://api.immich.app/endpoints/server/getVersionCheck
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_check", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-version-history", deprecated=False, rich_help_panel="API commands")
def get_version_history(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Get version history

    Docs: https://api.immich.app/endpoints/server/getVersionHistory
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.server, "get_version_history", ctx, **kwargs)
    print_response(result, ctx)


@app.command("ping-server", deprecated=False, rich_help_panel="API commands")
def ping_server(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Ping

    Docs: https://api.immich.app/endpoints/server/pingServer
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
) -> None:  # pragma: no cover
    """Set server product key

    Docs: https://api.immich.app/endpoints/server/setServerLicense
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
