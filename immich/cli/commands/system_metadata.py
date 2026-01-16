"""Generated CLI commands for System metadata tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.

Docs: https://api.immich.app/endpoints/system-metadata""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("get-admin-onboarding")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-reverse-geocoding-state")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-version-check-state")
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-admin-onboarding")
def update_admin_onboarding(
    ctx: typer.Context,
    is_onboarded: bool = typer.Option(..., "--isOnboarded"),
) -> None:
    """Update admin onboarding

    Docs: https://api.immich.app/endpoints/system-metadata/updateAdminOnboarding
    """
    kwargs = {}
    has_flags = any([is_onboarded])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            is_onboarded,
        ]
    ):
        json_data = {}
        set_nested(json_data, ["isOnboarded"], is_onboarded)
        from immich.client.models.admin_onboarding_update_dto import (
            AdminOnboardingUpdateDto,
        )

        admin_onboarding_update_dto = deserialize_request_body(
            json_data, AdminOnboardingUpdateDto
        )
        kwargs["admin_onboarding_update_dto"] = admin_onboarding_update_dto
    client = ctx.obj["client"]
    result = run_command(
        client, client.system_metadata, "update_admin_onboarding", **kwargs
    )
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
