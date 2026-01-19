"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command
from immich.client.generated.models import *

app = typer.Typer(
    help="""A plugin is an installed module that makes filters and actions available for the workflow feature.\n\nDocs: https://api.immich.app/endpoints/plugins"""
)


@app.command("get-plugin", deprecated=False, rich_help_panel="API commands")
def get_plugin(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:  # pragma: no cover
    """Retrieve a plugin

    Docs: https://api.immich.app/endpoints/plugins/getPlugin
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-plugin-triggers", deprecated=False, rich_help_panel="API commands")
def get_plugin_triggers(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """List all plugin triggers

    Docs: https://api.immich.app/endpoints/plugins/getPluginTriggers
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin_triggers", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-plugins", deprecated=False, rich_help_panel="API commands")
def get_plugins(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """List all plugins

    Docs: https://api.immich.app/endpoints/plugins/getPlugins
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugins", ctx, **kwargs)
    print_response(result, ctx)
