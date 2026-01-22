"""Generated CLI commands for System metadata tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.\n\n[link=https://api.immich.app/endpoints/system-metadata]Immich API documentation[/link]"""
)


@app.command("get-admin-onboarding", deprecated=False, rich_help_panel="API commands")
def get_admin_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve admin onboarding

    [link=https://api.immich.app/endpoints/system-metadata/getAdminOnboarding]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_admin_onboarding", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "get-reverse-geocoding-state", deprecated=False, rich_help_panel="API commands"
)
def get_reverse_geocoding_state(
    ctx: typer.Context,
) -> None:
    """Retrieve reverse geocoding state

    [link=https://api.immich.app/endpoints/system-metadata/getReverseGeocodingState]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_reverse_geocoding_state", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "get-version-check-state", deprecated=False, rich_help_panel="API commands"
)
def get_version_check_state(
    ctx: typer.Context,
) -> None:
    """Retrieve version check state

    [link=https://api.immich.app/endpoints/system-metadata/getVersionCheckState]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_version_check_state", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "update-admin-onboarding", deprecated=False, rich_help_panel="API commands"
)
def update_admin_onboarding(
    ctx: typer.Context,
    is_onboarded: bool = typer.Option(..., "--is-onboarded", help=""""""),
) -> None:
    """Update admin onboarding

    [link=https://api.immich.app/endpoints/system-metadata/updateAdminOnboarding]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["is_onboarded"], is_onboarded)
    admin_onboarding_update_dto = AdminOnboardingUpdateDto.model_validate(json_data)
    kwargs["admin_onboarding_update_dto"] = admin_onboarding_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "update_admin_onboarding", ctx, **kwargs
    )
    print_response(result, ctx)
