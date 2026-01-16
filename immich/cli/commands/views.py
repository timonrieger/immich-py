"""Generated CLI commands for Views tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command

app = typer.Typer(
    help="""Endpoints for specialized views, such as the folder view.

Docs: https://api.immich.app/endpoints/views""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("get-assets-by-original-path")
def get_assets_by_original_path(
    ctx: typer.Context,
    path: str = typer.Option(..., "--path"),
) -> None:
    """Retrieve assets by original path

    Docs: https://api.immich.app/endpoints/views/getAssetsByOriginalPath
    """
    kwargs = {}
    kwargs["path"] = path
    client = ctx.obj["client"]
    result = run_command(client, client.views, "get_assets_by_original_path", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-unique-original-paths")
def get_unique_original_paths(
    ctx: typer.Context,
) -> None:
    """Retrieve unique paths

    Docs: https://api.immich.app/endpoints/views/getUniqueOriginalPaths
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.views, "get_unique_original_paths", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
