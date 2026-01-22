import typer
from immich.cli.consts import CONFIG_FILE
from immich.cli.utils import (
    check_config,
    get_path,
    load_config,
    mask,
    print_,
    set_path,
    write_config,
)

app = typer.Typer(
    help="""Configure the CLI with server details, profiles, and request settings."""
)


@app.command("set")
def set(
    key: str = typer.Argument(..., help="Dot-separated config key"),
    value: str = typer.Option(
        ...,
        "--value",
        "-v",
        help="Value to set (prompts if not provided)",
        prompt="Enter the value",
    ),
) -> None:  # pragma: no cover
    """Set a value in the config file."""
    data = load_config()
    set_path(data, key, value)
    write_config(data)
    print_(f"Successfully set '{key}'!", type="success")


@app.command("get")
def get(
    ctx: typer.Context,
    key: str = typer.Argument(..., help="The key to get from the config"),
    show_secrets: bool = typer.Option(
        False,
        "--show-secrets",
        help="Show secret values without redaction",
    ),
) -> None:  # pragma: no cover
    """Get a value from the config file. Secrets are redacted by default."""
    check_config()
    data = load_config()
    value = get_path(data, key)
    if not show_secrets:
        value = mask(value, key=key)
    print_(message=value, type="text", ctx=ctx)


@app.command("reset")
def reset(
    ctx: typer.Context,
    _yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Skip confirmation",
        prompt="Are you sure you want to reset the config? This will permanently delete the config file",
    ),
) -> None:  # pragma: no cover
    """Reset the configuration by deleting the config file."""
    check_config()
    CONFIG_FILE.unlink()
    print_("Config file removed", type="success", ctx=ctx)


@app.command("open")
def open() -> None:  # pragma: no cover
    """Open the config file in the default editor."""
    check_config()
    typer.launch(str(CONFIG_FILE), locate=True)
