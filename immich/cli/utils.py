from typing import Any, Optional, cast, overload
import json

from rich import print as print_rich, print_json
from rich.table import Table
import rtoml
import typer

from immich.cli.consts import CONFIG_FILE, DEFAULT_FORMAT, SECRET_KEYS
from immich.cli.types import ClientConfig, FormatMode, PrintType


def set_path(data: dict[str, Any], path: str, value: Any) -> None:
    """
    Set a nested dictionary value using a path list.

    Example: set_path({}, 'user.name', 'John') -> {'user': {'name': 'John'}}
    """
    parts = path.split(".")
    cur = data
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = value


def get_path(data: dict[str, Any], path: str) -> Any:
    """
    Get a nested dictionary value using a path list.
    """
    parts = path.split(".")
    cur = data
    for p in parts:
        cur = cur[p]
    return cur


def load_config() -> dict[str, Any]:
    """
    Load the config file. Returns an empty dict if the file does not exist.
    """
    if not CONFIG_FILE.exists():
        return {}
    return rtoml.load(CONFIG_FILE, none_value="")


def write_config(data: dict[str, Any]) -> None:
    """
    Write the config data to the config file and set permissions.
    """
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with CONFIG_FILE.open("w") as f:
        rtoml.dump(data, f, none_value="")
    CONFIG_FILE.chmod(0o600)


def check_config() -> None:
    """
    Check if the config file exists.
    """
    if not CONFIG_FILE.exists():
        print_(
            "Config file does not exist. Run [bold]immich config set[/bold] to create it.",
            type="error",
        )
        raise typer.Exit(code=1)


def resolve_client_config(
    config: ClientConfig, profile: str, profile_explicit: bool = False
) -> ClientConfig:
    """
    Resolve the client config from the config file.

    :param config: The config to resolve
    :param profile: The profile to use
    :param profile_explicit: Whether the profile was explicitly set by the user
    :raises typer.Exit: If the profile is not found in the config
    :return: The resolved config
    """
    data = load_config()
    profiles: dict[str, Any] = data.get("profiles", {})

    if profile_explicit and profile not in profiles:
        print_(
            f"Profile '{profile}' not found. Run immich config set --profile {profile}.",
            type="error",
        )
        raise typer.Exit(code=1)

    profile_data = profiles.get(profile, {})

    return ClientConfig(
        api_key=config.api_key or profile_data.get("api_key"),
        access_token=config.access_token or profile_data.get("access_token"),
        base_url=config.base_url or profile_data.get("base_url"),
    )


def _is_secret_key(key: str) -> bool:
    """Check if a key indicates a secret value."""
    return any(secret in key.lower() for secret in SECRET_KEYS)


def _redact_secret(secret: str, start: int = 3, end: int = 3) -> str:
    """
    Redact a secret by showing only the first `start` and last `end` characters.

    :param secret: The secret string to redact
    :param start: Number of characters to show at the start (default: 3)
    :param end: Number of characters to show at the end (default: 3)
    :return: The redacted secret string
    """
    if not secret:
        return ""

    length = len(secret)
    if length <= start + end:
        return "*" * length

    return secret[:start] + "*" * (length - start - end) + secret[-end:]


@overload
def mask(secret: str, start: int = 3, end: int = 3) -> str: ...


@overload
def mask(obj: Any, start: int = 3, end: int = 3, key: Optional[str] = None) -> Any: ...


def mask(obj: Any, start: int = 3, end: int = 3, key: Optional[str] = None) -> Any:
    """
    Recursively mask secret values in nested dictionaries and lists.

    :param obj: The object to mask (dict, list, or any other type)
    :param start: Number of characters to show at the start (default: 3)
    :param end: Number of characters to show at the end (default: 3)
    :param key: Optional key path for top-level values to check if they're secrets
    :return: The masked object with secrets redacted using _redact_secret
    """
    if isinstance(obj, dict):
        return {
            k: (
                _redact_secret(v, start, end)
                if _is_secret_key(k) and isinstance(v, str)
                else mask(v, start, end, k)
            )
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [mask(v, start, end) for v in obj]
    if isinstance(obj, str):
        if key is None or _is_secret_key(key):
            return _redact_secret(obj, start, end)
    return obj


def _print_table(data: Any) -> None:  # pragma: no cover
    """
    Print data as a table using rich.
    For dicts: creates a table with key/value columns.
    For lists: prints multiple tables.
    """
    if isinstance(data, list):
        for item in data:
            _print_table(item)
    elif isinstance(data, dict):
        _print_dict_table(data)
    else:
        print_rich(str(data))


def _print_dict_table(data: dict[str, Any]) -> None:  # pragma: no cover
    """Print a dictionary as a table with key and value columns."""
    table = Table(show_header=True, header_style="bold")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")

    for key, value in data.items():
        table.add_row(key, str(value))

    print_rich(table)


def print_(
    message: str,
    *,
    type: PrintType,
    ctx: Optional[typer.Context] = None,
) -> None:
    """
    Print a message in the given format as a rich print or a plain print.
    :param message: The message to print
    :param type: The type of the message
    :param ctx: The context to use
    """
    match type:
        case "json":
            try:
                format_mode = cast(FormatMode, ctx.obj.get("format", DEFAULT_FORMAT))  # type: ignore[possibly-missing-attribute]
            except (AttributeError, KeyError):
                format_mode = DEFAULT_FORMAT
            match format_mode:
                case "pretty":
                    print_json(message)
                case "json":
                    print(message)
                case "table":  # pragma: no cover
                    try:
                        data = json.loads(message)
                        _print_table(data)
                    except json.JSONDecodeError:
                        print(message)
                    print_("The 'table' format is experimental.", type="warning")
        case "text":
            print(message)
        case "info":
            print_rich(message)
        case "warning":
            print_rich(f"[yellow][bold][Warning][/bold] {message}[/yellow]")
        case "error":
            print_rich(f"[red][bold][Error][/bold] {message}[/red]")
        case "success":
            print_rich(f"[green][bold][Success][/bold][/green] {message}")
        case "debug":
            if ctx is not None and ctx.obj["verbose"]:
                print_rich(f"[blue][bold][Debug][/bold] {message}[/blue]")
