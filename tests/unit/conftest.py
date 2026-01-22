from __future__ import annotations

from pathlib import Path
from typing import Callable, Generator, Optional
import uuid

import pytest

from immich.client.generated.models.asset_media_response_dto import (
    AssetMediaResponseDto,
)
from immich.client.generated.models.asset_media_status import AssetMediaStatus
from immich.client.utils.upload import UploadedEntry


@pytest.fixture
def uploaded_entry_factory(
    tmp_path: Path,
) -> Generator[Callable[[Optional[str], bool], UploadedEntry], None, None]:
    """Factory fixture: yields a callable to create uploaded entries with optional sidecar.

    Example:
        entry = uploaded_entry_factory()
        entry2 = uploaded_entry_factory(filename="custom.jpg", sidecar=True)
    """

    def _create_uploaded_entry(
        filename: Optional[str] = None, sidecar: bool = False
    ) -> UploadedEntry:
        if filename is None:
            filename = f"test{uuid.uuid4()}.jpg"
        file_path = tmp_path / filename
        file_path.write_bytes(b"test image data")

        if sidecar:
            sidecar_path = tmp_path / f"{file_path.stem}.xmp"
            sidecar_path.write_bytes(b"xmp sidecar data")

        return UploadedEntry(
            asset=AssetMediaResponseDto(
                id=str(uuid.uuid4()), status=AssetMediaStatus.CREATED
            ),
            filepath=file_path,
        )

    yield _create_uploaded_entry
