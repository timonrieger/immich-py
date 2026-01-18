import typer
from typing import Optional
from immich._internal.consts import (
    CONFIG_FILE,
    DEFAULT_PROFILE,
    IMMICH_ACCESS_TOKEN,
    IMMICH_API_KEY,
    IMMICH_API_URL,
)
from immich._internal.cli.utils import load_config, print_, set_path, write_config
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
        ...,
        "--base-url",
        help="The base URL of the Immich server, including the API path. (e.g., https://demo.immich.app/api)",
        envvar=IMMICH_API_URL,
        prompt="Base URL (e.g., https://demo.immich.app/api)",
    ),
    api_key: Optional[str] = typer.Option(
        "",
        "--api-key",
        help="An API key to use with the profile.",
        envvar=IMMICH_API_KEY,
        prompt="API Key",
        hide_input=True,
        show_default=False,
    ),
    access_token: Optional[str] = typer.Option(
        "",
        "--access-token",
        help="An access token to use with the profile.",
        envvar=IMMICH_ACCESS_TOKEN,
        prompt="Access Token",
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

    if not skip_validation:
        # Validate the server is reachable
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

    typer.echo(
        f"Profile '{profile}' written to {CONFIG_FILE}. To verify the config, run 'immich config get profiles.{profile}'"
    )
