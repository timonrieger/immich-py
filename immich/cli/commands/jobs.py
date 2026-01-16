"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

app = typer.Typer(help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

Docs: https://api.immich.app/endpoints/jobs""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-job")
def create_job(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name"),
) -> None:
    """Create a manual job

Docs: https://api.immich.app/endpoints/jobs/createJob
    """
    kwargs = {}
    has_flags = any([name])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([name]):
        json_data = {}
        set_nested(json_data, ['name'], name)
        from immich.client.models.job_create_dto import JobCreateDto
        job_create_dto = deserialize_request_body(json_data, JobCreateDto)
        kwargs['job_create_dto'] = job_create_dto
    client = ctx.obj['client']
    result = run_command(client, client.jobs, 'create_job', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-queues-legacy")
def get_queues_legacy(
    ctx: typer.Context,
) -> None:
    """Retrieve queue counts and status

Docs: https://api.immich.app/endpoints/jobs/getQueuesLegacy
    """
    kwargs = {}
    client = ctx.obj['client']
    result = run_command(client, client.jobs, 'get_queues_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("run-queue-command-legacy")
def run_queue_command_legacy(
    ctx: typer.Context,
    name: str,
    command: str = typer.Option(..., "--command"),
    force: bool | None = typer.Option(None, "--force"),
) -> None:
    """Run jobs

Docs: https://api.immich.app/endpoints/jobs/runQueueCommandLegacy
    """
    kwargs = {}
    kwargs['name'] = name
    has_flags = any([command, force])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([command, force]):
        json_data = {}
        set_nested(json_data, ['command'], command)
        if force is not None:
            set_nested(json_data, ['force'], force)
        from immich.client.models.queue_command_dto import QueueCommandDto
        queue_command_dto = deserialize_request_body(json_data, QueueCommandDto)
        kwargs['queue_command_dto'] = queue_command_dto
    client = ctx.obj['client']
    result = run_command(client, client.jobs, 'run_queue_command_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
