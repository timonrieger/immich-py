"""Generated CLI commands for Views tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Views operations")

@app.command("get-assets-by-original-path")
def get_assets_by_original_path(
    path: str = typer.Option(..., "--path"),
    ctx: typer.Context,
) -> None:
    """Retrieve assets by original path"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.views
    result = run_command(client, api_group, 'get_unique_original_paths', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
