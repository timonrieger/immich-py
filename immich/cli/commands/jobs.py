"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

Docs: https://api.immich.app/endpoints/jobs""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("create-job")
def create_job(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    name: str = typer.Option(..., "--name", help="""Job name"""),
) -> None:
    """Create a manual job

Docs: https://api.immich.app/endpoints/jobs/createJob
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([name])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.job_create_dto import JobCreateDto
        job_create_dto = deserialize_request_body(json_data, JobCreateDto)
        kwargs['job_create_dto'] = job_create_dto
    elif any([
        name,
    ]):
        # Build body from dotted flags
        json_data = {}
        if name is None:
            raise SystemExit("Error: --name is required")
        set_nested(json_data, ['name'], name)
        if json_data:
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
    """Retrieve queue counts and status

Docs: https://api.immich.app/endpoints/jobs/getQueuesLegacy
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'get_queues_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("run-queue-command-legacy")
def run_queue_command_legacy(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="""Queue name"""),
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    command: str = typer.Option(..., "--command", help="""Queue command to execute"""),
    force: bool | None = typer.Option(None, "--force", help="""Force the command execution (if applicable)"""),
) -> None:
    """Run jobs

Docs: https://api.immich.app/endpoints/jobs/runQueueCommandLegacy
    """
    kwargs = {}
    kwargs['name'] = name
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([command, force])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.queue_command_dto import QueueCommandDto
        queue_command_dto = deserialize_request_body(json_data, QueueCommandDto)
        kwargs['queue_command_dto'] = queue_command_dto
    elif any([
        command,
        force,
    ]):
        # Build body from dotted flags
        json_data = {}
        if command is None:
            raise SystemExit("Error: --command is required")
        set_nested(json_data, ['command'], command)
        if force is not None:
            set_nested(json_data, ['force'], force)
        if json_data:
            from immich.client.models.queue_command_dto import QueueCommandDto
            queue_command_dto = deserialize_request_body(json_data, QueueCommandDto)
            kwargs['queue_command_dto'] = queue_command_dto
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'run_queue_command_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
