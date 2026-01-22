"""Generated CLI commands for Queues tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.\n\n[link=https://api.immich.app/endpoints/queues]Immich API documentation[/link]"""
)


@app.command("empty-queue", deprecated=False, rich_help_panel="API commands")
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

    [link=https://api.immich.app/endpoints/queues/emptyQueue]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    if failed is not None:
        set_nested(json_data, ["failed"], failed.lower() == "true")
    queue_delete_dto = QueueDeleteDto.model_validate(json_data)
    kwargs["queue_delete_dto"] = queue_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.queues, "empty_queue", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-queue", deprecated=False, rich_help_panel="API commands")
def get_queue(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a queue

    [link=https://api.immich.app/endpoints/queues/getQueue]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queue", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-queue-jobs", deprecated=False, rich_help_panel="API commands")
def get_queue_jobs(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    status: list[QueueJobStatus] | None = typer.Option(None, "--status", help=""""""),
) -> None:
    """Retrieve queue jobs

    [link=https://api.immich.app/endpoints/queues/getQueueJobs]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    if status is not None:
        kwargs["status"] = status
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queue_jobs", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-queues", deprecated=False, rich_help_panel="API commands")
def get_queues(
    ctx: typer.Context,
) -> None:
    """List all queues

    [link=https://api.immich.app/endpoints/queues/getQueues]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queues", ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-queue", deprecated=False, rich_help_panel="API commands")
def update_queue(
    ctx: typer.Context,
    name: QueueName = typer.Argument(..., help=""""""),
    is_paused: Literal["true", "false"] | None = typer.Option(
        None, "--is-paused", help=""""""
    ),
) -> None:
    """Update a queue

    [link=https://api.immich.app/endpoints/queues/updateQueue]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["name"] = name
    if is_paused is not None:
        set_nested(json_data, ["is_paused"], is_paused.lower() == "true")
    queue_update_dto = QueueUpdateDto.model_validate(json_data)
    kwargs["queue_update_dto"] = queue_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.queues, "update_queue", ctx, **kwargs)
    print_response(result, ctx)
