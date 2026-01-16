"""Generated CLI commands for Partners tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""A partner is a link with another user that allows sharing of assets between two users.

Docs: https://api.immich.app/endpoints/partners""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("create-partner")
def create_partner(
    ctx: typer.Context,
    shared_with_id: str = typer.Option(..., "--sharedWithId"),
) -> None:
    """Create a partner

    Docs: https://api.immich.app/endpoints/partners/createPartner
    """
    kwargs = {}
    has_flags = any([shared_with_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            shared_with_id,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["sharedWithId"], shared_with_id)
        from immich.client.models.partner_create_dto import PartnerCreateDto

        partner_create_dto = deserialize_request_body(json_data, PartnerCreateDto)
        kwargs["partner_create_dto"] = partner_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("create-partner-deprecated")
def create_partner_deprecated(
    ctx: typer.Context,
    id: str,
) -> None:
    """Create a partner

    Docs: https://api.immich.app/endpoints/partners/createPartnerDeprecated
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "create_partner_deprecated", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-partners")
def get_partners(
    ctx: typer.Context,
    direction: str = typer.Option(..., "--direction"),
) -> None:
    """Retrieve partners

    Docs: https://api.immich.app/endpoints/partners/getPartners
    """
    kwargs = {}
    kwargs["direction"] = direction
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "get_partners", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("remove-partner")
def remove_partner(
    ctx: typer.Context,
    id: str,
) -> None:
    """Remove a partner

    Docs: https://api.immich.app/endpoints/partners/removePartner
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "remove_partner", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-partner")
def update_partner(
    ctx: typer.Context,
    id: str,
    in_timeline: bool = typer.Option(..., "--inTimeline"),
) -> None:
    """Update a partner

    Docs: https://api.immich.app/endpoints/partners/updatePartner
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([in_timeline])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            in_timeline,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["inTimeline"], in_timeline)
        from immich.client.models.partner_update_dto import PartnerUpdateDto

        partner_update_dto = deserialize_request_body(json_data, PartnerUpdateDto)
        kwargs["partner_update_dto"] = partner_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.partners, "update_partner", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
