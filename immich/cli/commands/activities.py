"""Generated CLI commands for Activities tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""An activity is a like or a comment made by a user on an asset or album.\n\n[link=https://api.immich.app/endpoints/activities]Immich API documentation[/link]"""
)


@app.command("create-activity", deprecated=False, rich_help_panel="API commands")
def create_activity(
    ctx: typer.Context,
    album_id: str = typer.Option(..., "--album-id", help=""""""),
    asset_id: str | None = typer.Option(None, "--asset-id", help=""""""),
    comment: str | None = typer.Option(None, "--comment", help=""""""),
    type: str = typer.Option(..., "--type", help=""""""),
) -> None:
    """Create an activity

    [link=https://api.immich.app/endpoints/activities/createActivity]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["album_id"], album_id)
    if asset_id is not None:
        set_nested(json_data, ["asset_id"], asset_id)
    if comment is not None:
        set_nested(json_data, ["comment"], comment)
    set_nested(json_data, ["type"], type)
    activity_create_dto = ActivityCreateDto.model_validate(json_data)
    kwargs["activity_create_dto"] = activity_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.activities, "create_activity", ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-activity", deprecated=False, rich_help_panel="API commands")
def delete_activity(
    ctx: typer.Context,
    id: str = typer.Argument(..., help=""""""),
) -> None:
    """Delete an activity

    [link=https://api.immich.app/endpoints/activities/deleteActivity]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.activities, "delete_activity", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-activities", deprecated=False, rich_help_panel="API commands")
def get_activities(
    ctx: typer.Context,
    album_id: str = typer.Option(..., "--album-id", help=""""""),
    asset_id: str | None = typer.Option(None, "--asset-id", help=""""""),
    level: ReactionLevel | None = typer.Option(None, "--level", help=""""""),
    type: ReactionType | None = typer.Option(None, "--type", help=""""""),
    user_id: str | None = typer.Option(None, "--user-id", help=""""""),
) -> None:
    """List all activities

    [link=https://api.immich.app/endpoints/activities/getActivities]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["album_id"] = album_id
    if asset_id is not None:
        kwargs["asset_id"] = asset_id
    if level is not None:
        kwargs["level"] = level
    if type is not None:
        kwargs["type"] = type
    if user_id is not None:
        kwargs["user_id"] = user_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.activities, "get_activities", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "get-activity-statistics", deprecated=False, rich_help_panel="API commands"
)
def get_activity_statistics(
    ctx: typer.Context,
    album_id: str = typer.Option(..., "--album-id", help=""""""),
    asset_id: str | None = typer.Option(None, "--asset-id", help=""""""),
) -> None:
    """Retrieve activity statistics

    [link=https://api.immich.app/endpoints/activities/getActivityStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["album_id"] = album_id
    if asset_id is not None:
        kwargs["asset_id"] = asset_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.activities, "get_activity_statistics", ctx, **kwargs
    )
    print_response(result, ctx)
