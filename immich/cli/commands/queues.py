"""Generated CLI commands for Queues tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import (
    deserialize_request_body,
    print_response,
    run_command,
    set_nested,
)

app = typer.Typer(
    help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

Docs: https://api.immich.app/endpoints/queues""",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command("empty-queue")
def empty_queue(
    ctx: typer.Context,
    name: str,
    failed: bool | None = typer.Option(
        None,
        "--failed",
        help="""If true, will also remove failed jobs from the queue.""",
    ),
) -> None:
    """Empty a queue

    Docs: https://api.immich.app/endpoints/queues/emptyQueue
    """
    kwargs = {}
    kwargs["name"] = name
    has_flags = any([failed])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            failed,
        ]
    ):
        json_data = {}
        if failed is not None:
            set_nested(json_data, ["failed"], failed)
        from immich.client.models.queue_delete_dto import QueueDeleteDto

        queue_delete_dto = deserialize_request_body(json_data, QueueDeleteDto)
        kwargs["queue_delete_dto"] = queue_delete_dto
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "empty_queue", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-queue")
def get_queue(
    ctx: typer.Context,
    name: str,
) -> None:
    """Retrieve a queue

    Docs: https://api.immich.app/endpoints/queues/getQueue
    """
    kwargs = {}
    kwargs["name"] = name
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queue", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-queue-jobs")
def get_queue_jobs(
    ctx: typer.Context,
    name: str,
    status: list[str] | None = typer.Option(None, "--status"),
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
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-queues")
def get_queues(
    ctx: typer.Context,
) -> None:
    """List all queues

    Docs: https://api.immich.app/endpoints/queues/getQueues
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "get_queues", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-queue")
def update_queue(
    ctx: typer.Context,
    name: str,
    is_paused: bool | None = typer.Option(None, "--isPaused"),
) -> None:
    """Update a queue

    Docs: https://api.immich.app/endpoints/queues/updateQueue
    """
    kwargs = {}
    kwargs["name"] = name
    has_flags = any([is_paused])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any(
        [
            is_paused,
        ]
    ):
        json_data = {}
        if is_paused is not None:
            set_nested(json_data, ["isPaused"], is_paused)
        from immich.client.models.queue_update_dto import QueueUpdateDto

        queue_update_dto = deserialize_request_body(json_data, QueueUpdateDto)
        kwargs["queue_update_dto"] = queue_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.queues, "update_queue", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
