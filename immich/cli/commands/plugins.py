"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command
from immich.client.generated.models import *

app = typer.Typer(
    help="""A plugin is an installed module that makes filters and actions available for the workflow feature.\n\n[link=https://api.immich.app/endpoints/plugins]Immich API documentation[/link]"""
)


@app.command("get-plugin", deprecated=False, rich_help_panel="API commands")
def get_plugin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a plugin

    [link=https://api.immich.app/endpoints/plugins/getPlugin]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-plugins", deprecated=False, rich_help_panel="API commands")
def get_plugins(
    ctx: typer.Context,
) -> None:
    """List all plugins

    [link=https://api.immich.app/endpoints/plugins/getPlugins]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugins", ctx, **kwargs)
    print_response(result, ctx)
