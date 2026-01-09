"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='A partner is a link with another user that allows sharing of assets between two users.. https://api.immich.app/endpoints/partners', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-partner")
def create_partner(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a partner"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.partner_create_dto import PartnerCreateDto
        partner_create_dto = deserialize_request_body(json_data, PartnerCreateDto)
        kwargs['partner_create_dto'] = partner_create_dto
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'create_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("create-partner-deprecated")
def create_partner_deprecated(
    ctx: typer.Context,
    id: str,
) -> None:
    """Create a partner"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'create_partner_deprecated', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-partners")
def get_partners(
    ctx: typer.Context,
    direction: str = typer.Option(..., "--direction"),
) -> None:
    """Retrieve partners"""
    kwargs = {}
    kwargs['direction'] = direction
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'get_partners', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-partner")
def remove_partner(
    ctx: typer.Context,
    id: str,
) -> None:
    """Remove a partner"""
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'remove_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-partner")
def update_partner(
    ctx: typer.Context,
    id: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update a partner"""
    kwargs = {}
    kwargs['id'] = id
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.partner_update_dto import PartnerUpdateDto
        partner_update_dto = deserialize_request_body(json_data, PartnerUpdateDto)
        kwargs['partner_update_dto'] = partner_update_dto
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'update_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
