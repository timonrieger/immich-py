"""Main CLI entrypoint."""

from __future__ import annotations

import sys
from typing import Optional
from importlib.metadata import version

from click.core import ParameterSource

from immich.cli.consts import (
    API_KEY_URL,
    DEFAULT_FORMAT,
    DEFAULT_PROFILE,
    IMMICH_API_KEY,
    IMMICH_ACCESS_TOKEN,
    IMMICH_API_URL,
    IMMICH_FORMAT,
    IMMICH_PROFILE,
)
from immich.cli.utils import resolve_client_config, mask, print_

try:
    import typer
    from rich.console import Console
except ImportError:  # pragma: no cover
    print(
        "Error: CLI dependencies not installed. Install with: pip install immich[cli]",
        file=sys.stderr,
    )
    sys.exit(1)

from immich import AsyncClient
from immich.cli.types import FormatMode, ClientConfig

# Import command modules
from immich.cli.commands import api_keys as api_keys_commands
from immich.cli.commands import activities as activities_commands
from immich.cli.commands import albums as albums_commands
from immich.cli.wrapper import assets as assets_wrapper
from immich.cli.commands import authentication as authentication_commands
from immich.cli.commands import authentication_admin as authentication_admin_commands
from immich.cli.wrapper import download as download_wrapper
from immich.cli.wrapper import config as config_commands
from immich.cli.wrapper import setup as setup_commands
from immich.cli.commands import duplicates as duplicates_commands
from immich.cli.commands import faces as faces_commands
from immich.cli.commands import jobs as jobs_commands
from immich.cli.commands import libraries as libraries_commands
from immich.cli.commands import maintenance_admin as maintenance_admin_commands
from immich.cli.commands import map as map_commands
from immich.cli.commands import memories as memories_commands
from immich.cli.commands import notifications as notifications_commands
from immich.cli.commands import notifications_admin as notifications_admin_commands
from immich.cli.commands import partners as partners_commands
from immich.cli.commands import people as people_commands
from immich.cli.commands import plugins as plugins_commands
from immich.cli.commands import queues as queues_commands
from immich.cli.commands import search as search_commands
from immich.cli.commands import server as server_commands
from immich.cli.commands import sessions as sessions_commands
from immich.cli.commands import shared_links as shared_links_commands
from immich.cli.commands import stacks as stacks_commands
from immich.cli.commands import sync as sync_commands
from immich.cli.commands import system_config as system_config_commands
from immich.cli.commands import system_metadata as system_metadata_commands
from immich.cli.commands import tags as tags_commands
from immich.cli.commands import timeline as timeline_commands
from immich.cli.commands import trash as trash_commands
from immich.cli.wrapper import users as users_wrapper
from immich.cli.commands import users_admin as users_admin_commands
from immich.cli.commands import views as views_commands
from immich.cli.commands import workflows as workflows_commands
# from immich.cli.commands import (
#     database_backups_admin as database_backups_admin_commands,
# )

# Global state
app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]}, no_args_is_help=True
)
console = Console()
stderr_console = Console(file=sys.stderr)

# Add command modules to the main app
app.add_typer(api_keys_commands.app, name="api-keys", rich_help_panel="API commands")
app.add_typer(
    activities_commands.app, name="activities", rich_help_panel="API commands"
)
app.add_typer(albums_commands.app, name="albums", rich_help_panel="API commands")
app.add_typer(assets_wrapper.app, name="assets", rich_help_panel="API commands")
app.add_typer(authentication_commands.app, name="auth", rich_help_panel="API commands")
app.add_typer(
    authentication_admin_commands.app,
    name="auth-admin",
    rich_help_panel="API commands",
)
app.add_typer(download_wrapper.app, name="download", rich_help_panel="API commands")
app.add_typer(config_commands.app, name="config", rich_help_panel="Custom commands")
app.command(rich_help_panel="Custom commands")(setup_commands.setup)
app.add_typer(
    duplicates_commands.app, name="duplicates", rich_help_panel="API commands"
)
app.add_typer(faces_commands.app, name="faces", rich_help_panel="API commands")
app.add_typer(jobs_commands.app, name="jobs", rich_help_panel="API commands")
app.add_typer(libraries_commands.app, name="libraries", rich_help_panel="API commands")
app.add_typer(
    maintenance_admin_commands.app,
    name="maintenance-admin",
    rich_help_panel="API commands",
)
app.add_typer(map_commands.app, name="map", rich_help_panel="API commands")
app.add_typer(memories_commands.app, name="memories", rich_help_panel="API commands")
app.add_typer(
    notifications_commands.app, name="notifications", rich_help_panel="API commands"
)
app.add_typer(
    notifications_admin_commands.app,
    name="notifications-admin",
    rich_help_panel="API commands",
)
app.add_typer(partners_commands.app, name="partners", rich_help_panel="API commands")
app.add_typer(people_commands.app, name="people", rich_help_panel="API commands")
app.add_typer(plugins_commands.app, name="plugins", rich_help_panel="API commands")
app.add_typer(queues_commands.app, name="queues", rich_help_panel="API commands")
app.add_typer(search_commands.app, name="search", rich_help_panel="API commands")
app.add_typer(server_commands.app, name="server", rich_help_panel="API commands")
app.add_typer(sessions_commands.app, name="sessions", rich_help_panel="API commands")
app.add_typer(
    shared_links_commands.app, name="shared-links", rich_help_panel="API commands"
)
app.add_typer(stacks_commands.app, name="stacks", rich_help_panel="API commands")
app.add_typer(sync_commands.app, name="sync", rich_help_panel="API commands")
app.add_typer(
    system_config_commands.app, name="system-config", rich_help_panel="API commands"
)
app.add_typer(
    system_metadata_commands.app, name="system-metadata", rich_help_panel="API commands"
)
app.add_typer(tags_commands.app, name="tags", rich_help_panel="API commands")
app.add_typer(timeline_commands.app, name="timeline", rich_help_panel="API commands")
app.add_typer(trash_commands.app, name="trash", rich_help_panel="API commands")
app.add_typer(users_wrapper.app, name="users", rich_help_panel="API commands")
app.add_typer(
    users_admin_commands.app, name="users-admin", rich_help_panel="API commands"
)
app.add_typer(views_commands.app, name="views", rich_help_panel="API commands")
app.add_typer(workflows_commands.app, name="workflows", rich_help_panel="API commands")
# app.add_typer(
#     database_backups_admin_commands.app,
#     name="backups",
#     rich_help_panel="API commands",
# )


def version_callback(value: bool) -> None:  # pragma: no cover
    if value:
        print_(f"immich CLI (unofficial) {version('immich')}", type="text")
        raise typer.Exit(0)


@app.callback(invoke_without_command=False)
def callback(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show verbose output.",
    ),
    format_mode: FormatMode = typer.Option(
        DEFAULT_FORMAT,
        "--format",
        help="Output format of the CLI.",
        envvar=IMMICH_FORMAT,
    ),
    api_key: Optional[str] = typer.Option(
        None,
        "--api-key",
        help=f"Authorize via API key (get one [link={API_KEY_URL}]here[/link]).",
        envvar=IMMICH_API_KEY,
    ),
    access_token: Optional[str] = typer.Option(
        None,
        "--access-token",
        help="Authorize via access token.",
        envvar=IMMICH_ACCESS_TOKEN,
    ),
    base_url: Optional[str] = typer.Option(
        None,
        "--base-url",
        help="The server to connect to.",
        envvar=IMMICH_API_URL,
    ),
    profile: str = typer.Option(
        DEFAULT_PROFILE,
        "--profile",
        "-p",
        envvar=IMMICH_PROFILE,
        help="The profile to use.",
    ),
    _version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit.",
    ),
) -> None:  # pragma: no cover
    ctx.ensure_object(dict)
    ctx.obj["format"] = format_mode
    ctx.obj["verbose"] = verbose
    if ctx.invoked_subcommand is not None and ctx.invoked_subcommand not in [
        "setup",
        "config",
    ]:
        config = resolve_client_config(
            ClientConfig(
                api_key=api_key,
                access_token=access_token,
                base_url=base_url,
            ),
            profile=profile,
            # we only consider the profile explicit if it was set via the command line
            # environment variables are not considered explicit
            profile_explicit=ctx.get_parameter_source("profile")
            == ParameterSource.COMMANDLINE,
        )
        if not config.base_url:
            print_(
                "No base URL provided. Run 'immich setup' to set up a profile or use '--base-url' to specify a base URL.",
                type="error",
            )
            raise typer.Exit(code=1)
        if ctx.obj["verbose"]:
            cli_vars = {
                k: v
                for k, v in ctx.params.items()
                if k in ClientConfig.model_fields.keys() and v is not None
            }
            print_("Configuration used:", type="debug", ctx=ctx)
            for field in ClientConfig.model_fields.keys():
                value = getattr(config, field)
                if field in ("api_key", "access_token") and value:
                    value = mask(value)
                elif value is None:
                    value = "None"
                source = "cli/env" if field in cli_vars else f"profile '{profile}'"
                print_(f"- {field}: {value} (from {source})", type="debug", ctx=ctx)
        if omit_access_token := (config.api_key is not None):
            print_(
                "Omitting access token because API key is provided.",
                type="debug",
                ctx=ctx,
            )
        ctx.obj["client"] = AsyncClient(
            api_key=config.api_key,
            access_token=None if omit_access_token else config.access_token,
            base_url=config.base_url,
        )


if __name__ == "__main__":  # pragma: no cover
    app()
