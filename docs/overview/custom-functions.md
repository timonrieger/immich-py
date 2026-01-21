# Custom functions

While most of the API is auto-generated, some API groups include custom convenience methods that are **preferred** over the auto-generated ones for common operations as they make it easier to use the API.

## Assets API

- **assets.download_asset_to_file**: Download an asset (original file) directly to disk.
- **assets.view_asset_to_file**: Download an asset thumbnail directly to disk .
- **assets.play_asset_video_to_file**: Download an asset video stream directly to disk.
- **assets.upload**: Upload assets with smart features (duplicate detection, album management, sidecar support, dry run).

**Resumable Downloads**: All asset download methods support automatic resumable downloads.

## Download API

- **download.download_archive_to_file**: Download asset archives (ZIP files) directly to disk. You can download whole albums or user-specified assets in a single request.

**Note**: Archive downloads (ZIP files) do not support resumable downloads due to the nature of streaming archives.

## Users API

- **users.get_profile_image_to_file**: Download a user's profile image directly to disk.
