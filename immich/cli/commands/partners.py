"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A partner is a link with another user that allows sharing of assets between two users.\n\nDocs: https://api.immich.app/endpoints/partners"""
)


@app.command("create-partner", deprecated=False)
def create_partner(
    ctx: typer.Context,
    shared_with_id: str = typer.Option(..., "--shared-with-id", help=""""""),
) -> None:
    """Create a partner

    Docs: https://api.immich.app/endpoints/partners/createPartner
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["shared_with_id"], shared_with_id)
    from immich.client.models.partner_create_dto import PartnerCreateDto

    partner_create_dto = PartnerCreateDto.model_validate(json_data)
    kwargs["partner_create_dto"] = partner_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("create-partner-deprecated", deprecated=True)
def create_partner_deprecated(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Create a partner

    Docs: https://api.immich.app/endpoints/partners/createPartnerDeprecated
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner_deprecated", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-partners", deprecated=False)
def get_partners(
    ctx: typer.Context,
    direction: PartnerDirection = typer.Option(..., "--direction", help=""""""),
) -> None:
    """Retrieve partners

    Docs: https://api.immich.app/endpoints/partners/getPartners
    """
    kwargs = {}
    kwargs["direction"] = direction
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "get_partners", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("remove-partner", deprecated=False)
def remove_partner(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Remove a partner

    Docs: https://api.immich.app/endpoints/partners/removePartner
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "remove_partner", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-partner", deprecated=False)
def update_partner(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    in_timeline: Literal["true", "false"] = typer.Option(
        ..., "--in-timeline", help=""""""
    ),
) -> None:
    """Update a partner

    Docs: https://api.immich.app/endpoints/partners/updatePartner
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["in_timeline"], in_timeline.lower() == "true")
    from immich.client.models.partner_update_dto import PartnerUpdateDto

    partner_update_dto = PartnerUpdateDto.model_validate(json_data)
    kwargs["partner_update_dto"] = partner_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "update_partner", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
