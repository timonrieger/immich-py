# Getting Started

## Installation

You need Python 3.10–3.14 installed to be able to use this library.

<div class="termy">

```console
$ pip install immich

---> 100%
```

</div>

## Structure

This SDK is **async-only**. The client exposes API groups as attributes, and endpoints as methods on those groups. Groups and endpoints are documented in the [Immich API documentation](https://api.immich.app/endpoints) or under the [Reference](reference/client.md) section.

## Set up your Immich server

1. Have your Immich server running or use the [demo server](https://demo.immich.app).
2. Get an API key from your [Immich account settings](https://my.immich.app/user-settings?isOpen=api-keys).

## Basic Usage

With a context manager (recommended):

```python title="main.py"
from immich import AsyncClient

async with AsyncClient(api_key="your-immich-api-key", base_url="http://localhost:2283/api") as client:
    await client.server.get_about_info()
```

Run it with
<div class="termy">

```console
$ python main.py

{
  "build": "20375083601",
  "version": "v2.4.1",
}
```

??? note "Alternative"
    Without a context manager:

    ```python title="main.py"
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
