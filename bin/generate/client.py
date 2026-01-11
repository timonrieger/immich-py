# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openapi-generator-cli[jdk4py]==7.18.0",
# ]
# ///

from __future__ import annotations

import argparse
import os
import shutil
import subprocess  # nosec: B404
import urllib.error
import urllib.request
from pathlib import Path


def project_root() -> Path:
    # This file lives at bin/generate/client.py
    return Path(__file__).resolve().parents[2]


def openapi_url(ref: str) -> str:
    return (
        "https://raw.githubusercontent.com/immich-app/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )


def rewrite_imports_in_tree(root: Path) -> int:
    """
    Rewrite OpenAPI generator absolute imports:
      from client...  -> from immich.client...
      import client... -> import immich.client...
    """
    replacements: list[tuple[str, str]] = [
        ("from client.", "from immich.client."),
        ("from client ", "from immich.client "),
        ("import client.", "import immich.client."),
        ("import client", "import immich.client"),
        ("klass = getattr(client", "klass = getattr(immich.client"),
    ]

    changed = 0
    for path in root.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Immich OpenAPI client and rewrite imports."
    )
    parser.add_argument(
        "--ref",
        default=os.environ.get("IMMICH_OPENAPI_REF", "main"),
        help="Immich git ref for OpenAPI spec (default: IMMICH_OPENAPI_REF or 'main')",
    )
    args = parser.parse_args()

    root = project_root()
    out_dir = root / "immich"
    client_dir = out_dir / "client"

    url = openapi_url(args.ref)
    print(f"Generating Immich client from ref: {args.ref}")
    print(f"Spec URL: {url}")

    if client_dir.exists():
        print("Deleting existing generated client folder:", client_dir)
        shutil.rmtree(client_dir)

    generator_cmd = [
        "openapi-generator-cli",
        "generate",
        "-i",
        url,
        "-g",
        "python",
        "--package-name",
        "client",
        "--global-property",
        "supportingFiles,models,apis",
        "--additional-properties",
        "pipPackageName=immich",
        "-o",
        str(out_dir),
        "--openapi-generator-ignore-list",
        "setup.py,setup.cfg,pyproject.toml,tox.ini,py.typed,.gitignore,.gitlab-ci.yml,.github/,git_push.sh,test/,docs/,.travis.yml,test-requirements.txt,requirements.txt,README.md,.openapi-generator-ignore",
        "--minimal-update",
        "--library",
        "asyncio",
    ]
    subprocess.run(generator_cmd, cwd=str(root), check=True)  # nosec: B603

    if not client_dir.exists():
        print(f"Expected generated directory not found: {client_dir}")
        return 1

    changed = rewrite_imports_in_tree(client_dir)
    print(f"Rewrote imports in {changed} files under {client_dir}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
