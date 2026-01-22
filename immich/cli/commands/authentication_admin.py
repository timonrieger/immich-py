"""Generated CLI commands for Authentication (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command
from immich.client.generated.models import *

app = typer.Typer(
    help="""Administrative endpoints related to authentication.\n\n[link=https://api.immich.app/endpoints/authentication-admin]Immich API documentation[/link]"""
)


@app.command(
    "unlink-all-o-auth-accounts-admin", deprecated=False, rich_help_panel="API commands"
)
def unlink_all_o_auth_accounts_admin(
    ctx: typer.Context,
) -> None:
    """Unlink all OAuth accounts

    [link=https://api.immich.app/endpoints/authentication-admin/unlinkAllOAuthAccountsAdmin]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.auth_admin, "unlink_all_o_auth_accounts_admin", ctx, **kwargs
    )
    print_response(result, ctx)
