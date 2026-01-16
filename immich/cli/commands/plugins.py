"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command

app = typer.Typer(
    help="""A plugin is an installed module that makes filters and actions available for the workflow feature.

Docs: https://api.immich.app/endpoints/plugins""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("get-plugin")
def get_plugin(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a plugin

    Docs: https://api.immich.app/endpoints/plugins/getPlugin
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-plugin-triggers")
def get_plugin_triggers(
    ctx: typer.Context,
) -> None:
    """List all plugin triggers

    Docs: https://api.immich.app/endpoints/plugins/getPluginTriggers
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugin_triggers", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-plugins")
def get_plugins(
    ctx: typer.Context,
) -> None:
    """List all plugins

    Docs: https://api.immich.app/endpoints/plugins/getPlugins
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.plugins, "get_plugins", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
