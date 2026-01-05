# Immich API Client

Unofficial Python client for the [Immich](https://immich.app) API.

> [!IMPORTANT]
> This repository is **auto-generated** from the Immich OpenAPI specification.
> **Do not open pull requests**. See [CONTRIBUTING](CONTRIBUTING.md) for more details.

## Status

- **Unofficial**: Not affiliated with or endorsed by Immich.
- **Auto-synced**: Kept in sync with the **latest Immich release** (regenerated as upstream changes land).

## Installation

You need Python 3.10–3.14 installed to be able to use this library.

Install the latest stable version from PyPI:

```bash
pip install immich
```

If you want the latest version (which may be a pre-release):

```bash
pip install --pre immich
```

## Structure

This SDK is **async-only**. The client exposes API groups as attributes, and endpoints as methods on those groups. Groups and endpoints are documented in the [Immich API documentation](https://api.immich.app/endpoints).

## Authentication

Immich supports API keys. Create one in your server and pass it via `api_key=...`. Cookie and Bearer tokens are also supported.

## Usage

With a context manager (recommended):

```python
from immich import AsyncClient

async with AsyncClient(api_key="your-immich-api-key", base_url="http://localhost:2283/api") as client:
    await client.server.get_about_info()
```

Without a context manager:

```python
import asyncio
from immich import AsyncClient

async def main():
    client = AsyncClient(api_key="your-immich-api-key", base_url="http://localhost:2283/api")
    try:
        await client.server.get_about_info()
    finally:
        await client.close()

asyncio.run(main())
```

## Session management

The client can manage a shared `aiohttp.ClientSession`, or you can pass your own via `http_client=...` (you are responsible for its lifecycle).

## Versioning

This package follows **[Semantic Versioning](https://semver.org)**.

- **Package version is not the server version**: `immich` package `X.Y.Z` is the client’s own version.
- **Upstream breaking changes ⇒ major bump**: Breaking Immich changes that require breaking client changes produce a new **major** version.
- **Supported Immich server version**: `IMMICH-VERSION` (repo root) tracks the Immich version this client was generated from.
  - If you run an **older** Immich server version, you can install an **older** `immich` package release where `IMMICH-VERSION` matches your server.
  - This client supports **Immich v2.4.1** and above.
