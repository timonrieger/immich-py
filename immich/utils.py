from __future__ import annotations

from email.message import Message
from mimetypes import guess_extension
from typing import Optional


def filename_from_headers(
    headers: dict[str, str] | None, *, fallback_base: str
) -> Optional[str]:
    """
    Derive a filename from response headers. First, we try to derive the original filename from the Content-Disposition header. If that fails, we try to derive the filename from the Content-Type header.

    :param headers: The response headers.
    :param fallback_base: The fallback base for the filename if we cannot derive the original filename from the headers.
    """
    if not headers:
        return None

    def h(name: str) -> Optional[str]:
        return next((v for k, v in headers.items() if k.lower() == name.lower()), None)

    cd = h("content-disposition")
    if cd:
        msg = Message()
        msg["content-disposition"] = cd
        filename = msg.get_filename()
        if filename:
            return filename

    ct = h("content-type")
    if not ct:
        return None

    ext = guess_extension(ct.partition(";")[0].strip())
    if not ext:
        return None
    return f"{fallback_base}{ext}"
