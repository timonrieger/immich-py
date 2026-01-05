"""Generated CLI commands for Jobs tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="Jobs operations")

@app.command("create-job")
def create_job(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Create a manual job"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
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
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'get_queues_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("run-queue-command-legacy")
def run_queue_command_legacy(
    name: QueueName,
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Run jobs"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    kwargs['name'] = name
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.queue_command_dto import QueueCommandDto
        queue_command_dto = deserialize_request_body(json_data, QueueCommandDto)
        kwargs['queue_command_dto'] = queue_command_dto
    client = ctx.obj['client']
    api_group = client.jobs
    result = run_command(client, api_group, 'run_queue_command_legacy', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
