from pathlib import Path
from typing import AsyncGenerator, Awaitable, Callable, Generator, Optional

import pytest
from uuid import uuid4

from immich import AsyncClient
from immich.client.generated.models.album_response_dto import AlbumResponseDto
from tests.generators import make_random_image, make_random_video


@pytest.fixture
def mock_config_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Fixture that patches CONFIG_DIR and CONFIG_FILE to use tmp_path."""
    config_dir = tmp_path / ".immich-py"
    config_file = config_dir / "config.toml"

    monkeypatch.setattr("immich.cli.consts.CONFIG_DIR", config_dir)
    monkeypatch.setattr("immich.cli.consts.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich.cli.utils.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich.cli.wrapper.setup.CONFIG_FILE", config_file)
    monkeypatch.setattr("immich.cli.wrapper.config.CONFIG_FILE", config_file)

    return config_file


@pytest.fixture
def test_image_factory(
    tmp_path: Path,
) -> Generator[Callable[[Optional[str]], Path], None, None]:
    """Factory fixture: yields a callable to create test images.

    Example:
        img_path = test_image_factory()
        img_path2 = test_image_factory(filename="custom.jpg")
    """

    def _create_image(filename: Optional[str] = None) -> Path:
        if filename is None:
            filename = f"{uuid4()}.jpg"
        img_path = tmp_path / filename
        img_path.write_bytes(make_random_image())
        return img_path

    yield _create_image


@pytest.fixture
def test_image(
    test_image_factory: Callable[[], Path],
) -> Generator[Path, None, None]:
    """Create a minimal JPEG test image."""
    yield test_image_factory()


@pytest.fixture
def test_video_factory(
    tmp_path: Path,
) -> Generator[Callable[[Optional[str]], Path], None, None]:
    """Factory fixture: yields a callable to create test videos.

    Example:
        video_path = test_video_factory()
        video_path2 = test_video_factory(filename="custom.mp4")
    """

    def _create_video(filename: Optional[str] = None) -> Path:
        if filename is None:
            filename = f"{uuid4()}.mp4"
        video_path = tmp_path / filename
        video_path.write_bytes(make_random_video())
        return video_path

    yield _create_video


@pytest.fixture
def test_video(
    test_video_factory: Callable[[], Path],
) -> Generator[Path, None, None]:
    """Create a minimal MP4 test video."""
    yield test_video_factory()


@pytest.fixture
async def album_factory(
    client_with_api_key: AsyncClient,
) -> AsyncGenerator[Callable[..., Awaitable[AlbumResponseDto]], None]:
    """Fixture to set up album for testing with factory pattern.

    Creates an album, returns parsed album object.
    Skips dependent tests if album creation fails.
    """

    async def _create_album(*args, **kwargs) -> AlbumResponseDto:
        try:
            result = await client_with_api_key.albums.create_album(*args, **kwargs)
        except Exception as e:
            pytest.skip(f"Asset upload failed:\n{e}")

        return result

    yield _create_album
