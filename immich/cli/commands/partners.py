"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A partner is a link with another user that allows sharing of assets between two users.\n\nDocs: https://api.immich.app/endpoints/partners"""
)


@app.command("create-partner", deprecated=False, rich_help_panel="API commands")
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
    partner_create_dto = PartnerCreateDto.model_validate(json_data)
    kwargs["partner_create_dto"] = partner_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner", **kwargs)
    print_response(result, ctx)


@app.command(
    "create-partner-deprecated", deprecated=True, rich_help_panel="API commands"
)
def create_partner_deprecated(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Create a partner

    Docs: https://api.immich.app/endpoints/partners/createPartnerDeprecated
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner_deprecated", **kwargs)
    print_response(result, ctx)


@app.command("get-partners", deprecated=False, rich_help_panel="API commands")
def get_partners(
    ctx: typer.Context,
    direction: PartnerDirection = typer.Option(..., "--direction", help=""""""),
) -> None:
    """Retrieve partners

    Docs: https://api.immich.app/endpoints/partners/getPartners
    """
    kwargs = {}
    kwargs["direction"] = direction
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.partners, "get_partners", **kwargs)
    print_response(result, ctx)


@app.command("remove-partner", deprecated=False, rich_help_panel="API commands")
def remove_partner(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Remove a partner

    Docs: https://api.immich.app/endpoints/partners/removePartner
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.partners, "remove_partner", **kwargs)
    print_response(result, ctx)


@app.command("update-partner", deprecated=False, rich_help_panel="API commands")
def update_partner(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
    in_timeline: bool = typer.Option(..., "--in-timeline", help=""""""),
) -> None:
    """Update a partner

    Docs: https://api.immich.app/endpoints/partners/updatePartner
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["in_timeline"], in_timeline)
    partner_update_dto = PartnerUpdateDto.model_validate(json_data)
    kwargs["partner_update_dto"] = partner_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.partners, "update_partner", **kwargs)
    print_response(result, ctx)
