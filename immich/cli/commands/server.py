"""Generated CLI commands for Server tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""Information about the current server deployment, including version and build information, available features, supported media types, and more.

Docs: https://api.immich.app/endpoints/server""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("delete-server-license")
def delete_server_license(
    ctx: typer.Context,
) -> None:
    """Delete server product key

Docs: https://api.immich.app/endpoints/server/deleteServerLicense
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'delete_server_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-about-info")
def get_about_info(
    ctx: typer.Context,
) -> None:
    """Get server information

Docs: https://api.immich.app/endpoints/server/getAboutInfo
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_about_info', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-apk-links")
def get_apk_links(
    ctx: typer.Context,
) -> None:
    """Get APK links

Docs: https://api.immich.app/endpoints/server/getApkLinks
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_apk_links', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-server-config")
def get_server_config(
    ctx: typer.Context,
) -> None:
    """Get config

Docs: https://api.immich.app/endpoints/server/getServerConfig
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_server_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-server-features")
def get_server_features(
    ctx: typer.Context,
) -> None:
    """Get features

Docs: https://api.immich.app/endpoints/server/getServerFeatures
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_server_features', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-server-license")
def get_server_license(
    ctx: typer.Context,
) -> None:
    """Get product key

Docs: https://api.immich.app/endpoints/server/getServerLicense
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_server_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-server-statistics")
def get_server_statistics(
    ctx: typer.Context,
) -> None:
    """Get statistics

Docs: https://api.immich.app/endpoints/server/getServerStatistics
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_server_statistics', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-server-version")
def get_server_version(
    ctx: typer.Context,
) -> None:
    """Get server version

Docs: https://api.immich.app/endpoints/server/getServerVersion
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_server_version', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-storage")
def get_storage(
    ctx: typer.Context,
) -> None:
    """Get storage

Docs: https://api.immich.app/endpoints/server/getStorage
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_storage', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-supported-media-types")
def get_supported_media_types(
    ctx: typer.Context,
) -> None:
    """Get supported media types

Docs: https://api.immich.app/endpoints/server/getSupportedMediaTypes
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_supported_media_types', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-theme")
def get_theme(
    ctx: typer.Context,
) -> None:
    """Get theme

Docs: https://api.immich.app/endpoints/server/getTheme
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_theme', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-version-check")
def get_version_check(
    ctx: typer.Context,
) -> None:
    """Get version check status

Docs: https://api.immich.app/endpoints/server/getVersionCheck
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_version_check', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-version-history")
def get_version_history(
    ctx: typer.Context,
) -> None:
    """Get version history

Docs: https://api.immich.app/endpoints/server/getVersionHistory
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'get_version_history', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("ping-server")
def ping_server(
    ctx: typer.Context,
) -> None:
    """Ping

Docs: https://api.immich.app/endpoints/server/pingServer
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.server, 'ping_server', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("set-server-license")
def set_server_license(
    ctx: typer.Context,
    activation_key: str = typer.Option(..., "--activationKey"),
    license_key: str = typer.Option(..., "--licenseKey"),
) -> None:
    """Set server product key

Docs: https://api.immich.app/endpoints/server/setServerLicense
    """
    kwargs = {}
    has_flags = any([activation_key, license_key])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([activation_key, license_key]):
        json_data = {}
        set_nested(json_data, ['activationKey'], activation_key)
        set_nested(json_data, ['licenseKey'], license_key)
        from immich.client.models.license_key_dto import LicenseKeyDto
        license_key_dto = deserialize_request_body(json_data, LicenseKeyDto)
        kwargs['license_key_dto'] = license_key_dto
    client = ctx.obj['client']
    result = run_command(client, client.server, 'set_server_license', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
