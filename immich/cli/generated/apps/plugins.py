"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Plugins operations")

@app.command("get-plugin")
def get_plugin(
    id: str,
    ctx: typer.Context,
) -> None:
    """Retrieve a plugin"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.plugins
    result = run_command(client, api_group, 'get_plugins', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
