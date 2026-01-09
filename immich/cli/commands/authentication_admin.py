"""Generated CLI commands for Authentication (admin) tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Administrative endpoints related to authentication.. https://api.immich.app/endpoints/authentication-admin', context_settings={'help_option_names': ['-h', '--help']})

@app.command("unlink-all-o-auth-accounts-admin")
def unlink_all_o_auth_accounts_admin(
    ctx: typer.Context,
) -> None:
    """Unlink all OAuth accounts"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.authentication_admin
    result = run_command(client, api_group, 'unlink_all_o_auth_accounts_admin', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
