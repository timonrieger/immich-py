"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.\n\n[link=https://api.immich.app/endpoints/jobs]Immich API documentation[/link]"""
)


@app.command("create-job", deprecated=False, rich_help_panel="API commands")
def create_job(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help=""""""),
) -> None:
    """Create a manual job

    [link=https://api.immich.app/endpoints/jobs/createJob]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["name"], name)
    job_create_dto = JobCreateDto.model_validate(json_data)
    kwargs["job_create_dto"] = job_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.jobs, "create_job", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-queues-legacy", deprecated=True, rich_help_panel="API commands")
def get_queues_legacy(
    ctx: typer.Context,
) -> None:
    """Retrieve queue counts and status

    [link=https://api.immich.app/endpoints/jobs/getQueuesLegacy]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.jobs, "get_queues_legacy", ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "run-queue-command-legacy", deprecated=True, rich_help_panel="API commands"
)
def run_queue_command_legacy(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    command: str = typer.Option(..., "--command", help=""""""),
    force: Literal["true", "false"] | None = typer.Option(None, "--force", help=""""""),
) -> None:
    """Run jobs

    [link=https://api.immich.app/endpoints/jobs/runQueueCommandLegacy]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    set_nested(json_data, ["command"], command)
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    queue_command_dto = QueueCommandDto.model_validate(json_data)
    kwargs["queue_command_dto"] = queue_command_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.jobs, "run_queue_command_legacy", ctx, **kwargs)
    print_response(result, ctx)
