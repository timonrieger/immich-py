"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Partners operations")

@app.command("create-partner")
def create_partner(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a partner"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    id: str,
    ctx: typer.Context,
) -> None:
    """Create a partner"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'create_partner_deprecated', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-partners")
def get_partners(
    direction: PartnerDirection = typer.Option(..., "--direction"),
    ctx: typer.Context,
) -> None:
    """Retrieve partners"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['direction'] = direction
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'get_partners', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("remove-partner")
def remove_partner(
    id: str,
    ctx: typer.Context,
) -> None:
    """Remove a partner"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'remove_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-partner")
def update_partner(
    id: str,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update a partner"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['id'] = id
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.partner_update_dto import PartnerUpdateDto
        partner_update_dto = deserialize_request_body(json_data, PartnerUpdateDto)
        kwargs['partner_update_dto'] = partner_update_dto
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'update_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
