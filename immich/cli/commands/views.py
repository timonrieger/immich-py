"""Generated CLI commands for Views tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints for specialized views, such as the folder view.. https://api.immich.app/endpoints/views', context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-assets-by-original-path")
def get_assets_by_original_path(
    ctx: typer.Context,
    path: str = typer.Option(..., "--path"),
) -> None:
    """Retrieve assets by original path"""
    kwargs = {}
    kwargs['path'] = path
    client = ctx.obj['client']
    api_group = client.views
    result = run_command(client, api_group, 'get_assets_by_original_path', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-unique-original-paths")
def get_unique_original_paths(
    ctx: typer.Context,
) -> None:
    """Retrieve unique paths"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.views
    result = run_command(client, api_group, 'get_unique_original_paths', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
