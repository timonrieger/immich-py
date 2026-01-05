"""Generated CLI commands for System metadata tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import typer
from typer import Context

app = typer.Typer(help="System metadata operations")

@app.command("get-admin-onboarding")
def get_admin_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve admin onboarding"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'get_version_check_state', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-admin-onboarding")
def update_admin_onboarding(
    ctx: typer.Context,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
) -> None:
    """Update admin onboarding"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
        admin_onboarding_update_dto = deserialize_request_body(json_data, AdminOnboardingUpdateDto)
        kwargs['admin_onboarding_update_dto'] = admin_onboarding_update_dto
    client = ctx.obj['client']
    api_group = client.system_metadata
    result = run_command(client, api_group, 'update_admin_onboarding', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
