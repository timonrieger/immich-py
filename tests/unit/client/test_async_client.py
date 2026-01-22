import pytest

from immich import AsyncClient
from immich.client.generated.api.assets_api import AssetsApi
from immich.client.generated.api.users_api import UsersApi


@pytest.mark.asyncio
async def test_client_requires_base_url():
    with pytest.raises(TypeError):
        AsyncClient()  # type: ignore[call-arg]


@pytest.mark.asyncio
async def test_client_exposes_api_groups():
    async with AsyncClient(base_url="http://localhost:2283/api") as client:
        assert isinstance(client.assets, AssetsApi)
        assert isinstance(client.users, UsersApi)


@pytest.mark.asyncio
async def test_client_passes_parameters():
    async with AsyncClient(
        base_url="http://localhost:2283/api", api_key="test", access_token="test"
    ) as client:
        assert client.base_client.configuration.host == "http://localhost:2283/api"
        assert client.base_client.configuration.api_key == {"api_key": "test"}
        assert client.base_client.configuration.access_token == "test"


@pytest.mark.asyncio
async def test_client_normalizes_base_url():
    async with AsyncClient(base_url="http://localhost:2283/api/") as client:
        assert client.base_client.configuration.host == "http://localhost:2283/api"
