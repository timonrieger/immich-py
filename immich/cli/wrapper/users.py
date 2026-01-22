"""CLI wrapper commands for UsersApiWrapped convenience methods."""

from __future__ import annotations

from pathlib import Path

import typer

from immich.cli.commands import users as users_commands
from immich.cli.runtime import print_response, run_command

# Reuse the existing app from the generated commands
app = users_commands.app


@app.command("get-profile-image-to-file")
def get_profile_image_to_file(
    ctx: typer.Context,
    id: str = typer.Argument(..., help="User ID (UUID)"),
    out_dir: Path = typer.Argument(
        ..., help="Output directory for the profile image file"
    ),
    filename: str | None = typer.Option(
        None,
        "--filename",
        help="Filename to use (defaults to original filename or profile-{user_id})",
    ),
    show_progress: bool = typer.Option(
        False,
        "--show-progress",
        help="Show progress bar while downloading",
    ),
) -> None:  # pragma: no cover
    """Download a user's profile image and save it to a file.

    Downloads the profile image for the specified user and saves it to the specified output directory.
    The filename can be specified or will be derived from the response headers.
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["out_dir"] = out_dir
    if filename is not None:
        kwargs["filename"] = filename
    kwargs["show_progress"] = show_progress
    client = ctx.obj["client"]
    result = run_command(client, client.users, "get_profile_image_to_file", **kwargs)
    print_response(result, ctx)
