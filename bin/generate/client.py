# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openapi-generator-cli[jdk4py]==7.18.0",
# ]
# ///

from __future__ import annotations

import os
import shutil
import subprocess  # nosec: B404
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
      from generated...  -> from immich.client.generated...
      import generated... -> import immich.client.generated...
    """
    replacements: list[tuple[str, str]] = [
        ("from generated.", "from immich.client.generated."),
        ("from generated ", "from immich.client.generated "),
        ("import generated.", "import immich.client.generated."),
        ("import generated", "import immich.client.generated"),
        ("klass = getattr(generated", "klass = getattr(immich.client.generated"),
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
    root = project_root()
    out_dir = root / "immich" / "client"
    client_dir = out_dir / "generated"

    url = openapi_url(os.environ.get("IMMICH_OPENAPI_REF", "main"))
    print(f"Fetching OpenAPI spec from: {url}")

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
        "generated",
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
