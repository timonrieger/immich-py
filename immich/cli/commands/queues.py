"""Generated CLI commands for Queues tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.\n\nDocs: https://api.immich.app/endpoints/queues"""
)


@app.command("empty-queue", deprecated=False)
def empty_queue(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    failed: Literal["true", "false"] | None = typer.Option(
        None,
        "--failed",
        help="""If true, will also remove failed jobs from the queue.""",
    ),
) -> None:
    """Empty a queue

    Docs: https://api.immich.app/endpoints/queues/emptyQueue
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    if failed is not None:
        set_nested(json_data, ["failed"], failed.lower() == "true")
    from immich.client.models.queue_delete_dto import QueueDeleteDto

    queue_delete_dto = QueueDeleteDto.model_validate(json_data)
    kwargs["queue_delete_dto"] = queue_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "empty_queue", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-queue", deprecated=False)
def get_queue(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a queue

    Docs: https://api.immich.app/endpoints/queues/getQueue
    """
    kwargs = {}
    kwargs["name"] = name
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queue", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-queue-jobs", deprecated=False)
def get_queue_jobs(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    status: list[QueueJobStatus] | None = typer.Option(None, "--status", help=""""""),
) -> None:
    """Retrieve queue jobs

    Docs: https://api.immich.app/endpoints/queues/getQueueJobs
    """
    kwargs = {}
    kwargs["name"] = name
    if status is not None:
        kwargs["status"] = status
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queue_jobs", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("get-queues", deprecated=False)
def get_queues(
    ctx: typer.Context,
) -> None:
    """List all queues

    Docs: https://api.immich.app/endpoints/queues/getQueues
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queues", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)


@app.command("update-queue", deprecated=False)
def update_queue(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    is_paused: Literal["true", "false"] | None = typer.Option(
        None, "--is-paused", help=""""""
    ),
) -> None:
    """Update a queue

    Docs: https://api.immich.app/endpoints/queues/updateQueue
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    if is_paused is not None:
        set_nested(json_data, ["is_paused"], is_paused.lower() == "true")
    from immich.client.models.queue_update_dto import QueueUpdateDto

    queue_update_dto = QueueUpdateDto.model_validate(json_data)
    kwargs["queue_update_dto"] = queue_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "update_queue", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
