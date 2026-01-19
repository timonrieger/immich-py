import os
import typer
from typing import Optional
from immich._internal.consts import (
    CONFIG_FILE,
    DEFAULT_PROFILE,
    DEMO_API_URL,
    IMMICH_ACCESS_TOKEN,
    IMMICH_API_KEY,
    IMMICH_API_URL,
)
from immich._internal.cli.utils import load_config, mask, print_, set_path, write_config
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
    base_url: Optional[str] = typer.Option(
        None,
        "--base-url",
        help="The base URL of the Immich server, including the API path.",
    ),
    api_key: Optional[str] = typer.Option(
        None,
        "--api-key",
        help="An API key to use with the profile ([green]recommended[/green])",
        hide_input=True,
        show_default=False,
    ),
    access_token: Optional[str] = typer.Option(
        None,
        "--access-token",
        help="An access token to use with the profile ([red]not recommended[/red])",
        hide_input=True,
        show_default=False,
    ),
    skip_validation: bool = typer.Option(
        False,
        "--skip-validation",
        help="Skip validation of the server.",
    ),
):
    """Interactively set up a profile for the CLI to connect to an Immich server."""
    data = load_config(ensure_exists=True)

    if base_url is None:
        base_url = typer.prompt(
            "Base URL",
            default=os.getenv(IMMICH_API_URL) or DEMO_API_URL,
        )

    if api_key is None:
        env_api_key = os.getenv(IMMICH_API_KEY)
        api_key = typer.prompt(
            "API Key (optional, recommended)"
            + (f" [{mask(env_api_key)}]" if env_api_key else ""),
            # default=None is not possible input is required
            default=env_api_key or "",
            show_default=False,
        )

    if not api_key and access_token is None:
        env_access_token = os.getenv(IMMICH_ACCESS_TOKEN)
        access_token = typer.prompt(
            "Access Token (optional, not recommended)"
            + (f" [{mask(env_access_token)}]" if env_access_token else ""),
            # default=None is not possible input is required
            default=env_access_token or "",
            show_default=False,
        )

    if not skip_validation:
        # Validate the server is reachable
        # passing empty strings is fine, as the client checks for falsey values
        client = AsyncClient(
            base_url=base_url, api_key=api_key, access_token=access_token
        )
        try:
            run_command(client, client.server, "ping_server")
        except Exception as exc:
            print_(
                "Error validating server. Make sure the base URL is correct and the server is reachable.",
                level="error",
                ctx=ctx,
            )
            print_(str(exc), level="debug", ctx=ctx)
            raise typer.Exit(1)

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
