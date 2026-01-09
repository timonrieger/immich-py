from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from immich.client.models.server_media_types_response_dto import (
    ServerMediaTypesResponseDto,
)
from immich._internal.upload import scan_files


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


@pytest.mark.asyncio
async def test_scan_files_single_file(mock_server_api, tmp_path: Path) -> None:
    test_file = tmp_path / "test.jpg"
    test_file.write_bytes(b"test")
    result = await scan_files([test_file], mock_server_api)
    assert len(result) == 1
    assert result[0] == test_file.resolve()


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
async def test_scan_files_unsupported_extension(
    mock_server_api, tmp_path: Path
) -> None:
    test_file = tmp_path / "test.txt"
    test_file.write_bytes(b"test")
    result = await scan_files([test_file], mock_server_api)
    assert len(result) == 0


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
async def test_scan_files_exclude_hidden_files(mock_server_api, tmp_path: Path) -> None:
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / ".hidden.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, include_hidden=False)
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_include_hidden_files(mock_server_api, tmp_path: Path) -> None:
    file1 = tmp_path / "test.jpg"
    file2 = tmp_path / ".hidden.jpg"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api, include_hidden=True)
    assert len(result) == 2
    assert set(result) == {file1.resolve(), file2.resolve()}


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
async def test_scan_files_empty_directory(mock_server_api, tmp_path: Path) -> None:
    result = await scan_files([tmp_path], mock_server_api)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_scan_files_video_extensions(mock_server_api, tmp_path: Path) -> None:
    file1 = tmp_path / "test.mp4"
    file2 = tmp_path / "test.mov"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api)
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
async def test_scan_files_file_with_ignore_pattern_no_match(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.jpg"
    file1.write_bytes(b"test1")
    result = await scan_files([file1], mock_server_api, ignore_pattern="other.jpg")
    assert len(result) == 1
    assert result[0] == file1.resolve()


@pytest.mark.asyncio
async def test_scan_files_directory_with_only_unsupported_files(
    mock_server_api, tmp_path: Path
) -> None:
    file1 = tmp_path / "test.txt"
    file2 = tmp_path / "test.doc"
    file1.write_bytes(b"test1")
    file2.write_bytes(b"test2")
    result = await scan_files([tmp_path], mock_server_api)
    assert len(result) == 0
