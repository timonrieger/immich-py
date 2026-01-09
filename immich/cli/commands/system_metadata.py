"""Generated CLI commands for System metadata tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.. https://api.immich.app/endpoints/system-metadata', context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-admin-onboarding")
def get_admin_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve admin onboarding"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'get_admin_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-reverse-geocoding-state")
def get_reverse_geocoding_state(
    ctx: typer.Context,
) -> None:
    """Retrieve reverse geocoding state"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'get_reverse_geocoding_state', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-version-check-state")
def get_version_check_state(
    ctx: typer.Context,
) -> None:
    """Retrieve version check state"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'get_version_check_state', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-admin-onboarding")
def update_admin_onboarding(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update admin onboarding"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
        admin_onboarding_update_dto = deserialize_request_body(json_data, AdminOnboardingUpdateDto)
        kwargs['admin_onboarding_update_dto'] = admin_onboarding_update_dto
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'update_admin_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
