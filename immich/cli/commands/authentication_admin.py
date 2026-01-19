"""Generated CLI commands for Authentication (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command
from immich.client.generated.models import *

app = typer.Typer(
    help="""Administrative endpoints related to authentication.\n\nDocs: https://api.immich.app/endpoints/authentication-admin"""
)


@app.command(
    "unlink-all-o-auth-accounts-admin", deprecated=False, rich_help_panel="API commands"
)
def unlink_all_o_auth_accounts_admin(
    ctx: typer.Context,
) -> None:  # pragma: no cover
    """Unlink all OAuth accounts

    Docs: https://api.immich.app/endpoints/authentication-admin/unlinkAllOAuthAccountsAdmin
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client,
        client.authentication_admin,
        "unlink_all_o_auth_accounts_admin",
        ctx,
        **kwargs,
    )
    print_response(result, ctx)
