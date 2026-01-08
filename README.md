
<h1 align="center">Immich API Client</h1>
<h3 align="center">Unofficial Python client for the <a href="https://immich.app">Immich</a> API.</h3>
<p align="center">
<a href="https://github.com/immich-app/immich/releases" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/dynamic/regex?url=https://raw.githubusercontent.com/timonrieger/immich-python-client/main/IMMICH-VERSION&search=(.*)&replace=%241%20-%20$1&label=supported%20Immich%20versions&color=blue" alt="Supported Immich version">
</a>
    <a href="https://pypi.org/project/immich" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/pypi/v/immich?color=blue&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pypi.org/project/immich" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/pypi/pyversions/immich.svg?color=blue" alt="Supported Python versions">
    </a>
    <a href="https://pypi.org/project/immich" target="_blank" rel="noopener noreferrer">
        <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/immich?color=blue">
    </a>
    <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/timonrieger/immich-python-client/cd.yml?branch=main&event=push&logo=github&label=Continuous%20Delivery&color=blue">
    <a href="https://github.com/timonrieger/immich-python-client" target="_blank" rel="noopener noreferrer">
        <img alt="GitHub Repository" src="https://img.shields.io/badge/Github-repository-blue?logo=github&color=blue">
    </a>

</p>

> [!IMPORTANT]
> This repository is mostly **auto-generated** from the Immich OpenAPI specification.
> Pull requests are welcome, but modifications to auto-generated code will be rejected. See [CONTRIBUTING](CONTRIBUTING.md) for more details.

> [!NOTE]
> This project is [auto-synced](./.github/workflows/upstream-sync.yml) with the **latest Immich release**.

> [!NOTE]
> This project is not affiliated with or endorsed by Immich.


## Versioning

This package follows **[Semantic Versioning](https://semver.org)**. Some important notes:

- **Package version is not the server version**: `immich` package `x.y.z` is the client’s own version.
- **Upstream breaking changes ⇒ major bump**: Breaking Immich changes produce a new **major** version of this package.
- **Supported Immich server version**: [IMMICH-VERSION](./IMMICH-VERSION) tracks the Immich version the client was generated from. [COMPATIBILITY.csv](./COMPATIBILITY.csv) maps package versions to supported server versions.

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
- **assets.play_asset_video_to_file**: Download an asset video stream directly to disk.

**Resumable Downloads**: All asset download methods support automatic resumable downloads.

### Download API

- **download.download_archive_to_file**: Download asset archives (ZIP files) directly to disk. You can download whole albums or user-specified assets in a single request.

**Note**: Archive downloads (ZIP files) do not support resumable downloads due to the nature of streaming archives.

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
