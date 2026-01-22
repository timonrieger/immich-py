from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from immich.client.generated.models.asset_bulk_upload_check_response_dto import (
    AssetBulkUploadCheckResponseDto,
)
from immich.client.generated.models.asset_bulk_upload_check_result import (
    AssetBulkUploadCheckResult,
)
from immich.client.generated.models.server_media_types_response_dto import (
    ServerMediaTypesResponseDto,
)
from immich.client.utils.upload import check_duplicates, find_sidecar, scan_files


@pytest.fixture
def mock_server_api():
    api = MagicMock()
    api.get_supported_media_types = AsyncMock(
        return_value=ServerMediaTypesResponseDto(
            image=[".jpg", ".jpeg", ".png"],
            video=[".mp4", ".mov"],
            sidecar=[".xmp"],
        )
    )
    return api


@pytest.fixture
def mock_assets():
    api = MagicMock()
    api.check_bulk_upload = AsyncMock()
    return api


@pytest.mark.asyncio
async def test_scan_files_list_of_files(mock_server_api, tmp_path: Path) -> None:
    file1 = tmp_path / "test1.jpg"
    file2 = tmp_path / "test2.png"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([file1, file2], mock_server_api)
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file2.resolve()}


@pytest.mark.asyncio
async def test_scan_files_directory_recursive(mock_server_api, tmp_path: Path) -> None:
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    file1 = tmp_path / "test1.jpg"
    file2 = subdir / "test2.png"
    file3 = subdir / "test3.mp4"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    file3.write_bytes(b"test3")
    result = await scan_files([tmp_path], mock_server_api)
    assert len(result) == 3
    assert set(result) == {file1.resolve(), file2.resolve(), file3.resolve()}


@pytest.mark.asyncio
async def test_scan_files_ignore_pattern_file(mock_server_api, tmp_path: Path) -> None:
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / "ignore.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, ignore_pattern="ignore.jpg")
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_ignore_pattern_single_file(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / "ignore.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([file2], mock_server_api, ignore_pattern="ignore.jpg")
    assert len(result) == 0


@pytest.mark.asyncio
async def test_scan_files_ignore_pattern_wildcard(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / "ignore.jpeg"
    file3 = tmp_path / "other.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    file3.write_bytes(b"test3")
    result = await scan_files([tmp_path], mock_server_api, ignore_pattern="*.jpeg")
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file3.resolve()}


@pytest.mark.asyncio
async def test_scan_files_ignore_pattern_directory(
    mock_server_api, tmp_path: Path
) -> None:
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    file1 = tmp_path / "test.jpg"
    file2 = subdir / "test2.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, ignore_pattern="*/subdir/*")
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_exclude_hidden_dir_path(
    mock_server_api, tmp_path: Path
) -> None:
    """Test that hidden files are excluded when scanning a directory."""
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / ".hidden.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, include_hidden=False)
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_include_hidden_dir_path(
    mock_server_api, tmp_path: Path
) -> None:
    """Test that hidden files are included when scanning a directory."""
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / ".hidden.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, include_hidden=True)
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file2.resolve()}


@pytest.mark.asyncio
async def test_scan_files_exclude_hidden_file_path(
    mock_server_api, tmp_path: Path
) -> None:
    """Test that hidden files are excluded when passed as a single file path."""
    file = tmp_path / ".hidden.jpg"
    file.write_bytes(b"test1")
    result = await scan_files([file], mock_server_api, include_hidden=False)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_scan_files_include_hidden_file_path(
    mock_server_api, tmp_path: Path
) -> None:
    """Test that hidden files are included when passed as a single file path."""
    file = tmp_path / ".hidden.jpg"
    file.write_bytes(b"test1")
    result = await scan_files([file], mock_server_api, include_hidden=True)
    assert len(result) == 1
    assert result[0] == file.resolve()


@pytest.mark.asyncio
async def test_scan_files_case_insensitive_extension_file(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.JPG"
    file2 = tmp_path / "test2.JpEg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([file1, file2], mock_server_api)
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file2.resolve()}


@pytest.mark.asyncio
async def test_scan_files_mixed_file_and_directory(
    mock_server_api, tmp_path: Path
) -> None:
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    file1 = tmp_path / "test1.jpg"
    file2 = subdir / "test2.png"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([file1, subdir], mock_server_api)
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file2.resolve()}


@pytest.mark.asyncio
async def test_scan_files_duplicate_files_in_list(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.jpg"
    file1.write_bytes(b"test1")
    result = await scan_files([file1, file1], mock_server_api)
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_only_unsupported_files(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.txt"
    file2 = tmp_path / "test.doc"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_check_duplicates_skip_duplicates(
    mock_assets: MagicMock, tmp_path: Path
) -> None:
    """Test that skip_duplicates returns early without API calls."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    new_files, rejected = await check_duplicates(
        [file1], mock_assets, skip_duplicates=True
    )
    assert new_files == [file1]
    assert rejected == []
    mock_assets.check_bulk_upload.assert_not_called()


@pytest.mark.asyncio
async def test_check_duplicates_dry_run(mock_assets: MagicMock, tmp_path: Path) -> None:
    """Test that dry_run returns early without API calls."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    new_files, rejected = await check_duplicates([file1], mock_assets, dry_run=True)
    assert new_files == [file1]
    assert rejected == []
    mock_assets.check_bulk_upload.assert_not_called()


@pytest.mark.asyncio
async def test_check_duplicates_unexpected_action(
    mock_assets, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that unexpected actions log a warning."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    # Use model_construct to bypass validation for unexpected action
    unexpected_result = AssetBulkUploadCheckResult.model_construct(
        action="unknown", id=str(file1), asset_id=None, reason=None
    )
    mock_assets.check_bulk_upload.return_value = AssetBulkUploadCheckResponseDto(
        results=[unexpected_result]
    )
    new_files, rejected = await check_duplicates([file1], mock_assets)
    assert new_files == []
    assert rejected == []
    assert "unexpected action" in caplog.text.lower()
    mock_assets.check_bulk_upload.assert_called_once()


@pytest.mark.asyncio
async def test_check_duplicates_mixed_results(mock_assets, tmp_path: Path) -> None:
    """Test that mixed accept and reject results are handled correctly."""
    file1 = tmp_path / "test1.jpg"
    file2 = tmp_path / "test2.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    mock_assets.check_bulk_upload.return_value = AssetBulkUploadCheckResponseDto(
        results=[
            AssetBulkUploadCheckResult(
                action="accept", id=str(file1), asset_id=None, reason=None
            ),
            AssetBulkUploadCheckResult(
                action="reject",
                id=str(file2),
                asset_id="asset-456",
                reason="duplicate",
            ),
        ]
    )
    new_files, rejected = await check_duplicates([file1, file2], mock_assets)
    assert new_files == [file1]
    assert len(rejected) == 1
    assert rejected[0].filepath == file2
    assert rejected[0].asset_id == "asset-456"
    assert rejected[0].reason == "duplicate"
    mock_assets.check_bulk_upload.assert_called_once()


@pytest.mark.asyncio
async def test_check_duplicates_with_progress(mock_assets, tmp_path: Path) -> None:
    """Test that show_progress doesn't break the function."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    mock_assets.check_bulk_upload.return_value = AssetBulkUploadCheckResponseDto(
        results=[
            AssetBulkUploadCheckResult(
                action="accept", id=str(file1), asset_id=None, reason=None
            )
        ]
    )
    new_files, rejected = await check_duplicates(
        [file1], mock_assets, show_progress=True
    )
    assert new_files == [file1]
    assert rejected == []
    mock_assets.check_bulk_upload.assert_called_once()


def test_find_sidecar_no_sidecar(tmp_path: Path) -> None:
    """Test that find_sidecar returns None when no sidecar exists."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    result = find_sidecar(file1)
    assert result is None


def test_find_sidecar_first_convention(tmp_path: Path) -> None:
    """Test that find_sidecar finds sidecar with first convention (filename.xmp)."""
    file1 = tmp_path / "test1.jpg"
    sidecar1 = tmp_path / "test1.xmp"
    file1.write_bytes(b"test1")
    sidecar1.write_bytes(b"xmp data")
    result = find_sidecar(file1)
    assert result == sidecar1


def test_find_sidecar_second_convention(tmp_path: Path) -> None:
    """Test that find_sidecar finds sidecar with second convention (filename.ext.xmp)."""
    file1 = tmp_path / "test1.jpg"
    sidecar1 = tmp_path / "test1.jpg.xmp"
    file1.write_bytes(b"test1")
    sidecar1.write_bytes(b"xmp data")
    result = find_sidecar(file1)
    assert result == sidecar1


def test_find_sidecar_both_exist(tmp_path: Path) -> None:
    """Test that find_sidecar returns first convention when both exist."""
    file1 = tmp_path / "test1.jpg"
    sidecar1 = tmp_path / "test1.xmp"
    sidecar2 = tmp_path / "test1.jpg.xmp"
    file1.write_bytes(b"test1")
    sidecar1.write_bytes(b"xmp data 1")
    sidecar2.write_bytes(b"xmp data 2")
    result = find_sidecar(file1)
    assert result == sidecar1
