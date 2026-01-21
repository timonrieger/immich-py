# Custom functions

While most of the API is auto-generated, some API groups include custom convenience methods that are **preferred** over the auto-generated ones for common operations as they make it easier to use the API.

## Assets API

- Download an asset (original file) directly to disk. ([CLI](../cli/reference.md#immich-assets-download-asset-to-file), [Client](../client/reference/wrapper/assets_api_wrapped.md#immich.client.wrapper.assets_api_wrapped.AssetsApiWrapped.download_asset_to_file))
- Download an asset thumbnail directly to disk. ([CLI](../cli/reference.md#immich-assets-view-asset-to-file), [Client](../client/reference/wrapper/assets_api_wrapped.md#immich.client.wrapper.assets_api_wrapped.AssetsApiWrapped.view_asset_to_file))
- Download an asset video stream directly to disk. ([CLI](../cli/reference.md#immich-assets-play-asset-video-to-file), [Client](../client/reference/wrapper/assets_api_wrapped.md#immich.client.wrapper.assets_api_wrapped.AssetsApiWrapped.play_asset_video_to_file))
- Upload assets with smart features. ([CLI](../cli/reference.md#immich-assets-upload), [Client](../client/reference/wrapper/assets_api_wrapped.md#immich.client.wrapper.assets_api_wrapped.AssetsApiWrapped.upload))

!!! info "Resumable Downloads"
    All of the asset download methods support automatic resumable downloads.

## Download API

- Download asset archives (ZIP files) directly to disk. You can download whole albums or user-specified assets in a single request. ([CLI](../cli/reference.md#immich-download-download-archive-to-file), [Client](../client/reference/wrapper/download_api_wrapped.md#immich.client.wrapper.download_api_wrapped.DownloadApiWrapped.download_archive_to_file))

!!! info "Resumable Downloads"
    Archive downloads (ZIP files) do not support resumable downloads due to the nature of streaming archives.

## Users API

- Download a user's profile image directly to disk. ([CLI](../cli/reference.md#immich-users-get-profile-image-to-file), [Client](../client/reference/wrapper/users_api_wrapped.md#immich.client.wrapper.users_api_wrapped.UsersApiWrapped.get_profile_image_to_file))
