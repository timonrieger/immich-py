"""Generated CLI commands for Views tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints for specialized views, such as the folder view.\n\nDocs: https://api.immich.app/endpoints/views"""
)


@app.command("get-assets-by-original-path", deprecated=False)
def get_assets_by_original_path(
    ctx: typer.Context,
    path: str = typer.Option(..., "--path", help=""""""),
) -> None:
    """Retrieve assets by original path

    Docs: https://api.immich.app/endpoints/views/getAssetsByOriginalPath
    """
    kwargs = {}
    kwargs["path"] = path
    client = ctx.obj["client"]
    result = run_command(client, client.views, "get_assets_by_original_path", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-unique-original-paths", deprecated=False)
def get_unique_original_paths(
    ctx: typer.Context,
) -> None:
    """Retrieve unique paths

    Docs: https://api.immich.app/endpoints/views/getUniqueOriginalPaths
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.views, "get_unique_original_paths", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
