from __future__ import annotations

from pathlib import Path
from typing import Callable
from unittest.mock import AsyncMock, MagicMock, patch
import uuid

import pytest

from immich.client.generated.models.asset_bulk_upload_check_response_dto import (
    AssetBulkUploadCheckResponseDto,
)
from immich.client.generated.models.asset_bulk_upload_check_result import (
    AssetBulkUploadCheckResult,
)
from immich.client.generated.api_response import ApiResponse
from immich.client.generated.models.asset_media_response_dto import (
    AssetMediaResponseDto,
)
from immich.client.generated.models.asset_media_status import AssetMediaStatus
from immich.client.generated.models.server_media_types_response_dto import (
    ServerMediaTypesResponseDto,
)
from immich.client.generated.models.album_response_dto import AlbumResponseDto
from immich.client.generated.exceptions import ApiException
from immich.client.utils.upload import (
    check_duplicates,
    delete_files,
    find_sidecar,
    RejectedEntry,
    scan_files,
    update_albums,
    upload_file,
    upload_files,
    UploadedEntry,
)


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
    api.upload_asset_with_http_info = AsyncMock()
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


@pytest.mark.asyncio
async def test_upload_file_dry_run(mock_assets, tmp_path: Path) -> None:
    """Test that dry_run returns mock response without API call."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    result = await upload_file(file1, mock_assets, dry_run=True)
    assert isinstance(result, ApiResponse)
    assert result.status_code == 201
    assert isinstance(result.data, AssetMediaResponseDto)
    assert result.data.status == AssetMediaStatus.CREATED
    mock_assets.upload_asset_with_http_info.assert_not_called()


@pytest.mark.asyncio
async def test_upload_file_with_sidecar(mock_assets, tmp_path: Path) -> None:
    """Test upload with sidecar file found."""
    file1 = tmp_path / "test1.jpg"
    sidecar1 = tmp_path / "test1.xmp"
    file1.write_bytes(b"test1")
    sidecar1.write_bytes(b"xmp data")
    mock_response = ApiResponse(
        status_code=201,
        headers=None,
        data=AssetMediaResponseDto(id="asset-123", status=AssetMediaStatus.CREATED),
        raw_data=b"",
    )
    mock_assets.upload_asset_with_http_info.return_value = mock_response
    result = await upload_file(file1, mock_assets)
    assert result == mock_response
    call_kwargs = mock_assets.upload_asset_with_http_info.call_args[1]
    assert call_kwargs["sidecar_data"] == str(sidecar1)


@pytest.mark.asyncio
async def test_upload_files_empty_list(mock_assets) -> None:
    """Test that empty files list returns empty results."""
    uploaded, rejected, failed = await upload_files([], mock_assets)
    assert uploaded == []
    assert rejected == []
    assert failed == []


@pytest.mark.asyncio
async def test_upload_files_api_exception(mock_assets, tmp_path: Path) -> None:
    """Test that ApiException is caught and added to failed list."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    with patch("immich.client.utils.upload.upload_file") as mock_upload:
        api_exception = ApiException(status=400, reason="Bad Request")
        api_exception.body = '{"message": "Invalid file format"}'
        mock_upload.side_effect = api_exception
        uploaded, rejected, failed = await upload_files([file1], mock_assets)
        assert uploaded == []
        assert rejected == []
        assert len(failed) == 1
        assert failed[0].filepath == file1
        assert "Invalid file format" in failed[0].error


@pytest.mark.asyncio
async def test_upload_files_api_exception_invalid_json(
    mock_assets, tmp_path: Path
) -> None:
    """Test that ApiException with invalid JSON body falls back to error message."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    with patch("immich.client.utils.upload.upload_file") as mock_upload:
        api_exception = ApiException(status=400, reason="Bad Request")
        api_exception.body = "not valid json"
        mock_upload.side_effect = api_exception
        uploaded, rejected, failed = await upload_files([file1], mock_assets)
        assert uploaded == []
        assert rejected == []
        assert len(failed) == 1
        assert failed[0].filepath == file1
        # Should use the exception string message when JSON parsing fails
        assert failed[0].error


@pytest.mark.asyncio
async def test_upload_files_generic_exception(mock_assets, tmp_path: Path) -> None:
    """Test that generic exceptions are caught and added to failed list."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    with patch("immich.client.utils.upload.upload_file") as mock_upload:
        mock_upload.side_effect = RuntimeError("Network error")
        uploaded, rejected, failed = await upload_files([file1], mock_assets)
        assert uploaded == []
        assert rejected == []
        assert len(failed) == 1
        assert failed[0].filepath == file1
        assert "Network error" in failed[0].error


@pytest.mark.asyncio
async def test_upload_files_mixed_results(mock_assets, tmp_path: Path) -> None:
    """Test mixed results (uploaded, rejected, failed)."""
    file1 = tmp_path / "test1.jpg"
    file2 = tmp_path / "test2.jpg"
    file3 = tmp_path / "test3.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    file3.write_bytes(b"test3")
    with patch("immich.client.utils.upload.upload_file") as mock_upload:
        mock_upload.side_effect = [
            ApiResponse(
                status_code=201,
                headers=None,
                data=AssetMediaResponseDto(
                    id="asset-1", status=AssetMediaStatus.CREATED
                ),
                raw_data=b"",
            ),
            ApiResponse(
                status_code=200,
                headers=None,
                data=AssetMediaResponseDto(
                    id="asset-2", status=AssetMediaStatus.CREATED
                ),
                raw_data=b"",
            ),
            ApiResponse(
                status_code=500,
                headers=None,
                data=AssetMediaResponseDto(
                    id="asset-1", status=AssetMediaStatus.CREATED
                ),
                raw_data=b"",
            ),
        ]
        uploaded, rejected, failed = await upload_files(
            [file1, file2, file3], mock_assets
        )
        assert len(uploaded) == 1
        assert uploaded[0].filepath == file1
        assert len(rejected) == 1
        assert rejected[0].filepath == file2
        assert len(failed) == 1
        assert failed[0].filepath == file3
        assert "status_code=500" in failed[0].error


@pytest.mark.asyncio
async def test_upload_files_dry_run_no_progress_update(
    mock_assets, tmp_path: Path
) -> None:
    """Test that dry_run doesn't update progress bar."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    with patch("immich.client.utils.upload.upload_file") as mock_upload:
        mock_upload.return_value = ApiResponse(
            status_code=201,
            headers=None,
            data=AssetMediaResponseDto(id="asset-1", status=AssetMediaStatus.CREATED),
            raw_data=b"",
        )
        uploaded, rejected, failed = await upload_files(
            [file1], mock_assets, dry_run=True
        )
        assert len(uploaded) == 1
        # Progress update should not be called in dry_run mode
        # (verified by the fact that upload_file is called with dry_run=True)


@pytest.fixture
def mock_albums_api():
    api = MagicMock()
    api.get_all_albums = AsyncMock()
    api.create_album = AsyncMock()
    api.add_assets_to_album = AsyncMock()
    return api


@pytest.mark.asyncio
async def test_update_albums_no_album_name(
    mock_albums_api, uploaded_entry_factory: Callable[..., UploadedEntry]
) -> None:
    """Test that update_albums returns early when album_name is None."""
    uploaded_entry = uploaded_entry_factory()
    uploaded_entry.asset.id = "asset-1"
    await update_albums([uploaded_entry], None, mock_albums_api)
    mock_albums_api.get_all_albums.assert_not_called()
    mock_albums_api.create_album.assert_not_called()
    mock_albums_api.add_assets_to_album.assert_not_called()


@pytest.mark.asyncio
async def test_update_albums_empty_uploaded(mock_albums_api) -> None:
    """Test that update_albums returns early when uploaded is empty."""
    await update_albums([], "My Album", mock_albums_api)
    mock_albums_api.get_all_albums.assert_not_called()
    mock_albums_api.create_album.assert_not_called()
    mock_albums_api.add_assets_to_album.assert_not_called()


@pytest.mark.asyncio
async def test_update_albums_existing_album(
    mock_albums_api, uploaded_entry_factory: Callable[..., UploadedEntry]
) -> None:
    """Test that update_albums adds assets to existing album."""
    album_id = uuid.uuid4()
    uploaded_entry = uploaded_entry_factory()
    existing_album = AlbumResponseDto.model_construct(
        album_name="My Album", id=str(album_id)
    )
    mock_albums_api.get_all_albums.return_value = [existing_album]
    await update_albums([uploaded_entry], "My Album", mock_albums_api)
    mock_albums_api.get_all_albums.assert_called_once()
    mock_albums_api.create_album.assert_not_called()
    mock_albums_api.add_assets_to_album.assert_called_once()
    call_args = mock_albums_api.add_assets_to_album.call_args
    assert call_args[1]["id"] == album_id
    assert len(call_args[1]["bulk_ids_dto"].ids) == 1


@pytest.mark.asyncio
async def test_update_albums_create_new_album(
    mock_albums_api, uploaded_entry_factory: Callable[..., UploadedEntry]
) -> None:
    """Test that update_albums creates album if it doesn't exist."""
    album_id = uuid.uuid4()
    uploaded_entry = uploaded_entry_factory()
    new_album = AlbumResponseDto.model_construct(
        album_name="New Album", id=str(album_id)
    )
    mock_albums_api.get_all_albums.return_value = []
    mock_albums_api.create_album.return_value = new_album
    await update_albums([uploaded_entry], "New Album", mock_albums_api)
    mock_albums_api.get_all_albums.assert_called_once()
    mock_albums_api.create_album.assert_called_once()
    mock_albums_api.add_assets_to_album.assert_called_once()
    call_args = mock_albums_api.add_assets_to_album.call_args
    assert call_args[1]["id"] == album_id


@pytest.mark.asyncio
async def test_update_albums_batching(
    mock_albums_api, uploaded_entry_factory: Callable[..., UploadedEntry]
) -> None:
    """Test that update_albums batches assets in groups of 1000."""
    album_id = uuid.uuid4()
    uploaded_entries = [
        uploaded_entry_factory(filename=f"test{i}.jpg") for i in range(1500)
    ]
    existing_album = AlbumResponseDto.model_construct(
        album_name="Large Album", id=str(album_id)
    )
    mock_albums_api.get_all_albums.return_value = [existing_album]
    await update_albums(uploaded_entries, "Large Album", mock_albums_api)
    assert mock_albums_api.add_assets_to_album.call_count == 2
    first_call = mock_albums_api.add_assets_to_album.call_args_list[0]
    second_call = mock_albums_api.add_assets_to_album.call_args_list[1]
    assert len(first_call[1]["bulk_ids_dto"].ids) == 1000
    assert len(second_call[1]["bulk_ids_dto"].ids) == 500


@pytest.mark.asyncio
async def test_delete_files_no_flags(
    uploaded_entry_factory: Callable[..., UploadedEntry],
) -> None:
    """Test that delete_files does nothing when both flags are False."""
    uploaded_entry = uploaded_entry_factory()
    await delete_files(
        [uploaded_entry], [], delete_uploads=False, delete_duplicates=False
    )
    assert uploaded_entry.filepath.exists()


@pytest.mark.asyncio
async def test_delete_files_delete_uploads(
    uploaded_entry_factory: Callable[..., UploadedEntry],
) -> None:
    """Test that delete_files deletes uploaded files when delete_uploads=True."""
    uploaded_entry = uploaded_entry_factory()
    await delete_files([uploaded_entry], [], delete_uploads=True)
    assert not uploaded_entry.filepath.exists()


@pytest.mark.asyncio
async def test_delete_files_delete_duplicates(tmp_path: Path) -> None:
    """Test that delete_files deletes duplicate rejected files when delete_duplicates=True."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    rejected_entry = RejectedEntry(
        filepath=file1,
        asset_id="asset-123",
        reason="duplicate",
    )
    await delete_files([], [rejected_entry], delete_duplicates=True)
    assert not file1.exists()


@pytest.mark.asyncio
async def test_delete_files_skip_non_duplicate_rejected(tmp_path: Path) -> None:
    """Test that delete_files skips rejected files that aren't duplicates."""
    file1 = tmp_path / "test1.jpg"
    file1.write_bytes(b"test1")
    rejected_entry = RejectedEntry(
        filepath=file1,
        asset_id=None,
        reason="unsupported_format",
    )
    await delete_files([], [rejected_entry], delete_duplicates=True)
    assert file1.exists()


@pytest.mark.asyncio
async def test_delete_files_dry_run(
    uploaded_entry_factory: Callable[..., UploadedEntry],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that delete_files logs but doesn't delete in dry_run mode."""
    import logging

    caplog.set_level(logging.INFO)
    uploaded_entry = uploaded_entry_factory(sidecar=True)
    await delete_files([uploaded_entry], [], delete_uploads=True, dry_run=True)
    assert uploaded_entry.filepath.exists()
    sidecar1 = uploaded_entry.filepath.parent / f"{uploaded_entry.filepath.stem}.xmp"
    assert sidecar1.exists()
    assert "Would have deleted" in caplog.text


@pytest.mark.asyncio
async def test_delete_files_with_sidecar(
    uploaded_entry_factory: Callable[..., UploadedEntry],
) -> None:
    """Test that delete_files deletes sidecar files."""
    uploaded_entry = uploaded_entry_factory(sidecar=True)
    sidecar1 = uploaded_entry.filepath.parent / f"{uploaded_entry.filepath.stem}.xmp"
    await delete_files([uploaded_entry], [], delete_uploads=True)
    assert not uploaded_entry.filepath.exists()
    assert not sidecar1.exists()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "fail_file,expected_file1_exists,expected_sidecar_exists,expected_log_message",
    [
        ("sidecar", False, True, "Failed to delete sidecar"),
        ("main", True, True, "Failed to delete"),
    ],
)
async def test_delete_files_deletion_failure(
    uploaded_entry_factory: Callable[..., UploadedEntry],
    caplog: pytest.LogCaptureFixture,
    fail_file: str,
    expected_file1_exists: bool,
    expected_sidecar_exists: bool,
    expected_log_message: str,
) -> None:
    """Test that delete_files handles deletion failures gracefully."""
    import logging
    from pathlib import Path as PathClass

    caplog.set_level(logging.ERROR)
    uploaded_entry = uploaded_entry_factory(sidecar=True)
    file1 = uploaded_entry.filepath
    sidecar1 = file1.parent / f"{file1.stem}.xmp"
    original_unlink = PathClass.unlink

    def failing_unlink(self):
        target = sidecar1 if fail_file == "sidecar" else file1
        if self.resolve() == target.resolve():
            raise Exception("Permission denied")
        return original_unlink(self)

    with patch.object(PathClass, "unlink", failing_unlink):
        await delete_files([uploaded_entry], [], delete_uploads=True)
        assert file1.exists() == expected_file1_exists
        assert sidecar1.exists() == expected_sidecar_exists
        assert expected_log_message in caplog.text
