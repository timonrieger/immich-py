# Session management

The client manages a shared `aiohttp.ClientSession` by default. If you need more control over the session, you can pass your own via `http_client=...`. In that case, you are responsible for its lifecycle, meaning you need to close it in your own code.

```python hl_lines="1 7 12"
>>> from aiohttp import ClientSession
>>> from immich import AsyncClient
>>> custom_session = ClientSession()

>>> client = AsyncClient(
      base_url="http://localhost:2283/api",
      http_client=custom_session,
      api_key="your-immich-api-key",
  )
>>> await client.server.get_about_info()
>>> await client.close()
>>> await custom_session.close()
```
