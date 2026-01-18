import typer
from immich._internal.consts import CONFIG_FILE
from immich._internal.cli.utils import (
    check_config,
    get_path,
    load_config,
    mask,
    set_path,
    write_config,
)

app = typer.Typer(
    help="""Configure the CLI with server details, profiles, and request settings."""
)


@app.command("set")
def set(
    key: str = typer.Argument(..., help="Dot-separated config key"),
    value: str = typer.Argument(..., help="Value to set"),
):
    """Set a value in the config file."""
    data = load_config(ensure_exists=True)
    set_path(data, key, value)
    write_config(data)


@app.command("get")
def get(
    key: str = typer.Argument(..., help="The key to get from the config"),
    show_secrets: bool = typer.Option(
        False,
        "--show-secrets",
        help="Show secret values without redaction",
    ),
):
    """Get a value from the config file. Secrets are redacted by default."""
    check_config()
    data = load_config()
    value = get_path(data, key)
    if not show_secrets:
        value = mask(value, key=key)
    typer.echo(value)


@app.command("reset")
def reset(
    _yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Skip confirmation",
        prompt="Are you sure you want to reset the config? This will permanently delete the config file",
    ),
):
    """Reset the configuration by deleting the config file."""
    check_config()
    CONFIG_FILE.unlink()
    typer.echo("Config file removed")
