import pytest
from aiohttp import ClientSession

from immich import AsyncClient


@pytest.mark.asyncio
async def test_default_session():
    client = AsyncClient(base_url="http://localhost:2283/api")
    assert client.base_client.rest_client.pool_manager is None
    await client.close()
    assert client.base_client.rest_client.pool_manager is None


@pytest.mark.asyncio
async def test_custom_session():
    custom_session = ClientSession()
    client = AsyncClient(
        base_url="http://localhost:2283/api", http_client=custom_session
    )
    assert client.base_client.rest_client.pool_manager is custom_session
    await client.close()
    assert not custom_session.closed
    await custom_session.close()
    assert custom_session.closed
    assert client.base_client.rest_client.pool_manager is None


@pytest.mark.asyncio
async def test_context_manager():
    async with AsyncClient(base_url="http://localhost:2283/api") as client:
        assert client.base_client is not None

    assert client.base_client.rest_client.pool_manager is None
