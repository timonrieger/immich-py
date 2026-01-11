"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""A partner is a link with another user that allows sharing of assets between two users.

Docs: https://api.immich.app/endpoints/partners""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-partner")
def create_partner(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    shared_with_id: str = typer.Option(..., "--sharedWithId", help="""User ID to share with"""),
) -> None:
    """Create a partner

Docs: https://api.immich.app/endpoints/partners/createPartner
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([shared_with_id])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.partner_create_dto import PartnerCreateDto
        partner_create_dto = deserialize_request_body(json_data, PartnerCreateDto)
        kwargs['partner_create_dto'] = partner_create_dto
    elif any([
        shared_with_id,
    ]):
        # Build body from dotted flags
        json_data = {}
        if shared_with_id is None:
            raise SystemExit("Error: --sharedWithId is required")
        set_nested(json_data, ['sharedWithId'], shared_with_id)
        if json_data:
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
    id: str = typer.Argument(..., help="""User ID to share with"""),
) -> None:
    """Create a partner

Docs: https://api.immich.app/endpoints/partners/createPartnerDeprecated
    """
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
    direction: str = typer.Option(..., "--direction", help="""Partner direction"""),
) -> None:
    """Retrieve partners

Docs: https://api.immich.app/endpoints/partners/getPartners
    """
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
    id: str = typer.Argument(..., help="""Partner ID"""),
) -> None:
    """Remove a partner

Docs: https://api.immich.app/endpoints/partners/removePartner
    """
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
    id: str = typer.Argument(..., help="""Partner ID"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    in_timeline: bool = typer.Option(..., "--inTimeline", help="""Show partner assets in timeline"""),
) -> None:
    """Update a partner

Docs: https://api.immich.app/endpoints/partners/updatePartner
    """
    kwargs = {}
    kwargs['id'] = id
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([in_timeline])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.partner_update_dto import PartnerUpdateDto
        partner_update_dto = deserialize_request_body(json_data, PartnerUpdateDto)
        kwargs['partner_update_dto'] = partner_update_dto
    elif any([
        in_timeline,
    ]):
        # Build body from dotted flags
        json_data = {}
        if in_timeline is None:
            raise SystemExit("Error: --inTimeline is required")
        set_nested(json_data, ['inTimeline'], in_timeline)
        if json_data:
            from immich.client.models.partner_update_dto import PartnerUpdateDto
            partner_update_dto = deserialize_request_body(json_data, PartnerUpdateDto)
            kwargs['partner_update_dto'] = partner_update_dto
    client = ctx.obj['client']
    api_group = client.partners
    result = run_command(client, api_group, 'update_partner', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
