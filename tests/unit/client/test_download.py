from __future__ import annotations

from pathlib import Path

import pytest

from immich.client.types import HeadersType
import immich.client.utils.download as download_utils


@pytest.mark.parametrize(
    ("name", "default_ext", "headers", "expected"),
    [
        # user name wins; path + extension are stripped; extension comes from Content-Type
        ("dir/evil.png", None, {"Content-Type": "image/jpeg"}, "evil.jpg"),
        ("image.txt", None, {"Content-Type": "image/jpeg"}, "image.jpg"),
        # user name with no ext gets content-type ext (when default_ext is not forcing)
        ("photo", None, {"Content-Type": "image/jpeg"}, "photo.jpg"),
        # user name with no ext and no content-type => keep as-is
        ("photo", None, None, "photo"),
        # user name with ext and no content-type => strip ext
        ("photo.txt", None, None, "photo"),
        # forcing default_ext strips any ext
        ("foo.tar.gz", ".zip", None, "foo.tar.zip"),
        ("foo.tar.gz", ".zip", {"Content-Type": "image/jpeg"}, "foo.tar.zip"),
        # header-derived name is used when no user name
        (
            None,
            None,
            {"Content-Disposition": 'attachment; filename="abc.jpeg"'},
            "abc.jpeg",
        ),
        # forcing default_ext also applies to header-derived name
        (
            None,
            ".zip",
            {"Content-Disposition": 'attachment; filename="abc.jpeg"'},
            "abc.zip",
        ),
        # header-derived name without ext (and no Content-Type ext) yields base only
        (None, None, {"Content-Disposition": 'attachment; filename="abc"'}, "abc"),
        # default is used when neither user name nor header name is available
        (None, None, None, "orig-123"),
        (None, ".zip", None, "archive-x.zip"),
    ],
)
def test_resolve_output_filename(
    name: str | None,
    default_ext: str | None,
    headers: HeadersType | None,
    expected: str,
) -> None:
    default_base = "archive-x" if expected.startswith("archive-x") else "orig-123"
    assert (
        download_utils.resolve_output_filename(
            headers,
            name=name,
            default_base=default_base,
            default_ext=default_ext,
        )
        == expected
    )


def test_resolve_output_filename_rejects_default_ext_without_dot() -> None:
    with pytest.raises(ValueError, match="default_ext must start with"):
        download_utils.resolve_output_filename(
            None, name=None, default_base="x", default_ext="zip"
        )


class MockResponse:
    """Mock aiohttp.ClientResponse for testing."""

    def __init__(
        self,
        headers: HeadersType,
        status: int = 200,
        content_data: bytes = b"test data",
        chunk_size: int = 1024 * 1024,
    ):
        self.headers = headers
        self.status = status
        self._content_data = content_data
        self._chunk_size = chunk_size
        self._closed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._closed = True

    @property
    def closed(self):
        return self._closed

    @property
    def content(self):
        """Return a mock content object with iter_chunked method."""
        data = self._content_data

        class MockContent:
            def iter_chunked(self, size):
                async def _iter():
                    offset = 0
                    while offset < len(data):
                        chunk = data[offset : offset + size]
                        offset += size
                        yield chunk

                return _iter()

        return MockContent()


@pytest.mark.asyncio
async def test_download_file_basic_download(tmp_path: Path) -> None:
    """Test basic file download with no existing files."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    content_data = b"test file content" * 1000
    headers = {"Content-Length": str(len(content_data))}

    async def make_request(headers_arg):
        return MockResponse(headers, content_data=content_data)

    def resolve_filename(h):
        return "test.txt"

    result = await download_utils.download_file(make_request, out_dir, resolve_filename)

    assert result == out_dir / "test.txt"
    assert result.exists()
    assert result.read_bytes() == content_data
    assert not (out_dir / "test.txt.temp").exists()


@pytest.mark.asyncio
async def test_download_file_file_already_exists_complete(tmp_path: Path) -> None:
    """Test that existing complete file is returned without re-downloading."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    content_data = b"existing content"
    existing_file = out_dir / "existing.txt"
    existing_file.write_bytes(content_data)

    headers = {"Content-Length": str(len(content_data))}

    request_count = 0

    async def make_request(headers_arg):
        nonlocal request_count
        request_count += 1
        # Function always calls make_request first to get headers
        return MockResponse(headers, content_data=content_data)

    def resolve_filename(h):
        return "existing.txt"

    result = await download_utils.download_file(make_request, out_dir, resolve_filename)

    assert result == existing_file
    assert result.read_bytes() == content_data
    # Should only call make_request once to get headers, then return early
    assert request_count == 1


@pytest.mark.asyncio
async def test_download_file_file_already_exists_incomplete(tmp_path: Path) -> None:
    """Test that file with size mismatch is not re-downloaded for security reasons."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    partial_data = b"partial"
    existing_file = out_dir / "incomplete.txt"
    existing_file.write_bytes(partial_data)

    full_content = b"complete file content"
    headers = {"Content-Length": str(len(full_content))}

    request_count = 0

    async def make_request(headers_arg):
        nonlocal request_count
        request_count += 1
        # Should only be called once to get headers, then return early
        return MockResponse(headers, content_data=full_content)

    def resolve_filename(h):
        return "incomplete.txt"

    result = await download_utils.download_file(make_request, out_dir, resolve_filename)

    # File should not be re-downloaded - original content preserved for security
    assert result == existing_file
    assert result.read_bytes() == partial_data
    # Should only make one request to get headers, then return early with warning
    assert request_count == 1


@pytest.mark.asyncio
async def test_download_file_resume_from_temp_file(tmp_path: Path) -> None:
    """Test resuming download from existing temp file."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    partial_data = b"partial data"
    temp_file = out_dir / "resume.txt.temp"
    temp_file.write_bytes(partial_data)

    full_content = b"partial data" + b"remaining content"
    headers = {"Content-Length": str(len(full_content))}

    request_count = 0

    async def make_request(headers_arg):
        nonlocal request_count
        request_count += 1
        if headers_arg and "Range" in headers_arg:
            # Resume request
            assert headers_arg["Range"] == f"bytes={len(partial_data)}-"
            return MockResponse(headers, status=206, content_data=b"remaining content")
        # Initial request
        return MockResponse(headers, content_data=full_content)

    def resolve_filename(h):
        return "resume.txt"

    result = await download_utils.download_file(
        make_request, out_dir, resolve_filename, resumeable=True
    )

    assert result == out_dir / "resume.txt"
    assert result.read_bytes() == full_content
    assert not temp_file.exists()
    assert request_count == 2  # Initial + resume


@pytest.mark.asyncio
async def test_download_file_resume_not_supported_by_server(tmp_path: Path) -> None:
    """Test that when server doesn't support Range, download restarts."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    partial_data = b"partial"
    temp_file = out_dir / "no_resume.txt.temp"
    temp_file.write_bytes(partial_data)

    full_content = b"complete content"
    headers = {"Content-Length": str(len(full_content))}

    request_count = 0

    async def make_request(headers_arg):
        nonlocal request_count
        request_count += 1
        if headers_arg and "Range" in headers_arg:
            # Server doesn't support Range - returns 200 instead of 206
            return MockResponse(headers, status=200, content_data=full_content)
        # Initial or restart request
        return MockResponse(headers, content_data=full_content)

    def resolve_filename(h):
        return "no_resume.txt"

    result = await download_utils.download_file(
        make_request, out_dir, resolve_filename, resumeable=True
    )

    assert result == out_dir / "no_resume.txt"
    assert result.read_bytes() == full_content
    assert not temp_file.exists()
    # Should have: initial, resume attempt (fails), restart
    assert request_count >= 2


@pytest.mark.asyncio
async def test_download_file_temp_file_complete_deletes_and_restarts(
    tmp_path: Path,
) -> None:
    """Test that complete temp file is deleted and download restarts."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    # Temp file with same size as expected (should be deleted and restarted)
    temp_file = out_dir / "complete_temp.txt.temp"
    temp_file.write_bytes(b"old content")

    full_content = b"new content"
    headers = {"Content-Length": str(len(full_content))}

    async def make_request(headers_arg):
        return MockResponse(headers, content_data=full_content)

    def resolve_filename(h):
        return "complete_temp.txt"

    result = await download_utils.download_file(make_request, out_dir, resolve_filename)

    assert result == out_dir / "complete_temp.txt"
    assert result.read_bytes() == full_content
    assert not temp_file.exists()


@pytest.mark.asyncio
async def test_download_file_raises_error_if_out_dir_is_not_directory(
    tmp_path: Path,
) -> None:
    """Test that ValueError is raised if out_dir is not a directory."""
    out_dir = tmp_path / "file.txt"
    out_dir.write_text("not a dir")

    headers = {"Content-Length": "10"}

    async def make_request(headers_arg):
        return MockResponse(headers, content_data=b"data")

    def resolve_filename(h):
        return "test.txt"

    # is_dir() check happens before mkdir(), so ValueError is raised
    with pytest.raises(ValueError, match="out_dir must be a directory"):
        await download_utils.download_file(make_request, out_dir, resolve_filename)
    # Temp file should not exist since error occurred before temp_path was set
    assert not (tmp_path / "test.txt.temp").exists()


@pytest.mark.asyncio
async def test_download_file_handles_empty_chunks(tmp_path: Path) -> None:
    """Test that empty chunks are skipped."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    content_data = b"data"
    headers = {"Content-Length": str(len(content_data))}

    class MockResponseWithEmptyChunks:
        def __init__(self):
            self.headers = headers
            self.status = 200
            self._closed = False

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            self.close()

        def close(self):
            self._closed = True

        @property
        def closed(self):
            return self._closed

        @property
        def content(self):
            class MockContent:
                def iter_chunked(self, size):
                    async def _iter():
                        yield b"da"
                        yield b""  # Empty chunk should be skipped
                        yield b"ta"
                        yield b""  # Another empty chunk

                    return _iter()

            return MockContent()

    async def make_request(headers_arg):
        return MockResponseWithEmptyChunks()

    def resolve_filename(h):
        return "empty_chunks.txt"

    result = await download_utils.download_file(make_request, out_dir, resolve_filename)

    assert result.read_bytes() == content_data


@pytest.mark.asyncio
async def test_download_file_cleans_up_temp_file_on_error(tmp_path: Path) -> None:
    """Test that temp file is deleted when an error occurs during download."""
    out_dir = tmp_path / "downloads"
    out_dir.mkdir()

    content_data = b"test"
    headers = {"Content-Length": str(len(content_data))}

    class FailingResponse(MockResponse):
        @property
        def content(self):
            class MockContent:
                def iter_chunked(self, size):
                    async def _iter():
                        yield b"te"
                        raise RuntimeError("Read error")

                    return _iter()

            return MockContent()

    async def make_request(headers_arg):
        return FailingResponse(headers, content_data=content_data)

    def resolve_filename(h):
        return "error.txt"

    with pytest.raises(RuntimeError, match="Read error"):
        await download_utils.download_file(make_request, out_dir, resolve_filename)

    # Temp file should not exist after error
    assert not (out_dir / "error.txt.temp").exists()
