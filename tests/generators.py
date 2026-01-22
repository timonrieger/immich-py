"""Image and video generators for E2E tests."""

from __future__ import annotations

import base64
import io
import time
from typing import Iterator

from PIL import Image


def _create_jpeg_with_seed(seed: int) -> bytes:
    """Create a minimal JPEG with seed-based pixel values to ensure uniqueness."""
    # Create a 2x2 image to embed more unique data in the content hash
    # This ensures better uniqueness even when seeds are close together
    img = Image.new("RGB", (2, 2))
    pixels = img.load()
    # load() always returns PixelAccess for newly created images
    assert pixels is not None

    # Use seed to set different pixel values across the 2x2 grid
    # Extract multiple values from seed to ensure variation
    pixels[0, 0] = ((seed >> 24) & 0xFF, (seed >> 16) & 0xFF, (seed >> 8) & 0xFF)
    pixels[1, 0] = ((seed >> 8) & 0xFF, seed & 0xFF, ((seed >> 24) & 0xFF))
    pixels[0, 1] = (seed & 0xFF, ((seed >> 16) & 0xFF), ((seed >> 24) & 0xFF))
    pixels[1, 1] = (((seed >> 16) & 0xFF), ((seed >> 8) & 0xFF), seed & 0xFF)

    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=95)
    return buffer.getvalue()


def _new_jpeg_factory() -> Iterator[bytes]:
    """Generator that yields unique JPEG images by incrementing seed."""
    # Initialize seed with timestamp (nanoseconds) to ensure uniqueness across test runs
    seed = int(time.time_ns()) % (2**32)
    while True:
        yield _create_jpeg_with_seed(seed)
        seed = (seed + 1) % (2**32)


_jpeg_factory = _new_jpeg_factory()


def make_random_image() -> bytes:
    """Generate a random unique JPEG image for testing."""
    return next(_jpeg_factory)


# Decode the MP4 template once at module import
_MP4_BASE64 = "AAAAIGZ0eXBtcDQyAAAAAG1wNDJtcDQxaXNvbWF2YzEAAAGhtZGF0AAACrgYF//+q3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE0OCByMjA1OCBlYjc2Y2U1IC0gSC4yNjQvTVBFRy00IEFWQyBjb2RlYyAtIENvcHlsZWZ0IDIwMDMtMjAxNyAtIGh0dHA6Ly93d3cudmlkZW9sYW4ub3JnL3gyNjQuaHRtbCAtIG9wdGlvbnM6IGNhYmFjPTEgcmVmPTMgZGVibG9jaz0xOjA6MCBhbmFseXNlPTB4MzoweDExMyBtZT1oZXggc3VibWU9NyBwc3k9MSBwc3lfcmQ9MS4wMDowLjAwIG1peGVkX3JlZj0xIG1lX3JhbmdlPTE2IGNocm9tYV9tZT0xIHRyZWxsaXM9MSA4eDhkY3Q9MSBjcW09MCBkZWFkem9uZT0yMSwxMSBmYXN0X3Bza2lwPTEgY2hyb21hX3FwX29mZnNldD0tMiB0aHJlYWRzPTEgbG9va2FoZWFkX3RocmVhZHM9MSBzbGljZWRfdGhyZWFkcz0wIG5yPTAgZGVjaW1hdGU9MSBpbnRlcmxhY2VkPTAgYmx1cmF5X2NvbXBhdD0wIGNvbnN0cmFpbmVkX2ludHJhPTAgYmZyYW1lcz0zIGJfcHlyYW1pZD0yIGJfYWRhcHQ9MSBiX2JpYXM9MCBkaXJlY3Q9MSB3ZWlnaHRiPTEgb3Blbl9nb3A9MCB3ZWlnaHRwPTIga2V5aW50PTI1MCBrZXlpbnRfbWluPTI1IHNjZW5lY3V0PTQwIGludHJhX3JlZnJlc2g9MCByY19sb29rYWhlYWQ9NDAgcmM9Y3JmIG1idHJlZT0xIGNyZj0yMy4wIHFjb21wPTAuNjAgcXBtaW49MCBxcG1heD02OSBxcHN0ZXA9NCBpcF9yYXRpbz0xLjQwIGFxPTE6MS4wMAA="
MODULE_TEMPLATE = base64.b64decode(_MP4_BASE64)


def _create_minimal_mp4(seed: int) -> bytes:
    """Create a minimal valid MP4 with variable seed data."""
    # Copy the template before mutating
    mp4_bytes = bytearray(MODULE_TEMPLATE)

    # Locate the mdat box (media data box) for safe payload region
    mdat_pos = mp4_bytes.find(b"mdat")
    if mdat_pos == -1:
        # If mdat not found, append a harmless free box at the end
        # free box: 8 bytes (size + type) + payload
        free_box = b"\x00\x00\x00\x10free"  # 16 bytes total (8 header + 8 payload)
        mp4_bytes.extend(free_box)
        payload_start = len(mp4_bytes) - 8  # Start of the free box payload
    else:
        # mdat box structure: [4 bytes size][4 bytes 'mdat'][payload...]
        # Payload starts after the 8-byte header
        payload_start = mdat_pos + 8

    # Apply seed-based mutations in the payload region
    seed_bytes = seed.to_bytes(8, byteorder="big")
    for i, byte_val in enumerate(seed_bytes):
        if payload_start + i < len(mp4_bytes):
            mp4_bytes[payload_start + i] = byte_val

    return bytes(mp4_bytes)


def _new_mp4_factory() -> Iterator[bytes]:
    """Generator that yields unique MP4 videos by incrementing seed."""
    seed = 0
    while True:
        yield _create_minimal_mp4(seed)
        seed = (seed + 1) % (2**32)


_mp4_factory = _new_mp4_factory()


def make_random_video() -> bytes:
    """Generate a random unique MP4 video for testing."""
    return next(_mp4_factory)
