"""Generated CLI commands for Views tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints for specialized views, such as the folder view.\n\n[link=https://api.immich.app/endpoints/views]Immich API documentation[/link]"""
)


@app.command(
    "get-assets-by-original-path", deprecated=False, rich_help_panel="API commands"
)
def get_assets_by_original_path(
    ctx: typer.Context,
    path: str = typer.Option(..., "--path", help=""""""),
) -> None:
    """Retrieve assets by original path

    [link=https://api.immich.app/endpoints/views/getAssetsByOriginalPath]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["path"] = path
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.views, "get_assets_by_original_path", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "get-unique-original-paths", deprecated=False, rich_help_panel="API commands"
)
def get_unique_original_paths(
    ctx: typer.Context,
) -> None:
    """Retrieve unique paths

    [link=https://api.immich.app/endpoints/views/getUniqueOriginalPaths]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.views, "get_unique_original_paths", ctx, **kwargs
    )
    print_response(result, ctx)
