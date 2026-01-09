"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command

app = typer.Typer(help='Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.. https://api.immich.app/endpoints/jobs', context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-job")
def create_job(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Create a manual job"""
    kwargs = {}
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.job_create_dto import JobCreateDto
        job_create_dto = deserialize_request_body(json_data, JobCreateDto)
        kwargs['job_create_dto'] = job_create_dto
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'create_job', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-queues-legacy")
def get_queues_legacy(
    ctx: typer.Context,
) -> None:
    """Retrieve queue counts and status"""
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'get_queues_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("run-queue-command-legacy")
def run_queue_command_legacy(
    ctx: typer.Context,
    name: str,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
) -> None:
    """Run jobs"""
    kwargs = {}
    kwargs['name'] = name
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.queue_command_dto import QueueCommandDto
        queue_command_dto = deserialize_request_body(json_data, QueueCommandDto)
        kwargs['queue_command_dto'] = queue_command_dto
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'run_queue_command_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
