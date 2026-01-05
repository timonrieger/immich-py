"""Generated CLI commands for System config tag (auto-generated, do not edit)."""

from __future__ import annotations

from pathlib import Path
import typer
from typer import Context

app = typer.Typer(help="System config operations")

@app.command("get-config")
def get_config(
    ctx: typer.Context,
) -> None:
    """Get system configuration"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-config-defaults")
def get_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get system configuration defaults"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config_defaults', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-storage-template-options")
def get_storage_template_options(
    ctx: typer.Context,
) -> None:
    """Get storage template options"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_storage_template_options', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-config")
def update_config(
    json_path: Path | None = typer.Option(None, "--json", help="Path to JSON file with request body"),
    ctx: typer.Context,
) -> None:
    """Update system configuration"""
    from pathlib import Path
    from immich.cli.runtime import load_json_file, load_file_bytes, deserialize_request_body, print_response, run_command
    kwargs = {}
    if json_path is not None:
        json_data = load_json_file(json_path)
        from immich.client.models.system_config_dto import SystemConfigDto
        system_config_dto = deserialize_request_body(json_data, SystemConfigDto)
        kwargs['system_config_dto'] = system_config_dto
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'update_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
