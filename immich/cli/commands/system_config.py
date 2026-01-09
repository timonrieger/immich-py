"""Generated CLI commands for System config tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints to view, modify, and validate the system configuration settings.. https://api.immich.app/endpoints/system-config', context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-config")
def get_config(
    ctx: typer.Context,
) -> None:
    """Get system configuration"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-config-defaults")
def get_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get system configuration defaults"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config_defaults', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-storage-template-options")
def get_storage_template_options(
    ctx: typer.Context,
) -> None:
    """Get storage template options"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_storage_template_options', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-config")
def update_config(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update system configuration"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.system_config_dto import SystemConfigDto
        system_config_dto = deserialize_request_body(json_data, SystemConfigDto)
        kwargs['system_config_dto'] = system_config_dto
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'update_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
