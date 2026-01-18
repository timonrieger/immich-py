"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.\n\nDocs: https://api.immich.app/endpoints/jobs"""
)


@app.command("create-job", deprecated=False)
def create_job(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help=""""""),
) -> None:
    """Create a manual job

    Docs: https://api.immich.app/endpoints/jobs/createJob
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["name"], name)
    from immich.client.models.job_create_dto import JobCreateDto

    job_create_dto = JobCreateDto.model_validate(json_data)
    kwargs["job_create_dto"] = job_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.jobs, "create_job", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-queues-legacy", deprecated=True)
def get_queues_legacy(
    ctx: typer.Context,
) -> None:
    """Retrieve queue counts and status

    Docs: https://api.immich.app/endpoints/jobs/getQueuesLegacy
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.jobs, "get_queues_legacy", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("run-queue-command-legacy", deprecated=True)
def run_queue_command_legacy(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    command: str = typer.Option(..., "--command", help=""""""),
    force: Literal["true", "false"] | None = typer.Option(None, "--force", help=""""""),
) -> None:
    """Run jobs

    Docs: https://api.immich.app/endpoints/jobs/runQueueCommandLegacy
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    set_nested(json_data, ["command"], command)
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    from immich.client.models.queue_command_dto import QueueCommandDto

    queue_command_dto = QueueCommandDto.model_validate(json_data)
    kwargs["queue_command_dto"] = queue_command_dto
    client = ctx.obj["client"]
    result = run_command(client, client.jobs, "run_queue_command_legacy", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
