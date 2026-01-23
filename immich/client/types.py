from pathlib import Path
from typing import Literal, Optional, Union
from multidict import CIMultiDictProxy
from pydantic import BaseModel, Field

from immich.client.generated import AssetMediaResponseDto

HeadersType = Union[dict[str, str], CIMultiDictProxy[str]]
RejectionReason = Literal["duplicate", "unsupported_format"]


class UploadStats(BaseModel):
    total: int
    uploaded: int
    rejected: int
    failed: int


class RejectedEntry(BaseModel):
    """Represents a file that was rejected during upload (check)."""

    filepath: Path = Field(
        ..., description="The path to the local file that was rejected."
    )
    asset_id: Optional[str] = Field(
        None, description="The ID of the asset. Set if reason is 'duplicate'."
    )
    reason: Optional[RejectionReason] = Field(
        None, description="The reason for the rejection."
    )


class FailedEntry(BaseModel):
    """Represents a file that failed to upload."""

    filepath: Path = Field(
        ..., description="The path to the local file that failed to upload."
    )
    error: str = Field(..., description="The error message from the server.")


class UploadedEntry(BaseModel):
    """Represents a successfully uploaded file."""

    asset: AssetMediaResponseDto = Field(
        ..., description="The asset that was uploaded."
    )
    filepath: Path = Field(
        ..., description="The path to the local file that was uploaded."
    )


class UploadResult(BaseModel):
    """The result of an upload operation containing all uploaded, rejected, and failed entries."""

    uploaded: list[UploadedEntry] = Field(
        ..., description="The assets that were uploaded."
    )
    rejected: list[RejectedEntry] = Field(
        ..., description="The files that were rejected."
    )
    failed: list[FailedEntry] = Field(
        ..., description="The files that failed to upload."
    )
    stats: UploadStats = Field(..., description="The statistics of the upload.")
