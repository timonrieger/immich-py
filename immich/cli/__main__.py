try:  # pragma: no cover
    from .main import app
except ImportError:  # pragma: no cover
    app = None  # type: ignore[invalid-assignment]


def main() -> None:  # pragma: no cover
    if not app:
        import sys

        message = 'To use the immich command, install the "cli" extra:\n\n\t- pip install immich[cli]\n\tOR\n\t- uv add immich --extra cli\n'
        print(message, file=sys.stderr)
        sys.exit(1)
    app()
