try:  # pragma: no cover
    from .main import app
except ImportError:  # pragma: no cover
    import sys

    message = 'To use the immichpy command, install the "cli" extra:\n\n\t- pip install immichpy[cli]\n\tOR\n\t- uv add immichpy --extra cli\n'
    print(message, file=sys.stderr)
    sys.exit(1)


def main() -> None:  # pragma: no cover
    app()
