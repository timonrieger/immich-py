# Immich API Client

<p align="center">
    <a href="https://coderabbit.ai" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/coderabbit/prs/github/timonrieger/immich-python-client?utm_source=oss&utm_medium=github&utm_campaign=timonrieger%2Fimmich-python-client&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews" alt="CodeRabbit Pull Request Reviews">
    </a>
    <a href="https://github.com/timonrieger/immich-python-client/actions/workflows/test.yml">
        <img src="https://github.com/timonrieger/immich-python-client/actions/workflows/test.yml/badge.svg" alt="Tests">
    </a>
    <a href="https://pypi.org/project/immich" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/pypi/v/immich?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pypi.org/project/immich" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/pypi/pyversions/immich.svg?color=%2334D058" alt="Supported Python versions">
    </a>
</p>

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

## Custom functions

Some API groups include custom convenience methods that are **preferred** over the auto-generated ones for common operations:

### Assets API

- **assets.download_asset_to_file**: Download an asset (original file) directly to disk.
- **assets.view_asset_to_file**: Download an asset thumbnail directly to disk .

### Download API

- **download.download_archive_to_file**: Download asset archives (ZIP files) directly to disk. You can download whole albums or user-specified assets in a single request.

### Users API

- **users.get_profile_image_to_file**: Download a user's profile image directly to disk.

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

## Response Types

There are three different available output formats you can choose from:

### Serialized Response

You can get fully serialized responses as Pydantic models. Using this, you get the full benefits of Pydantic's type checking.

```python
res = await client.server.get_about_info()
```

The output would look like this:

```python
ServerAboutResponseDto(...)
```

### Serialized Response with HTTP Info

```python
res = await client.server.get_about_info_with_http_info()
```

The output would look like this:

```python
status_code=200 headers={'Content-Type': 'application/json'} data=ServerAboutResponseDto(...) raw_data=b'{"...": "..."}'
```

### JSON Response

You can receive a classical JSON response by suffixing the function name with `_without_preload_content`:

```python
response = await client.server.get_about_info_without_preload_content()
await response.json()
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
