"""Generated CLI commands for System metadata tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.

Docs: https://api.immich.app/endpoints/system-metadata"""
)


@app.command("get-admin-onboarding", deprecated=False)
def get_admin_onboarding(
    ctx: typer.Context,
) -> None:
    """Retrieve admin onboarding

    Docs: https://api.immich.app/endpoints/system-metadata/getAdminOnboarding
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_admin_onboarding", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-reverse-geocoding-state", deprecated=False)
def get_reverse_geocoding_state(
    ctx: typer.Context,
) -> None:
    """Retrieve reverse geocoding state

    Docs: https://api.immich.app/endpoints/system-metadata/getReverseGeocodingState
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_reverse_geocoding_state", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-version-check-state", deprecated=False)
def get_version_check_state(
    ctx: typer.Context,
) -> None:
    """Retrieve version check state

    Docs: https://api.immich.app/endpoints/system-metadata/getVersionCheckState
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "get_version_check_state", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-admin-onboarding", deprecated=False)
def update_admin_onboarding(
    ctx: typer.Context,
    is_onboarded: Literal["true", "false"] = typer.Option(
        ..., "--is-onboarded", help="""Is admin onboarded"""
    ),
) -> None:
    """Update admin onboarding

    Docs: https://api.immich.app/endpoints/system-metadata/updateAdminOnboarding
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["is_onboarded"], is_onboarded.lower() == "true")
    from immich.client.models.admin_onboarding_update_dto import (
        AdminOnboardingUpdateDto,
    )

    admin_onboarding_update_dto = AdminOnboardingUpdateDto.model_validate(json_data)
    kwargs["admin_onboarding_update_dto"] = admin_onboarding_update_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "update_admin_onboarding", **kwargs
    )
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
