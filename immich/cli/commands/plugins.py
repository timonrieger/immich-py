"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A plugin is an installed module that makes filters and actions available for the workflow feature.. https://api.immich.app/endpoints/plugins', context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-plugin")
def get_plugin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a plugin"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.plugins
    result = run_command(client, api_group, 'get_plugin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-plugin-triggers")
def get_plugin_triggers(
    ctx: typer.Context,
) -> None:
    """List all plugin triggers"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.plugins
    result = run_command(client, api_group, 'get_plugin_triggers', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-plugins")
def get_plugins(
    ctx: typer.Context,
) -> None:
    """List all plugins"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.plugins
    result = run_command(client, api_group, 'get_plugins', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
