from __future__ import annotations

from email.message import Message
from mimetypes import guess_extension
from pathlib import Path
from typing import Awaitable, Callable, Optional

import logging
import tqdm

from immich.client.rest import RESTResponseType

logger = logging.getLogger(__name__)


def h(name: str, headers: dict[str, str]) -> Optional[str]:
    """
    Get a header value from a dictionary of headers case-insensitive.
    """
    return next((v for k, v in headers.items() if k.lower() == name.lower()), None)


def filename_from_headers(
    headers: dict[str, str] | None, *, fallback_base: str
) -> Optional[str]:
    """
    Derive a filename from response headers.

    Order of precedence:
    - Content-Disposition filename (if present)
      - if it has no extension, append an extension derived from Content-Type (if available)
    - Content-Type derived extension + `fallback_base`

    :param headers: The response headers.
    :param fallback_base: The filename without extension if we cannot derive the original filename from the Content-Disposition header.

    :returns: The derived filename or None if we cannot derive the filename from the headers.
    """
    if not headers:
        return None

    cd_name: Optional[str] = None
    if cd := h("content-disposition", headers):
        msg = Message()
        msg["content-disposition"] = cd
        if filename := msg.get_filename():
            cd_name = Path(filename).name

    ext = (
        guess_extension(ct.partition(";")[0].strip())
        if (ct := h("content-type", headers))
        else None
    )

    # Content-Disposition wins for the base name; Content-Type is the safety net for the extension.
    if cd_name:
        return cd_name if Path(cd_name).suffix or not ext else f"{cd_name}{ext}"

    return f"{fallback_base}{ext}" if ext else None


def resolve_output_filename(
    headers: dict[str, str] | None,
    *,
    name: Optional[str] = None,
    default_base: str,
    default_ext: Optional[str] = None,
) -> str:
    """
    Resolve an output filename by selecting a base name and an extension.

    Base name precedence:
    - user-supplied `name`
    - Content-Disposition filename
    - `default_base`

    Extension precedence:
    - `default_ext` (if provided; overrides any other extension)
    - extension present on the chosen base name (e.g. from Content-Disposition)
    - Content-Type derived extension
    - none

    :param headers: The response headers.
    :param name: The user-supplied name.
    :param default_base: The default base name, used when no user/header filename can be derived.
    :param default_ext: The default extension (must start with `.`), used when you want to force a specific extension (e.g. `.zip`).

    :returns: The resolved filename.
    """
    if default_ext and not default_ext.startswith("."):
        raise ValueError("default_ext must start with '.' (e.g. '.zip')")

    base = default_base
    ext = None

    header_path = None
    if _ := filename_from_headers(headers, fallback_base=default_base):
        header_path = Path(_)

    # Base name
    if name:
        base = Path(name).stem
    elif header_path:
        base = header_path.stem

    # Extension
    if default_ext:
        ext = default_ext
    elif header_path:
        ext = header_path.suffix
    return f"{base}{ext}" if ext else base


async def download_file(
    make_request: Callable[[Optional[dict[str, str]]], Awaitable[RESTResponseType]],
    out_dir: Path,
    resolve_filename: Callable[[dict[str, str]], str],
    *,
    show_progress: bool = True,
    pbar: Optional[tqdm.tqdm] = None,
    resumeable: bool = True,
) -> Path:
    """
    Download a file and show a progress bar. Allow resuming a download.

    :param make_request: A function that makes a request and returns a RESTResponseType. It takes an optional dictionary of headers.
    :param out_dir: Output directory where the downloaded file will be written.
    :param resolve_filename: Callable that derives the filename. It takes the response headers and returns a string.
    :param show_progress: Whether to show a progress bar.
    :param pbar: A tqdm progress bar to use. If not provided, a new one will be created. If provided, show_progress is ignored. Must be closed by the caller.
    :param resumeable: Whether the download can be resumed from an existing partial `.temp` file via HTTP Range requests.
    :return: The path to the downloaded file.
    """
    resp = None
    temp_path = None
    pbar_created = False

    try:
        file_size = 0
        resp = await make_request(None)

        if not out_dir.is_dir():
            raise ValueError(f"out_dir must be a directory, got: {out_dir}")
        out_dir.mkdir(parents=True, exist_ok=True)

        name = resolve_filename(resp.headers)
        out_path = out_dir / name

        total_size = int(h("Content-Length", resp.headers) or 0)
        temp_path = out_path.with_suffix(out_path.suffix + ".temp")

        if out_path.exists():
            logger.info(f"File already exists: {out_path}")
            file_size = out_path.stat().st_size
            if file_size == total_size:
                resp.close()
                return out_path
            else:
                logger.warning(
                    f"File size mismatch for {out_path}: local file is {file_size} bytes, "
                    f"server reports {total_size} bytes. Skipping download for security reasons. "
                    f"Possible reasons: file was modified locally, file corruption, or server file was updated. "
                    f"If you want to re-download, delete the file and rerun the request."
                )
                resp.close()
                return out_path

        resumed = False
        if temp_path.exists():
            file_size = temp_path.stat().st_size

            if file_size < total_size:
                if resumeable:
                    resume_header = {"Range": f"bytes={file_size}-"}
                    resp.close()
                    resp = await make_request(resume_header)
                    if file_size > 0 and resp.status != 206:
                        logger.debug(
                            "Server does not support resuming; restarting download"
                        )
                        resp.close()
                        temp_path.unlink()
                        file_size = 0
                        resp = await make_request(None)
                    else:
                        logger.info("Resuming download")
                        resumed = True
            else:
                logger.debug(f"Deleting file {out_path} and restarting")
                temp_path.unlink()
                file_size = 0
        else:
            logger.info("Starting download")

        if not pbar:
            pbar = tqdm.tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                desc=str(out_path),
                disable=not show_progress,
            )
            pbar_created = True

        if resumed and file_size > 0:
            pbar.update(file_size)
        async with resp:
            mode = "ab" if (resumed and file_size > 0) else "wb"
            with temp_path.open(mode) as f:
                async for chunk in resp.content.iter_chunked(1024 * 1024):
                    if not chunk:
                        continue
                    f.write(chunk)
                    pbar.update(len(chunk))

        temp_path.replace(out_path)
        return out_path

    except Exception:
        if temp_path and temp_path.exists():
            temp_path.unlink()
        raise
    finally:
        if resp and not resp.closed:
            resp.close()

        # Only close pbar if we created it
        if pbar_created and pbar:
            pbar.close()
