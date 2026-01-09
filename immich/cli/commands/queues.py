"""Generated CLI commands for Queues tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.. https://api.immich.app/endpoints/queues', context_settings={'help_option_names': ['-h', '--help']})

@app.command("empty-queue")
def empty_queue(
    ctx: typer.Context,
    name: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Empty a queue"""
    kwargs = {}
    kwargs['name'] = name
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.queue_delete_dto import QueueDeleteDto
        queue_delete_dto = deserialize_request_body(json_data, QueueDeleteDto)
        kwargs['queue_delete_dto'] = queue_delete_dto
    client = ctx.obj['client']
    api_group = client.queues
    result = run_command(client, api_group, 'empty_queue', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-queue")
def get_queue(
    ctx: typer.Context,
    name: str,
) -> None:
    """Retrieve a queue"""
    kwargs = {}
    kwargs['name'] = name
    client = ctx.obj['client']
    api_group = client.queues
    result = run_command(client, api_group, 'get_queue', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-queue-jobs")
def get_queue_jobs(
    ctx: typer.Context,
    name: str,
    status: list[str] | None = typer.Option(None, "--status"),
) -> None:
    """Retrieve queue jobs"""
    kwargs = {}
    kwargs['name'] = name
    if status is not None:
        kwargs['status'] = status
    client = ctx.obj['client']
    api_group = client.queues
    result = run_command(client, api_group, 'get_queue_jobs', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-queues")
def get_queues(
    ctx: typer.Context,
) -> None:
    """List all queues"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.queues
    result = run_command(client, api_group, 'get_queues', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-queue")
def update_queue(
    ctx: typer.Context,
    name: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Update a queue"""
    kwargs = {}
    kwargs['name'] = name
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.queue_update_dto import QueueUpdateDto
        queue_update_dto = deserialize_request_body(json_data, QueueUpdateDto)
        kwargs['queue_update_dto'] = queue_update_dto
    client = ctx.obj['client']
    api_group = client.queues
    result = run_command(client, api_group, 'update_queue', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
