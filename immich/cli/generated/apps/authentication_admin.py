"""Generated CLI commands for Authentication (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="Authentication (admin) operations")

@app.command("unlink-all-o-auth-accounts-admin")
def unlink_all_o_auth_accounts_admin(
    ctx: typer.Context,
) -> None:
    """Unlink all OAuth accounts"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication_admin
    result = run_command(client, api_group, 'unlink_all_o_auth_accounts_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
