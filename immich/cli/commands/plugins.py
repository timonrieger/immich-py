"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command
from immich.client.models import *

app = typer.Typer(
    help="""A plugin is an installed module that makes filters and actions available for the workflow feature.\n\nDocs: https://api.immich.app/endpoints/plugins"""
)


@app.command("get-plugin", deprecated=False)
def get_plugin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a plugin

    Docs: https://api.immich.app/endpoints/plugins/getPlugin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-plugins", deprecated=False)
def get_plugins(
    ctx: typer.Context,
) -> None:
    """List all plugins

    Docs: https://api.immich.app/endpoints/plugins/getPlugins
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugins", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
