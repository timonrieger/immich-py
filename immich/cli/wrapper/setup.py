import os
import typer
from typing import Optional
from immich.cli.consts import (
    CONFIG_FILE,
    DEFAULT_PROFILE,
    DEMO_API_URL,
    IMMICH_API_URL,
)
from immich.cli.utils import load_config, print_, set_path, write_config
from immich.cli.runtime import run_command

from immich import AsyncClient


def setup(
    ctx: typer.Context,
    profile: str = typer.Option(
        DEFAULT_PROFILE,
        "--profile",
        "-p",
        help="Profile name. This can be used to set different server configurations.",
    ),
    base_url: str = typer.Option(
        os.getenv(IMMICH_API_URL) or DEMO_API_URL,
        "--base-url",
        help="The base URL of the Immich server, including the API path.",
        prompt="Enter your server URL",
    ),
    api_key: Optional[str] = typer.Option(
        "",
        "--api-key",
        help="An API key to use with the profile ([green]recommended[/green])",
        prompt="Enter your API key (optional, recommended)",
        hide_input=True,
        show_default=False,
    ),
    access_token: Optional[str] = typer.Option(
        "",
        "--access-token",
        help="An access token to use with the profile ([red]not recommended[/red])",
        prompt="Enter your access token (optional, not recommended)",
        hide_input=True,
        show_default=False,
    ),
    skip_validation: bool = typer.Option(
        False,
        "--skip-validation",
        help="Skip validation of the server.",
    ),
) -> None:  # pragma: no cover
    """Interactively set up a profile for the CLI to connect to an Immich server."""
    data = load_config()

    if not skip_validation:
        # Validate the server is reachable
        client = AsyncClient(
            base_url=base_url, api_key=api_key, access_token=access_token
        )
        try:
            run_command(client, client.server, "ping_server", ctx=ctx)
        except Exception:
            print_(
                "Error validating server. Make sure the base URL is correct (including /api) and the server is reachable.",
                type="error",
                ctx=ctx,
            )
            raise

    set_path(
        data,
        f"profiles.{profile}",
        {
            "base_url": base_url,
            "api_key": api_key,
            "access_token": access_token,
        },
    )

    write_config(data)

    print("")
    print_(
        f"Profile [bold]{profile}[/bold] written to [bold]{CONFIG_FILE}[/bold].",
        type="success",
    )
    print_(
        f"To verify the config, run [bold]immich config get profiles.{profile}[/bold]",
        type="info",
    )
