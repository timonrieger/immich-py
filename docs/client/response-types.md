# Response Types

There are three different available output formats you can choose from:

## Serialized Response

You can get fully serialized responses as [Pydantic](https://docs.pydantic.dev/) models.

```python
await client.server.get_about_info()
```

The output would look like this:

```python
ServerAboutResponseDto(
    build='20375083601',
    build_image='main',
    ...
    version='v2.4.1',
    version_url='https://github.com/immich-app/immich/releases/tag/v2.4.1'
)
```


## Serialized Response with HTTP Info

To get additional metadata about the HTTP response by suffixing the function name with `_with_http_info`.

```python
await client.server.get_about_info_with_http_info()
```
```python
ApiResponse(
    status_code=200,
    headers={'Content-Type': 'application/json'},
    data=ServerAboutResponseDto(
        build='20375083601',
        build_image='main',
        ...
        version='v2.4.1',
        version_url='https://github.com/immich-app/immich/releases/tag/v2.4.1'
    ),
    raw_data=b'{"build":"20375083601","buildImage":"main",...}'
)
```

## JSON Response

You can receive a classical JSON response by suffixing the function name with `_without_preload_content`:

```python
response = await client.server.get_about_info_without_preload_content()
await response.json() # (1)!
```

1. The response is a `aiohttp.ClientResponse` object, which needs to be awaited to get the JSON data.

```json
{
    "build": "20375083601",
    "buildImage": "main",
    ...
    "version": "v2.4.1",
    "versionUrl": "https://github.com/immich-app/immich/releases/tag/v2.4.1"
}
```
