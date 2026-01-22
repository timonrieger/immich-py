# Reference

**Usage**:

```console
$ immich [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --verbose`: Show verbose output.
* `--format [pretty|json|table]`: Output format of the CLI.  [env var: IMMICH_FORMAT; default: pretty]
* `--api-key TEXT`: Authorize via API key (get one <a href="https://my.immich.app/user-settings?isOpen=api-keys">here</a>).  [env var: IMMICH_API_KEY]
* `--access-token TEXT`: Authorize via access token.  [env var: IMMICH_ACCESS_TOKEN]
* `--base-url TEXT`: The server to connect to.  [env var: IMMICH_API_URL]
* `-p, --profile TEXT`: The profile to use.  [env var: IMMICH_PROFILE; default: default]
* `--version`: Show version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `setup`: Interactively set up a profile for the CLI...
* `api-keys`: An api key can be used to programmatically...
* `activities`: An activity is a like or a comment made by...
* `albums`: An album is a collection of assets that...
* `assets`: An asset is an image or video that has...
* `auth`: Endpoints related to user authentication,...
* `auth-admin`: Administrative endpoints related to...
* `download`: Endpoints for downloading assets or...
* `config`: Configure the CLI with server details,...
* `duplicates`: Endpoints for managing and identifying...
* `faces`: A face is a detected human face within an...
* `jobs`: Queues and background jobs are used for...
* `libraries`: An external library is made up of input...
* `maintenance-admin`: Maintenance mode allows you to put Immich...
* `map`: Map endpoints include supplemental...
* `memories`: A memory is a specialized collection of...
* `notifications`: A notification is a specialized message...
* `notifications-admin`: Notification administrative endpoints.
* `partners`: A partner is a link with another user that...
* `people`: A person is a collection of faces, which...
* `plugins`: A plugin is an installed module that makes...
* `queues`: Queues and background jobs are used for...
* `search`: Endpoints related to searching assets via...
* `server`: Information about the current server...
* `sessions`: A session represents an authenticated...
* `shared-links`: A shared link is a public url that...
* `stacks`: A stack is a group of related assets.
* `sync`: A collection of endpoints for the new...
* `system-config`: Endpoints to view, modify, and validate...
* `system-metadata`: Endpoints to view, modify, and validate...
* `tags`: A tag is a user-defined label that can be...
* `timeline`: Specialized endpoints related to the...
* `trash`: Endpoints for managing the trash can,...
* `users`: Endpoints for viewing and updating the...
* `users-admin`: Administrative endpoints for managing...
* `views`: Endpoints for specialized views, such as...
* `workflows`: A workflow is a set of actions that run...

## `immich setup`

Interactively set up a profile for the CLI to connect to an Immich server.

**Usage**:

```console
$ immich setup [OPTIONS]
```

**Options**:

* `-p, --profile TEXT`: Profile name. This can be used to set different server configurations.  [default: default]
* `--base-url TEXT`: The base URL of the Immich server, including the API path.  [default: https://demo.immich.app/api]
* `--api-key TEXT`: An API key to use with the profile (<span style="color: #008000; text-decoration-color: #008000">recommended</span>)
* `--access-token TEXT`: An access token to use with the profile (<span style="color: #800000; text-decoration-color: #800000">not recommended</span>)
* `--skip-validation`: Skip validation of the server.
* `--help`: Show this message and exit.

## `immich api-keys`

An api key can be used to programmatically access the Immich API.

<a href="https://api.immich.app/endpoints/api-keys">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-api-key`: Create an API key
* `delete-api-key`: Delete an API key
* `get-api-key`: Retrieve an API key
* `get-api-keys`: List all API keys
* `get-my-api-key`: Retrieve the current API key
* `update-api-key`: Update an API key

### `immich api-keys create-api-key`

Create an API key

<a href="https://api.immich.app/endpoints/api-keys/createApiKey">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys create-api-key [OPTIONS]
```

**Options**:

* `--name TEXT`
* `--permissions [all|activity.create|activity.read|activity.update|activity.delete|activity.statistics|apiKey.create|apiKey.read|apiKey.update|apiKey.delete|asset.read|asset.update|asset.delete|asset.statistics|asset.share|asset.view|asset.download|asset.upload|asset.replace|asset.copy|album.create|album.read|album.update|album.delete|album.statistics|album.share|album.download|albumAsset.create|albumAsset.delete|albumUser.create|albumUser.update|albumUser.delete|auth.changePassword|authDevice.delete|archive.read|duplicate.read|duplicate.delete|face.create|face.read|face.update|face.delete|job.create|job.read|library.create|library.read|library.update|library.delete|library.statistics|timeline.read|timeline.download|maintenance|memory.create|memory.read|memory.update|memory.delete|memory.statistics|memoryAsset.create|memoryAsset.delete|notification.create|notification.read|notification.update|notification.delete|partner.create|partner.read|partner.update|partner.delete|person.create|person.read|person.update|person.delete|person.statistics|person.merge|person.reassign|pinCode.create|pinCode.update|pinCode.delete|plugin.create|plugin.read|plugin.update|plugin.delete|server.about|server.apkLinks|server.storage|server.statistics|server.versionCheck|serverLicense.read|serverLicense.update|serverLicense.delete|session.create|session.read|session.update|session.delete|session.lock|sharedLink.create|sharedLink.read|sharedLink.update|sharedLink.delete|stack.create|stack.read|stack.update|stack.delete|sync.stream|syncCheckpoint.read|syncCheckpoint.update|syncCheckpoint.delete|systemConfig.read|systemConfig.update|systemMetadata.read|systemMetadata.update|tag.create|tag.read|tag.update|tag.delete|tag.asset|user.read|user.update|userLicense.create|userLicense.read|userLicense.update|userLicense.delete|userOnboarding.read|userOnboarding.update|userOnboarding.delete|userPreference.read|userPreference.update|userProfileImage.create|userProfileImage.read|userProfileImage.update|userProfileImage.delete|queue.read|queue.update|queueJob.create|queueJob.read|queueJob.update|queueJob.delete|workflow.create|workflow.read|workflow.update|workflow.delete|adminUser.create|adminUser.read|adminUser.update|adminUser.delete|adminSession.read|adminAuth.unlinkAll]`: [required]
* `--help`: Show this message and exit.

### `immich api-keys delete-api-key`

Delete an API key

<a href="https://api.immich.app/endpoints/api-keys/deleteApiKey">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys delete-api-key [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich api-keys get-api-key`

Retrieve an API key

<a href="https://api.immich.app/endpoints/api-keys/getApiKey">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys get-api-key [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich api-keys get-api-keys`

List all API keys

<a href="https://api.immich.app/endpoints/api-keys/getApiKeys">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys get-api-keys [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich api-keys get-my-api-key`

Retrieve the current API key

<a href="https://api.immich.app/endpoints/api-keys/getMyApiKey">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys get-my-api-key [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich api-keys update-api-key`

Update an API key

<a href="https://api.immich.app/endpoints/api-keys/updateApiKey">Immich API documentation</a>

**Usage**:

```console
$ immich api-keys update-api-key [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--name TEXT`
* `--permissions [all|activity.create|activity.read|activity.update|activity.delete|activity.statistics|apiKey.create|apiKey.read|apiKey.update|apiKey.delete|asset.read|asset.update|asset.delete|asset.statistics|asset.share|asset.view|asset.download|asset.upload|asset.replace|asset.copy|album.create|album.read|album.update|album.delete|album.statistics|album.share|album.download|albumAsset.create|albumAsset.delete|albumUser.create|albumUser.update|albumUser.delete|auth.changePassword|authDevice.delete|archive.read|duplicate.read|duplicate.delete|face.create|face.read|face.update|face.delete|job.create|job.read|library.create|library.read|library.update|library.delete|library.statistics|timeline.read|timeline.download|maintenance|memory.create|memory.read|memory.update|memory.delete|memory.statistics|memoryAsset.create|memoryAsset.delete|notification.create|notification.read|notification.update|notification.delete|partner.create|partner.read|partner.update|partner.delete|person.create|person.read|person.update|person.delete|person.statistics|person.merge|person.reassign|pinCode.create|pinCode.update|pinCode.delete|plugin.create|plugin.read|plugin.update|plugin.delete|server.about|server.apkLinks|server.storage|server.statistics|server.versionCheck|serverLicense.read|serverLicense.update|serverLicense.delete|session.create|session.read|session.update|session.delete|session.lock|sharedLink.create|sharedLink.read|sharedLink.update|sharedLink.delete|stack.create|stack.read|stack.update|stack.delete|sync.stream|syncCheckpoint.read|syncCheckpoint.update|syncCheckpoint.delete|systemConfig.read|systemConfig.update|systemMetadata.read|systemMetadata.update|tag.create|tag.read|tag.update|tag.delete|tag.asset|user.read|user.update|userLicense.create|userLicense.read|userLicense.update|userLicense.delete|userOnboarding.read|userOnboarding.update|userOnboarding.delete|userPreference.read|userPreference.update|userProfileImage.create|userProfileImage.read|userProfileImage.update|userProfileImage.delete|queue.read|queue.update|queueJob.create|queueJob.read|queueJob.update|queueJob.delete|workflow.create|workflow.read|workflow.update|workflow.delete|adminUser.create|adminUser.read|adminUser.update|adminUser.delete|adminSession.read|adminAuth.unlinkAll]`
* `--help`: Show this message and exit.

## `immich activities`

An activity is a like or a comment made by a user on an asset or album.

<a href="https://api.immich.app/endpoints/activities">Immich API documentation</a>

**Usage**:

```console
$ immich activities [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-activity`: Create an activity
* `delete-activity`: Delete an activity
* `get-activities`: List all activities
* `get-activity-statistics`: Retrieve activity statistics

### `immich activities create-activity`

Create an activity

<a href="https://api.immich.app/endpoints/activities/createActivity">Immich API documentation</a>

**Usage**:

```console
$ immich activities create-activity [OPTIONS]
```

**Options**:

* `--album-id TEXT`: [required]
* `--asset-id TEXT`
* `--comment TEXT`
* `--type TEXT`: [required]
* `--help`: Show this message and exit.

### `immich activities delete-activity`

Delete an activity

<a href="https://api.immich.app/endpoints/activities/deleteActivity">Immich API documentation</a>

**Usage**:

```console
$ immich activities delete-activity [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich activities get-activities`

List all activities

<a href="https://api.immich.app/endpoints/activities/getActivities">Immich API documentation</a>

**Usage**:

```console
$ immich activities get-activities [OPTIONS]
```

**Options**:

* `--album-id TEXT`: [required]
* `--asset-id TEXT`
* `--level [album|asset]`
* `--type [comment|like]`
* `--user-id TEXT`
* `--help`: Show this message and exit.

### `immich activities get-activity-statistics`

Retrieve activity statistics

<a href="https://api.immich.app/endpoints/activities/getActivityStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich activities get-activity-statistics [OPTIONS]
```

**Options**:

* `--album-id TEXT`: [required]
* `--asset-id TEXT`
* `--help`: Show this message and exit.

## `immich albums`

An album is a collection of assets that can be shared with other users or via shared links.

<a href="https://api.immich.app/endpoints/albums">Immich API documentation</a>

**Usage**:

```console
$ immich albums [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add-assets-to-album`: Add assets to an album
* `add-assets-to-albums`: Add assets to albums
* `add-users-to-album`: Share album with users
* `create-album`: Create an album
* `delete-album`: Delete an album
* `get-album-info`: Retrieve an album
* `get-album-statistics`: Retrieve album statistics
* `get-all-albums`: List all albums
* `remove-asset-from-album`: Remove assets from an album
* `remove-user-from-album`: Remove user from album
* `update-album-info`: Update an album
* `update-album-user`: Update user role

### `immich albums add-assets-to-album`

Add assets to an album

<a href="https://api.immich.app/endpoints/albums/addAssetsToAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums add-assets-to-album [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich albums add-assets-to-albums`

Add assets to albums

<a href="https://api.immich.app/endpoints/albums/addAssetsToAlbums">Immich API documentation</a>

**Usage**:

```console
$ immich albums add-assets-to-albums [OPTIONS]
```

**Options**:

* `--album-ids TEXT`: [required]
* `--asset-ids TEXT`: [required]
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich albums add-users-to-album`

Share album with users

<a href="https://api.immich.app/endpoints/albums/addUsersToAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums add-users-to-album [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--album-users TEXT`: As a JSON string  [required]
* `--help`: Show this message and exit.

### `immich albums create-album`

Create an album

<a href="https://api.immich.app/endpoints/albums/createAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums create-album [OPTIONS]
```

**Options**:

* `--album-name TEXT`: [required]
* `--album-users TEXT`: As a JSON string
* `--asset-ids TEXT`
* `--description TEXT`
* `--help`: Show this message and exit.

### `immich albums delete-album`

Delete an album

<a href="https://api.immich.app/endpoints/albums/deleteAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums delete-album [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich albums get-album-info`

Retrieve an album

<a href="https://api.immich.app/endpoints/albums/getAlbumInfo">Immich API documentation</a>

**Usage**:

```console
$ immich albums get-album-info [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--key TEXT`
* `--slug TEXT`
* `--without-assets [true|false]`
* `--help`: Show this message and exit.

### `immich albums get-album-statistics`

Retrieve album statistics

<a href="https://api.immich.app/endpoints/albums/getAlbumStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich albums get-album-statistics [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich albums get-all-albums`

List all albums

<a href="https://api.immich.app/endpoints/albums/getAllAlbums">Immich API documentation</a>

**Usage**:

```console
$ immich albums get-all-albums [OPTIONS]
```

**Options**:

* `--asset-id TEXT`: Only returns albums that contain the asset
Ignores the shared parameter
undefined: get all albums
* `--shared [true|false]`
* `--help`: Show this message and exit.

### `immich albums remove-asset-from-album`

Remove assets from an album

<a href="https://api.immich.app/endpoints/albums/removeAssetFromAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums remove-asset-from-album [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich albums remove-user-from-album`

Remove user from album

<a href="https://api.immich.app/endpoints/albums/removeUserFromAlbum">Immich API documentation</a>

**Usage**:

```console
$ immich albums remove-user-from-album [OPTIONS] ID USER_ID
```

**Arguments**:

* `ID`: [required]
* `USER_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich albums update-album-info`

Update an album

<a href="https://api.immich.app/endpoints/albums/updateAlbumInfo">Immich API documentation</a>

**Usage**:

```console
$ immich albums update-album-info [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--album-name TEXT`
* `--album-thumbnail-asset-id TEXT`
* `--description TEXT`
* `--is-activity-enabled [true|false]`
* `--order TEXT`
* `--help`: Show this message and exit.

### `immich albums update-album-user`

Update user role

<a href="https://api.immich.app/endpoints/albums/updateAlbumUser">Immich API documentation</a>

**Usage**:

```console
$ immich albums update-album-user [OPTIONS] ID USER_ID
```

**Arguments**:

* `ID`: [required]
* `USER_ID`: [required]

**Options**:

* `--role TEXT`: [required]
* `--help`: Show this message and exit.

## `immich assets`

An asset is an image or video that has been uploaded to Immich.

<a href="https://api.immich.app/endpoints/assets">Immich API documentation</a>

**Usage**:

```console
$ immich assets [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `check-bulk-upload`: Check bulk upload
* `check-existing-assets`: Check existing assets
* `copy-asset`: Copy asset
* `delete-asset-metadata`: Delete asset metadata by key
* `delete-assets`: Delete assets
* `download-asset`: Download original asset
* `get-all-user-assets-by-device-id`: Retrieve assets by device ID (DEPRECATED)
* `get-asset-info`: Retrieve an asset
* `get-asset-metadata`: Get asset metadata
* `get-asset-metadata-by-key`: Retrieve asset metadata by key
* `get-asset-ocr`: Retrieve asset OCR data
* `get-asset-statistics`: Get asset statistics
* `get-random`: Get random assets (DEPRECATED)
* `play-asset-video`: Play asset video
* `replace-asset`: Replace asset (DEPRECATED)
* `run-asset-jobs`: Run an asset job
* `update-asset`: Update an asset
* `update-asset-metadata`: Update asset metadata
* `update-assets`: Update assets
* `upload-asset`: Upload asset
* `view-asset`: View asset thumbnail
* `download-asset-to-file`: Download an asset to a file.
* `play-asset-video-to-file`: Save an asset&#x27;s video stream to a file.
* `view-asset-to-file`: Save an asset&#x27;s thumbnail to a file.
* `upload`: Upload assets with smart features.

### `immich assets check-bulk-upload`

Check bulk upload

<a href="https://api.immich.app/endpoints/assets/checkBulkUpload">Immich API documentation</a>

**Usage**:

```console
$ immich assets check-bulk-upload [OPTIONS]
```

**Options**:

* `--assets TEXT`: As a JSON string  [required]
* `--help`: Show this message and exit.

### `immich assets check-existing-assets`

Check existing assets

<a href="https://api.immich.app/endpoints/assets/checkExistingAssets">Immich API documentation</a>

**Usage**:

```console
$ immich assets check-existing-assets [OPTIONS]
```

**Options**:

* `--device-asset-ids TEXT`: [required]
* `--device-id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich assets copy-asset`

Copy asset

<a href="https://api.immich.app/endpoints/assets/copyAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets copy-asset [OPTIONS]
```

**Options**:

* `--albums [true|false]`
* `--favorite [true|false]`
* `--shared-links [true|false]`
* `--sidecar [true|false]`
* `--source-id TEXT`: [required]
* `--stack [true|false]`
* `--target-id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich assets delete-asset-metadata`

Delete asset metadata by key

<a href="https://api.immich.app/endpoints/assets/deleteAssetMetadata">Immich API documentation</a>

**Usage**:

```console
$ immich assets delete-asset-metadata [OPTIONS] ID KEY:{mobile-app}
```

**Arguments**:

* `ID`: [required]
* `KEY:{mobile-app}`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich assets delete-assets`

Delete assets

<a href="https://api.immich.app/endpoints/assets/deleteAssets">Immich API documentation</a>

**Usage**:

```console
$ immich assets delete-assets [OPTIONS]
```

**Options**:

* `--force [true|false]`
* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich assets download-asset`

Download original asset

<a href="https://api.immich.app/endpoints/assets/downloadAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets download-asset [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich assets get-all-user-assets-by-device-id`

Retrieve assets by device ID

<a href="https://api.immich.app/endpoints/assets/getAllUserAssetsByDeviceId">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-all-user-assets-by-device-id [OPTIONS] DEVICE_ID
```

**Arguments**:

* `DEVICE_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich assets get-asset-info`

Retrieve an asset

<a href="https://api.immich.app/endpoints/assets/getAssetInfo">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-asset-info [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich assets get-asset-metadata`

Get asset metadata

<a href="https://api.immich.app/endpoints/assets/getAssetMetadata">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-asset-metadata [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich assets get-asset-metadata-by-key`

Retrieve asset metadata by key

<a href="https://api.immich.app/endpoints/assets/getAssetMetadataByKey">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-asset-metadata-by-key [OPTIONS] ID KEY:{mobile-app}
```

**Arguments**:

* `ID`: [required]
* `KEY:{mobile-app}`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich assets get-asset-ocr`

Retrieve asset OCR data

<a href="https://api.immich.app/endpoints/assets/getAssetOcr">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-asset-ocr [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich assets get-asset-statistics`

Get asset statistics

<a href="https://api.immich.app/endpoints/assets/getAssetStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-asset-statistics [OPTIONS]
```

**Options**:

* `--is-favorite [true|false]`
* `--is-trashed [true|false]`
* `--visibility [archive|timeline|hidden|locked]`
* `--help`: Show this message and exit.

### `immich assets get-random`

Get random assets

<a href="https://api.immich.app/endpoints/assets/getRandom">Immich API documentation</a>

**Usage**:

```console
$ immich assets get-random [OPTIONS]
```

**Options**:

* `--count FLOAT RANGE`: [x&gt;=1]
* `--help`: Show this message and exit.

### `immich assets play-asset-video`

Play asset video

<a href="https://api.immich.app/endpoints/assets/playAssetVideo">Immich API documentation</a>

**Usage**:

```console
$ immich assets play-asset-video [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich assets replace-asset`

Replace asset

<a href="https://api.immich.app/endpoints/assets/replaceAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets replace-asset [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--asset-data PATH`: [required]
* `--device-asset-id TEXT`: [required]
* `--device-id TEXT`: [required]
* `--duration TEXT`
* `--file-created-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--file-modified-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--filename TEXT`
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich assets run-asset-jobs`

Run an asset job

<a href="https://api.immich.app/endpoints/assets/runAssetJobs">Immich API documentation</a>

**Usage**:

```console
$ immich assets run-asset-jobs [OPTIONS]
```

**Options**:

* `--asset-ids TEXT`: [required]
* `--name TEXT`: [required]
* `--help`: Show this message and exit.

### `immich assets update-asset`

Update an asset

<a href="https://api.immich.app/endpoints/assets/updateAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets update-asset [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--date-time-original TEXT`
* `--description TEXT`
* `--is-favorite [true|false]`
* `--latitude FLOAT`
* `--live-photo-video-id TEXT`
* `--longitude FLOAT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--visibility TEXT`
* `--help`: Show this message and exit.

### `immich assets update-asset-metadata`

Update asset metadata

<a href="https://api.immich.app/endpoints/assets/updateAssetMetadata">Immich API documentation</a>

**Usage**:

```console
$ immich assets update-asset-metadata [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--items TEXT`: As a JSON string  [required]
* `--help`: Show this message and exit.

### `immich assets update-assets`

Update assets

<a href="https://api.immich.app/endpoints/assets/updateAssets">Immich API documentation</a>

**Usage**:

```console
$ immich assets update-assets [OPTIONS]
```

**Options**:

* `--date-time-original TEXT`
* `--date-time-relative FLOAT`
* `--description TEXT`
* `--duplicate-id TEXT`
* `--ids TEXT`: [required]
* `--is-favorite [true|false]`
* `--latitude FLOAT`
* `--longitude FLOAT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--time-zone TEXT`
* `--visibility TEXT`
* `--help`: Show this message and exit.

### `immich assets upload-asset`

Upload asset

<a href="https://api.immich.app/endpoints/assets/uploadAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets upload-asset [OPTIONS]
```

**Options**:

* `--asset-data PATH`: [required]
* `--device-asset-id TEXT`: [required]
* `--device-id TEXT`: [required]
* `--duration TEXT`
* `--file-created-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--file-modified-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--filename TEXT`
* `--is-favorite [true|false]`
* `--key TEXT`
* `--live-photo-video-id TEXT`
* `--metadata TEXT`: As a JSON string  [required]
* `--sidecar-data PATH`
* `--slug TEXT`
* `--visibility TEXT`
* `--x-immich-checksum TEXT`: sha1 checksum that can be used for duplicate detection before the file is uploaded
* `--help`: Show this message and exit.

### `immich assets view-asset`

View asset thumbnail

<a href="https://api.immich.app/endpoints/assets/viewAsset">Immich API documentation</a>

**Usage**:

```console
$ immich assets view-asset [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--key TEXT`
* `--size [fullsize|preview|thumbnail]`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich assets download-asset-to-file`

Download an asset to a file.

Downloads the original asset file and saves it to the specified output directory.
The filename can be specified or will be derived from the response headers.

**Usage**:

```console
$ immich assets download-asset-to-file [OPTIONS] ID OUT_DIR
```

**Arguments**:

* `ID`: Asset ID (UUID)  [required]
* `OUT_DIR`: Output directory for the downloaded file  [required]

**Options**:

* `--key TEXT`: Public share key (last path segment of /share/&lt;key&gt;)
* `--slug TEXT`: Public share slug (last path segment of /s/&lt;slug&gt;)
* `--filename TEXT`: Filename to use (defaults to original filename or orig-{asset_id})
* `--show-progress`: Show progress bar while downloading
* `--help`: Show this message and exit.

### `immich assets play-asset-video-to-file`

Save an asset&#x27;s video stream to a file.

Downloads the video stream for the asset and saves it to the specified output directory.
The filename can be specified or will be derived from the response headers.

**Usage**:

```console
$ immich assets play-asset-video-to-file [OPTIONS] ID OUT_DIR
```

**Arguments**:

* `ID`: Asset ID (UUID)  [required]
* `OUT_DIR`: Output directory for the video file  [required]

**Options**:

* `--key TEXT`: Public share key (last path segment of /share/&lt;key&gt;)
* `--slug TEXT`: Public share slug (last path segment of /s/&lt;slug&gt;)
* `--filename TEXT`: Filename to use (defaults to original filename or video-{asset_id})
* `--show-progress`: Show progress bar while downloading
* `--help`: Show this message and exit.

### `immich assets view-asset-to-file`

Save an asset&#x27;s thumbnail to a file.

Downloads the thumbnail for the asset and saves it to the specified output directory.
The filename can be specified or will be derived from the response headers.

**Usage**:

```console
$ immich assets view-asset-to-file [OPTIONS] ID OUT_DIR
```

**Arguments**:

* `ID`: Asset ID (UUID)  [required]
* `OUT_DIR`: Output directory for the thumbnail file  [required]

**Options**:

* `--key TEXT`: Public share key (last path segment of /share/&lt;key&gt;)
* `--slug TEXT`: Public share slug (last path segment of /s/&lt;slug&gt;)
* `--size TEXT`: Thumbnail size: fullsize, preview, or thumbnail
* `--filename TEXT`: Filename to use (defaults to original filename or thumb-{asset_id})
* `--show-progress`: Show progress bar while downloading
* `--help`: Show this message and exit.

### `immich assets upload`

Upload assets with smart features.

Uploads files or directories with duplicate detection, album management, sidecar support, and dry run capability.
Directories are automatically walked recursively.

**Usage**:

```console
$ immich assets upload [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: File or directory paths to upload (can specify multiple)  [required]

**Options**:

* `--ignore-pattern TEXT`: Wildcard pattern to ignore files (uses fnmatch, not regex)
* `--include-hidden`: Include hidden files (starting with &#x27;.&#x27;)
* `--skip-duplicates`: Check for duplicates using SHA1 hashes before uploading
* `--concurrency INTEGER`: Number of concurrent uploads  [default: 5]
* `--show-progress`: Show progress bars
* `--album-name TEXT`: Album name to create or use (if not provided, no album operations are performed)
* `--delete-uploads`: Delete successfully uploaded files locally
* `--delete-duplicates`: Delete rejected duplicate files locally
* `--dry-run`: Simulate uploads without actually uploading
* `--help`: Show this message and exit.

## `immich auth`

Endpoints related to user authentication, including OAuth.

<a href="https://api.immich.app/endpoints/authentication">Immich API documentation</a>

**Usage**:

```console
$ immich auth [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `change-password`: Change password
* `change-pin-code`: Change pin code
* `finish-o-auth`: Finish OAuth
* `get-auth-status`: Retrieve auth status
* `link-o-auth-account`: Link OAuth account
* `lock-auth-session`: Lock auth session
* `login`: Login
* `logout`: Logout
* `redirect-o-auth-to-mobile`: Redirect OAuth to mobile
* `reset-pin-code`: Reset pin code
* `setup-pin-code`: Setup pin code
* `sign-up-admin`: Register admin
* `start-o-auth`: Start OAuth
* `unlink-o-auth-account`: Unlink OAuth account
* `unlock-auth-session`: Unlock auth session
* `validate-access-token`: Validate access token

### `immich auth change-password`

Change password

<a href="https://api.immich.app/endpoints/authentication/changePassword">Immich API documentation</a>

**Usage**:

```console
$ immich auth change-password [OPTIONS]
```

**Options**:

* `--invalidate-sessions [true|false]`
* `--new-password TEXT`: Example: password  [required]
* `--password TEXT`: Example: password  [required]
* `--help`: Show this message and exit.

### `immich auth change-pin-code`

Change pin code

<a href="https://api.immich.app/endpoints/authentication/changePinCode">Immich API documentation</a>

**Usage**:

```console
$ immich auth change-pin-code [OPTIONS]
```

**Options**:

* `--new-pin-code TEXT`: Example: 123456  [required]
* `--password TEXT`
* `--pin-code TEXT`: Example: 123456
* `--help`: Show this message and exit.

### `immich auth finish-o-auth`

Finish OAuth

<a href="https://api.immich.app/endpoints/authentication/finishOAuth">Immich API documentation</a>

**Usage**:

```console
$ immich auth finish-o-auth [OPTIONS]
```

**Options**:

* `--code-verifier TEXT`
* `--state TEXT`
* `--url TEXT`: [required]
* `--help`: Show this message and exit.

### `immich auth get-auth-status`

Retrieve auth status

<a href="https://api.immich.app/endpoints/authentication/getAuthStatus">Immich API documentation</a>

**Usage**:

```console
$ immich auth get-auth-status [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich auth link-o-auth-account`

Link OAuth account

<a href="https://api.immich.app/endpoints/authentication/linkOAuthAccount">Immich API documentation</a>

**Usage**:

```console
$ immich auth link-o-auth-account [OPTIONS]
```

**Options**:

* `--code-verifier TEXT`
* `--state TEXT`
* `--url TEXT`: [required]
* `--help`: Show this message and exit.

### `immich auth lock-auth-session`

Lock auth session

<a href="https://api.immich.app/endpoints/authentication/lockAuthSession">Immich API documentation</a>

**Usage**:

```console
$ immich auth lock-auth-session [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich auth login`

Login

<a href="https://api.immich.app/endpoints/authentication/login">Immich API documentation</a>

**Usage**:

```console
$ immich auth login [OPTIONS]
```

**Options**:

* `--email TEXT`: Example: testuser@email.com  [required]
* `--password TEXT`: Example: password  [required]
* `--help`: Show this message and exit.

### `immich auth logout`

Logout

<a href="https://api.immich.app/endpoints/authentication/logout">Immich API documentation</a>

**Usage**:

```console
$ immich auth logout [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich auth redirect-o-auth-to-mobile`

Redirect OAuth to mobile

<a href="https://api.immich.app/endpoints/authentication/redirectOAuthToMobile">Immich API documentation</a>

**Usage**:

```console
$ immich auth redirect-o-auth-to-mobile [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich auth reset-pin-code`

Reset pin code

<a href="https://api.immich.app/endpoints/authentication/resetPinCode">Immich API documentation</a>

**Usage**:

```console
$ immich auth reset-pin-code [OPTIONS]
```

**Options**:

* `--password TEXT`
* `--pin-code TEXT`: Example: 123456
* `--help`: Show this message and exit.

### `immich auth setup-pin-code`

Setup pin code

<a href="https://api.immich.app/endpoints/authentication/setupPinCode">Immich API documentation</a>

**Usage**:

```console
$ immich auth setup-pin-code [OPTIONS]
```

**Options**:

* `--pin-code TEXT`: Example: 123456  [required]
* `--help`: Show this message and exit.

### `immich auth sign-up-admin`

Register admin

<a href="https://api.immich.app/endpoints/authentication/signUpAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich auth sign-up-admin [OPTIONS]
```

**Options**:

* `--email TEXT`: Example: testuser@email.com  [required]
* `--name TEXT`: Example: Admin  [required]
* `--password TEXT`: Example: password  [required]
* `--help`: Show this message and exit.

### `immich auth start-o-auth`

Start OAuth

<a href="https://api.immich.app/endpoints/authentication/startOAuth">Immich API documentation</a>

**Usage**:

```console
$ immich auth start-o-auth [OPTIONS]
```

**Options**:

* `--code-challenge TEXT`
* `--redirect-uri TEXT`: [required]
* `--state TEXT`
* `--help`: Show this message and exit.

### `immich auth unlink-o-auth-account`

Unlink OAuth account

<a href="https://api.immich.app/endpoints/authentication/unlinkOAuthAccount">Immich API documentation</a>

**Usage**:

```console
$ immich auth unlink-o-auth-account [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich auth unlock-auth-session`

Unlock auth session

<a href="https://api.immich.app/endpoints/authentication/unlockAuthSession">Immich API documentation</a>

**Usage**:

```console
$ immich auth unlock-auth-session [OPTIONS]
```

**Options**:

* `--password TEXT`
* `--pin-code TEXT`: Example: 123456
* `--help`: Show this message and exit.

### `immich auth validate-access-token`

Validate access token

<a href="https://api.immich.app/endpoints/authentication/validateAccessToken">Immich API documentation</a>

**Usage**:

```console
$ immich auth validate-access-token [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich auth-admin`

Administrative endpoints related to authentication.

<a href="https://api.immich.app/endpoints/authentication-admin">Immich API documentation</a>

**Usage**:

```console
$ immich auth-admin [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `unlink-all-o-auth-accounts-admin`: Unlink all OAuth accounts

### `immich auth-admin unlink-all-o-auth-accounts-admin`

Unlink all OAuth accounts

<a href="https://api.immich.app/endpoints/authentication-admin/unlinkAllOAuthAccountsAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich auth-admin unlink-all-o-auth-accounts-admin [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich download`

Endpoints for downloading assets or collections of assets.

<a href="https://api.immich.app/endpoints/download">Immich API documentation</a>

**Usage**:

```console
$ immich download [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `download-archive`: Download asset archive
* `get-download-info`: Retrieve download information
* `download-archive-to-file`: Download one or more asset archives and...

### `immich download download-archive`

Download asset archive

<a href="https://api.immich.app/endpoints/download/downloadArchive">Immich API documentation</a>

**Usage**:

```console
$ immich download download-archive [OPTIONS]
```

**Options**:

* `--asset-ids TEXT`: [required]
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich download get-download-info`

Retrieve download information

<a href="https://api.immich.app/endpoints/download/getDownloadInfo">Immich API documentation</a>

**Usage**:

```console
$ immich download get-download-info [OPTIONS]
```

**Options**:

* `--album-id TEXT`
* `--archive-size INTEGER RANGE`: [x&gt;=1]
* `--asset-ids TEXT`
* `--key TEXT`
* `--slug TEXT`
* `--user-id TEXT`
* `--help`: Show this message and exit.

### `immich download download-archive-to-file`

Download one or more asset archives and save them to ZIP files.

Downloads archives sequentially (not in parallel) to avoid overloading the server.
The download_info parameter can be provided via --json or using dotted flags.

**Usage**:

```console
$ immich download download-archive-to-file [OPTIONS] OUT_DIR
```

**Arguments**:

* `OUT_DIR`: Output directory for the downloaded ZIP archives  [required]

**Options**:

* `--key TEXT`: Public share key (last path segment of /share/&lt;key&gt;)
* `--slug TEXT`: Public share slug (last path segment of /s/&lt;slug&gt;)
* `--show-progress`: Show progress bars (per-archive bytes + overall archive count)
* `--album-id TEXT`: Album ID to download
* `--archive-size INTEGER`: Archive size limit in bytes
* `--asset-ids TEXT`: Asset IDs to download
* `--user-id TEXT`: User ID to download assets from
* `--help`: Show this message and exit.

## `immich config`

Configure the CLI with server details, profiles, and request settings.

**Usage**:

```console
$ immich config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `set`: Set a value in the config file.
* `get`: Get a value from the config file.
* `reset`: Reset the configuration by deleting the...
* `open`: Open the config file in the default editor.

### `immich config set`

Set a value in the config file.

**Usage**:

```console
$ immich config set [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Dot-separated config key  [required]

**Options**:

* `-v, --value TEXT`: Value to set (prompts if not provided)  [required]
* `--help`: Show this message and exit.

### `immich config get`

Get a value from the config file. Secrets are redacted by default.

**Usage**:

```console
$ immich config get [OPTIONS] KEY
```

**Arguments**:

* `KEY`: The key to get from the config  [required]

**Options**:

* `--show-secrets`: Show secret values without redaction
* `--help`: Show this message and exit.

### `immich config reset`

Reset the configuration by deleting the config file.

**Usage**:

```console
$ immich config reset [OPTIONS]
```

**Options**:

* `-y, --yes`: Skip confirmation
* `--help`: Show this message and exit.

### `immich config open`

Open the config file in the default editor.

**Usage**:

```console
$ immich config open [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich duplicates`

Endpoints for managing and identifying duplicate assets.

<a href="https://api.immich.app/endpoints/duplicates">Immich API documentation</a>

**Usage**:

```console
$ immich duplicates [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `delete-duplicate`: Delete a duplicate
* `delete-duplicates`: Delete duplicates
* `get-asset-duplicates`: Retrieve duplicates

### `immich duplicates delete-duplicate`

Delete a duplicate

<a href="https://api.immich.app/endpoints/duplicates/deleteDuplicate">Immich API documentation</a>

**Usage**:

```console
$ immich duplicates delete-duplicate [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich duplicates delete-duplicates`

Delete duplicates

<a href="https://api.immich.app/endpoints/duplicates/deleteDuplicates">Immich API documentation</a>

**Usage**:

```console
$ immich duplicates delete-duplicates [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich duplicates get-asset-duplicates`

Retrieve duplicates

<a href="https://api.immich.app/endpoints/duplicates/getAssetDuplicates">Immich API documentation</a>

**Usage**:

```console
$ immich duplicates get-asset-duplicates [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich faces`

A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.

<a href="https://api.immich.app/endpoints/faces">Immich API documentation</a>

**Usage**:

```console
$ immich faces [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-face`: Create a face
* `delete-face`: Delete a face
* `get-faces`: Retrieve faces for asset
* `reassign-faces-by-id`: Re-assign a face to another person

### `immich faces create-face`

Create a face

<a href="https://api.immich.app/endpoints/faces/createFace">Immich API documentation</a>

**Usage**:

```console
$ immich faces create-face [OPTIONS]
```

**Options**:

* `--asset-id TEXT`: [required]
* `--height INTEGER`: [required]
* `--image-height INTEGER`: [required]
* `--image-width INTEGER`: [required]
* `--person-id TEXT`: [required]
* `--width INTEGER`: [required]
* `--x INTEGER`: [required]
* `--y INTEGER`: [required]
* `--help`: Show this message and exit.

### `immich faces delete-face`

Delete a face

<a href="https://api.immich.app/endpoints/faces/deleteFace">Immich API documentation</a>

**Usage**:

```console
$ immich faces delete-face [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--force`: [required]
* `--help`: Show this message and exit.

### `immich faces get-faces`

Retrieve faces for asset

<a href="https://api.immich.app/endpoints/faces/getFaces">Immich API documentation</a>

**Usage**:

```console
$ immich faces get-faces [OPTIONS]
```

**Options**:

* `--id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich faces reassign-faces-by-id`

Re-assign a face to another person

<a href="https://api.immich.app/endpoints/faces/reassignFacesById">Immich API documentation</a>

**Usage**:

```console
$ immich faces reassign-faces-by-id [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--body-id TEXT`: [required]
* `--help`: Show this message and exit.

## `immich jobs`

Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

<a href="https://api.immich.app/endpoints/jobs">Immich API documentation</a>

**Usage**:

```console
$ immich jobs [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-job`: Create a manual job
* `get-queues-legacy`: Retrieve queue counts and status (DEPRECATED)
* `run-queue-command-legacy`: Run jobs (DEPRECATED)

### `immich jobs create-job`

Create a manual job

<a href="https://api.immich.app/endpoints/jobs/createJob">Immich API documentation</a>

**Usage**:

```console
$ immich jobs create-job [OPTIONS]
```

**Options**:

* `--name TEXT`: [required]
* `--help`: Show this message and exit.

### `immich jobs get-queues-legacy`

Retrieve queue counts and status

<a href="https://api.immich.app/endpoints/jobs/getQueuesLegacy">Immich API documentation</a>

**Usage**:

```console
$ immich jobs get-queues-legacy [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich jobs run-queue-command-legacy`

Run jobs

<a href="https://api.immich.app/endpoints/jobs/runQueueCommandLegacy">Immich API documentation</a>

**Usage**:

```console
$ immich jobs run-queue-command-legacy [OPTIONS] NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}
```

**Arguments**:

* `NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}`: [required]

**Options**:

* `--command TEXT`: [required]
* `--force [true|false]`
* `--help`: Show this message and exit.

## `immich libraries`

An external library is made up of input file paths or expressions that are scanned for asset files. Discovered files are automatically imported. Assets much be unique within a library, but can be duplicated across libraries. Each user has a default upload library, and can have one or more external libraries.

<a href="https://api.immich.app/endpoints/libraries">Immich API documentation</a>

**Usage**:

```console
$ immich libraries [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-library`: Create a library
* `delete-library`: Delete a library
* `get-all-libraries`: Retrieve libraries
* `get-library`: Retrieve a library
* `get-library-statistics`: Retrieve library statistics
* `scan-library`: Scan a library
* `update-library`: Update a library
* `validate`: Validate library settings

### `immich libraries create-library`

Create a library

<a href="https://api.immich.app/endpoints/libraries/createLibrary">Immich API documentation</a>

**Usage**:

```console
$ immich libraries create-library [OPTIONS]
```

**Options**:

* `--exclusion-patterns TEXT`
* `--import-paths TEXT`
* `--name TEXT`
* `--owner-id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich libraries delete-library`

Delete a library

<a href="https://api.immich.app/endpoints/libraries/deleteLibrary">Immich API documentation</a>

**Usage**:

```console
$ immich libraries delete-library [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich libraries get-all-libraries`

Retrieve libraries

<a href="https://api.immich.app/endpoints/libraries/getAllLibraries">Immich API documentation</a>

**Usage**:

```console
$ immich libraries get-all-libraries [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich libraries get-library`

Retrieve a library

<a href="https://api.immich.app/endpoints/libraries/getLibrary">Immich API documentation</a>

**Usage**:

```console
$ immich libraries get-library [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich libraries get-library-statistics`

Retrieve library statistics

<a href="https://api.immich.app/endpoints/libraries/getLibraryStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich libraries get-library-statistics [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich libraries scan-library`

Scan a library

<a href="https://api.immich.app/endpoints/libraries/scanLibrary">Immich API documentation</a>

**Usage**:

```console
$ immich libraries scan-library [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich libraries update-library`

Update a library

<a href="https://api.immich.app/endpoints/libraries/updateLibrary">Immich API documentation</a>

**Usage**:

```console
$ immich libraries update-library [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--exclusion-patterns TEXT`
* `--import-paths TEXT`
* `--name TEXT`
* `--help`: Show this message and exit.

### `immich libraries validate`

Validate library settings

<a href="https://api.immich.app/endpoints/libraries/validate">Immich API documentation</a>

**Usage**:

```console
$ immich libraries validate [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--exclusion-patterns TEXT`
* `--import-paths TEXT`
* `--help`: Show this message and exit.

## `immich maintenance-admin`

Maintenance mode allows you to put Immich in a read-only state to perform various operations.

<a href="https://api.immich.app/endpoints/maintenance-admin">Immich API documentation</a>

**Usage**:

```console
$ immich maintenance-admin [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `maintenance-login`: Log into maintenance mode
* `set-maintenance-mode`: Set maintenance mode

### `immich maintenance-admin maintenance-login`

Log into maintenance mode

<a href="https://api.immich.app/endpoints/maintenance-admin/maintenanceLogin">Immich API documentation</a>

**Usage**:

```console
$ immich maintenance-admin maintenance-login [OPTIONS]
```

**Options**:

* `--token TEXT`
* `--help`: Show this message and exit.

### `immich maintenance-admin set-maintenance-mode`

Set maintenance mode

<a href="https://api.immich.app/endpoints/maintenance-admin/setMaintenanceMode">Immich API documentation</a>

**Usage**:

```console
$ immich maintenance-admin set-maintenance-mode [OPTIONS]
```

**Options**:

* `--action TEXT`: [required]
* `--help`: Show this message and exit.

## `immich map`

Map endpoints include supplemental functionality related to geolocation, such as reverse geocoding and retrieving map markers for assets with geolocation data.

<a href="https://api.immich.app/endpoints/map">Immich API documentation</a>

**Usage**:

```console
$ immich map [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-map-markers`: Retrieve map markers
* `reverse-geocode`: Reverse geocode coordinates

### `immich map get-map-markers`

Retrieve map markers

<a href="https://api.immich.app/endpoints/map/getMapMarkers">Immich API documentation</a>

**Usage**:

```console
$ immich map get-map-markers [OPTIONS]
```

**Options**:

* `--file-created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--file-created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--is-archived [true|false]`
* `--is-favorite [true|false]`
* `--with-partners [true|false]`
* `--with-shared-albums [true|false]`
* `--help`: Show this message and exit.

### `immich map reverse-geocode`

Reverse geocode coordinates

<a href="https://api.immich.app/endpoints/map/reverseGeocode">Immich API documentation</a>

**Usage**:

```console
$ immich map reverse-geocode [OPTIONS]
```

**Options**:

* `--lat FLOAT`: [required]
* `--lon FLOAT`: [required]
* `--help`: Show this message and exit.

## `immich memories`

A memory is a specialized collection of assets with dedicated viewing implementations in the web and mobile clients. A memory includes fields related to visibility and are automatically generated per user via a background job.

<a href="https://api.immich.app/endpoints/memories">Immich API documentation</a>

**Usage**:

```console
$ immich memories [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add-memory-assets`: Add assets to a memory
* `create-memory`: Create a memory
* `delete-memory`: Delete a memory
* `get-memory`: Retrieve a memory
* `memories-statistics`: Retrieve memories statistics
* `remove-memory-assets`: Remove assets from a memory
* `search-memories`: Retrieve memories
* `update-memory`: Update a memory

### `immich memories add-memory-assets`

Add assets to a memory

<a href="https://api.immich.app/endpoints/memories/addMemoryAssets">Immich API documentation</a>

**Usage**:

```console
$ immich memories add-memory-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich memories create-memory`

Create a memory

<a href="https://api.immich.app/endpoints/memories/createMemory">Immich API documentation</a>

**Usage**:

```console
$ immich memories create-memory [OPTIONS]
```

**Options**:

* `--asset-ids TEXT`
* `--data-year FLOAT RANGE`: [x&gt;=1; required]
* `--is-saved [true|false]`
* `--memory-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--seen-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type TEXT`: [required]
* `--help`: Show this message and exit.

### `immich memories delete-memory`

Delete a memory

<a href="https://api.immich.app/endpoints/memories/deleteMemory">Immich API documentation</a>

**Usage**:

```console
$ immich memories delete-memory [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich memories get-memory`

Retrieve a memory

<a href="https://api.immich.app/endpoints/memories/getMemory">Immich API documentation</a>

**Usage**:

```console
$ immich memories get-memory [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich memories memories-statistics`

Retrieve memories statistics

<a href="https://api.immich.app/endpoints/memories/memoriesStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich memories memories-statistics [OPTIONS]
```

**Options**:

* `--for [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--is-saved [true|false]`
* `--is-trashed [true|false]`
* `--order [asc|desc|random]`
* `--size INTEGER RANGE`: Number of memories to return  [x&gt;=1]
* `--type [on_this_day]`
* `--help`: Show this message and exit.

### `immich memories remove-memory-assets`

Remove assets from a memory

<a href="https://api.immich.app/endpoints/memories/removeMemoryAssets">Immich API documentation</a>

**Usage**:

```console
$ immich memories remove-memory-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich memories search-memories`

Retrieve memories

<a href="https://api.immich.app/endpoints/memories/searchMemories">Immich API documentation</a>

**Usage**:

```console
$ immich memories search-memories [OPTIONS]
```

**Options**:

* `--for [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--is-saved [true|false]`
* `--is-trashed [true|false]`
* `--order [asc|desc|random]`
* `--size INTEGER RANGE`: Number of memories to return  [x&gt;=1]
* `--type [on_this_day]`
* `--help`: Show this message and exit.

### `immich memories update-memory`

Update a memory

<a href="https://api.immich.app/endpoints/memories/updateMemory">Immich API documentation</a>

**Usage**:

```console
$ immich memories update-memory [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--is-saved [true|false]`
* `--memory-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--seen-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--help`: Show this message and exit.

## `immich notifications`

A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.

<a href="https://api.immich.app/endpoints/notifications">Immich API documentation</a>

**Usage**:

```console
$ immich notifications [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `delete-notification`: Delete a notification
* `delete-notifications`: Delete notifications
* `get-notification`: Get a notification
* `get-notifications`: Retrieve notifications
* `update-notification`: Update a notification
* `update-notifications`: Update notifications

### `immich notifications delete-notification`

Delete a notification

<a href="https://api.immich.app/endpoints/notifications/deleteNotification">Immich API documentation</a>

**Usage**:

```console
$ immich notifications delete-notification [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich notifications delete-notifications`

Delete notifications

<a href="https://api.immich.app/endpoints/notifications/deleteNotifications">Immich API documentation</a>

**Usage**:

```console
$ immich notifications delete-notifications [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich notifications get-notification`

Get a notification

<a href="https://api.immich.app/endpoints/notifications/getNotification">Immich API documentation</a>

**Usage**:

```console
$ immich notifications get-notification [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich notifications get-notifications`

Retrieve notifications

<a href="https://api.immich.app/endpoints/notifications/getNotifications">Immich API documentation</a>

**Usage**:

```console
$ immich notifications get-notifications [OPTIONS]
```

**Options**:

* `--id TEXT`
* `--level [success|error|warning|info]`
* `--type [JobFailed|BackupFailed|SystemMessage|AlbumInvite|AlbumUpdate|Custom]`
* `--unread [true|false]`
* `--help`: Show this message and exit.

### `immich notifications update-notification`

Update a notification

<a href="https://api.immich.app/endpoints/notifications/updateNotification">Immich API documentation</a>

**Usage**:

```console
$ immich notifications update-notification [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--read-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--help`: Show this message and exit.

### `immich notifications update-notifications`

Update notifications

<a href="https://api.immich.app/endpoints/notifications/updateNotifications">Immich API documentation</a>

**Usage**:

```console
$ immich notifications update-notifications [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--read-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--help`: Show this message and exit.

## `immich notifications-admin`

Notification administrative endpoints.

<a href="https://api.immich.app/endpoints/notifications-admin">Immich API documentation</a>

**Usage**:

```console
$ immich notifications-admin [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-notification`: Create a notification
* `get-notification-template-admin`: Render email template
* `send-test-email-admin`: Send test email

### `immich notifications-admin create-notification`

Create a notification

<a href="https://api.immich.app/endpoints/notifications-admin/createNotification">Immich API documentation</a>

**Usage**:

```console
$ immich notifications-admin create-notification [OPTIONS]
```

**Options**:

* `--data TEXT`: As a JSON string
* `--description TEXT`
* `--level TEXT`
* `--read-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--title TEXT`: [required]
* `--type TEXT`
* `--user-id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich notifications-admin get-notification-template-admin`

Render email template

<a href="https://api.immich.app/endpoints/notifications-admin/getNotificationTemplateAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich notifications-admin get-notification-template-admin [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--template TEXT`: [required]
* `--help`: Show this message and exit.

### `immich notifications-admin send-test-email-admin`

Send test email

<a href="https://api.immich.app/endpoints/notifications-admin/sendTestEmailAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich notifications-admin send-test-email-admin [OPTIONS]
```

**Options**:

* `--enabled`: [required]
* `--from TEXT`: [required]
* `--reply-to TEXT`: [required]
* `--transport-host TEXT`: [required]
* `--transport-ignore-cert`: [required]
* `--transport-password TEXT`: [required]
* `--transport-port FLOAT RANGE`: [0&lt;=x&lt;=65535; required]
* `--transport-secure`: [required]
* `--transport-username TEXT`: [required]
* `--help`: Show this message and exit.

## `immich partners`

A partner is a link with another user that allows sharing of assets between two users.

<a href="https://api.immich.app/endpoints/partners">Immich API documentation</a>

**Usage**:

```console
$ immich partners [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-partner`: Create a partner
* `create-partner-deprecated`: Create a partner (DEPRECATED)
* `get-partners`: Retrieve partners
* `remove-partner`: Remove a partner
* `update-partner`: Update a partner

### `immich partners create-partner`

Create a partner

<a href="https://api.immich.app/endpoints/partners/createPartner">Immich API documentation</a>

**Usage**:

```console
$ immich partners create-partner [OPTIONS]
```

**Options**:

* `--shared-with-id TEXT`: [required]
* `--help`: Show this message and exit.

### `immich partners create-partner-deprecated`

Create a partner

<a href="https://api.immich.app/endpoints/partners/createPartnerDeprecated">Immich API documentation</a>

**Usage**:

```console
$ immich partners create-partner-deprecated [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich partners get-partners`

Retrieve partners

<a href="https://api.immich.app/endpoints/partners/getPartners">Immich API documentation</a>

**Usage**:

```console
$ immich partners get-partners [OPTIONS]
```

**Options**:

* `--direction [shared-by|shared-with]`: [required]
* `--help`: Show this message and exit.

### `immich partners remove-partner`

Remove a partner

<a href="https://api.immich.app/endpoints/partners/removePartner">Immich API documentation</a>

**Usage**:

```console
$ immich partners remove-partner [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich partners update-partner`

Update a partner

<a href="https://api.immich.app/endpoints/partners/updatePartner">Immich API documentation</a>

**Usage**:

```console
$ immich partners update-partner [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--in-timeline`: [required]
* `--help`: Show this message and exit.

## `immich people`

A person is a collection of faces, which can be favorited and named. A person can also be merged into another person. People are automatically created via the face recognition job.

<a href="https://api.immich.app/endpoints/people">Immich API documentation</a>

**Usage**:

```console
$ immich people [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-person`: Create a person
* `delete-people`: Delete people
* `delete-person`: Delete person
* `get-all-people`: Get all people
* `get-person`: Get a person
* `get-person-statistics`: Get person statistics
* `get-person-thumbnail`: Get person thumbnail
* `merge-person`: Merge people
* `reassign-faces`: Reassign faces
* `update-people`: Update people
* `update-person`: Update person

### `immich people create-person`

Create a person

<a href="https://api.immich.app/endpoints/people/createPerson">Immich API documentation</a>

**Usage**:

```console
$ immich people create-person [OPTIONS]
```

**Options**:

* `--birth-date TEXT`: Person date of birth.
Note: the mobile app cannot currently set the birth date to null.
* `--color TEXT`
* `--is-favorite [true|false]`
* `--is-hidden [true|false]`: Person visibility
* `--name TEXT`: Person name.
* `--help`: Show this message and exit.

### `immich people delete-people`

Delete people

<a href="https://api.immich.app/endpoints/people/deletePeople">Immich API documentation</a>

**Usage**:

```console
$ immich people delete-people [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich people delete-person`

Delete person

<a href="https://api.immich.app/endpoints/people/deletePerson">Immich API documentation</a>

**Usage**:

```console
$ immich people delete-person [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich people get-all-people`

Get all people

<a href="https://api.immich.app/endpoints/people/getAllPeople">Immich API documentation</a>

**Usage**:

```console
$ immich people get-all-people [OPTIONS]
```

**Options**:

* `--closest-asset-id TEXT`
* `--closest-person-id TEXT`
* `--page FLOAT RANGE`: Page number for pagination  [x&gt;=1]
* `--size FLOAT RANGE`: Number of items per page  [1&lt;=x&lt;=1000]
* `--with-hidden [true|false]`
* `--help`: Show this message and exit.

### `immich people get-person`

Get a person

<a href="https://api.immich.app/endpoints/people/getPerson">Immich API documentation</a>

**Usage**:

```console
$ immich people get-person [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich people get-person-statistics`

Get person statistics

<a href="https://api.immich.app/endpoints/people/getPersonStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich people get-person-statistics [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich people get-person-thumbnail`

Get person thumbnail

<a href="https://api.immich.app/endpoints/people/getPersonThumbnail">Immich API documentation</a>

**Usage**:

```console
$ immich people get-person-thumbnail [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich people merge-person`

Merge people

<a href="https://api.immich.app/endpoints/people/mergePerson">Immich API documentation</a>

**Usage**:

```console
$ immich people merge-person [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich people reassign-faces`

Reassign faces

<a href="https://api.immich.app/endpoints/people/reassignFaces">Immich API documentation</a>

**Usage**:

```console
$ immich people reassign-faces [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--data TEXT`: As a JSON string  [required]
* `--help`: Show this message and exit.

### `immich people update-people`

Update people

<a href="https://api.immich.app/endpoints/people/updatePeople">Immich API documentation</a>

**Usage**:

```console
$ immich people update-people [OPTIONS]
```

**Options**:

* `--people TEXT`: As a JSON string  [required]
* `--help`: Show this message and exit.

### `immich people update-person`

Update person

<a href="https://api.immich.app/endpoints/people/updatePerson">Immich API documentation</a>

**Usage**:

```console
$ immich people update-person [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--birth-date TEXT`: Person date of birth.
Note: the mobile app cannot currently set the birth date to null.
* `--color TEXT`
* `--feature-face-asset-id TEXT`: Asset is used to get the feature face thumbnail.
* `--is-favorite [true|false]`
* `--is-hidden [true|false]`: Person visibility
* `--name TEXT`: Person name.
* `--help`: Show this message and exit.

## `immich plugins`

A plugin is an installed module that makes filters and actions available for the workflow feature.

<a href="https://api.immich.app/endpoints/plugins">Immich API documentation</a>

**Usage**:

```console
$ immich plugins [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-plugin`: Retrieve a plugin
* `get-plugins`: List all plugins

### `immich plugins get-plugin`

Retrieve a plugin

<a href="https://api.immich.app/endpoints/plugins/getPlugin">Immich API documentation</a>

**Usage**:

```console
$ immich plugins get-plugin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich plugins get-plugins`

List all plugins

<a href="https://api.immich.app/endpoints/plugins/getPlugins">Immich API documentation</a>

**Usage**:

```console
$ immich plugins get-plugins [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich queues`

Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

<a href="https://api.immich.app/endpoints/queues">Immich API documentation</a>

**Usage**:

```console
$ immich queues [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `empty-queue`: Empty a queue
* `get-queue`: Retrieve a queue
* `get-queue-jobs`: Retrieve queue jobs
* `get-queues`: List all queues
* `update-queue`: Update a queue

### `immich queues empty-queue`

Empty a queue

<a href="https://api.immich.app/endpoints/queues/emptyQueue">Immich API documentation</a>

**Usage**:

```console
$ immich queues empty-queue [OPTIONS] NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}
```

**Arguments**:

* `NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}`: [required]

**Options**:

* `--failed [true|false]`: If true, will also remove failed jobs from the queue.
* `--help`: Show this message and exit.

### `immich queues get-queue`

Retrieve a queue

<a href="https://api.immich.app/endpoints/queues/getQueue">Immich API documentation</a>

**Usage**:

```console
$ immich queues get-queue [OPTIONS] NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}
```

**Arguments**:

* `NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich queues get-queue-jobs`

Retrieve queue jobs

<a href="https://api.immich.app/endpoints/queues/getQueueJobs">Immich API documentation</a>

**Usage**:

```console
$ immich queues get-queue-jobs [OPTIONS] NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}
```

**Arguments**:

* `NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}`: [required]

**Options**:

* `--status [active|failed|completed|delayed|waiting|paused]`
* `--help`: Show this message and exit.

### `immich queues get-queues`

List all queues

<a href="https://api.immich.app/endpoints/queues/getQueues">Immich API documentation</a>

**Usage**:

```console
$ immich queues get-queues [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich queues update-queue`

Update a queue

<a href="https://api.immich.app/endpoints/queues/updateQueue">Immich API documentation</a>

**Usage**:

```console
$ immich queues update-queue [OPTIONS] NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}
```

**Arguments**:

* `NAME:{thumbnailGeneration|metadataExtraction|videoConversion|faceDetection|facialRecognition|smartSearch|duplicateDetection|backgroundTask|storageTemplateMigration|migration|search|sidecar|library|notifications|backupDatabase|ocr|workflow}`: [required]

**Options**:

* `--is-paused [true|false]`
* `--help`: Show this message and exit.

## `immich search`

Endpoints related to searching assets via text, smart search, optical character recognition (OCR), and other filters like person, album, and other metadata. Search endpoints usually support pagination and sorting.

<a href="https://api.immich.app/endpoints/search">Immich API documentation</a>

**Usage**:

```console
$ immich search [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-assets-by-city`: Retrieve assets by city
* `get-explore-data`: Retrieve explore data
* `get-search-suggestions`: Retrieve search suggestions
* `search-asset-statistics`: Search asset statistics
* `search-assets`: Search assets by metadata
* `search-large-assets`: Search large assets
* `search-person`: Search people
* `search-places`: Search places
* `search-random`: Search random assets
* `search-smart`: Smart asset search

### `immich search get-assets-by-city`

Retrieve assets by city

<a href="https://api.immich.app/endpoints/search/getAssetsByCity">Immich API documentation</a>

**Usage**:

```console
$ immich search get-assets-by-city [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich search get-explore-data`

Retrieve explore data

<a href="https://api.immich.app/endpoints/search/getExploreData">Immich API documentation</a>

**Usage**:

```console
$ immich search get-explore-data [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich search get-search-suggestions`

Retrieve search suggestions

<a href="https://api.immich.app/endpoints/search/getSearchSuggestions">Immich API documentation</a>

**Usage**:

```console
$ immich search get-search-suggestions [OPTIONS]
```

**Options**:

* `--country TEXT`
* `--include-null [true|false]`
* `--lens-model TEXT`
* `--make TEXT`
* `--model TEXT`
* `--state TEXT`
* `--type [country|state|city|camera-make|camera-model|camera-lens-model]`: [required]
* `--help`: Show this message and exit.

### `immich search search-asset-statistics`

Search asset statistics

<a href="https://api.immich.app/endpoints/search/searchAssetStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich search search-asset-statistics [OPTIONS]
```

**Options**:

* `--album-ids TEXT`
* `--city TEXT`
* `--country TEXT`
* `--created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--description TEXT`
* `--device-id TEXT`
* `--is-encoded [true|false]`
* `--is-favorite [true|false]`
* `--is-motion [true|false]`
* `--is-not-in-album [true|false]`
* `--is-offline [true|false]`
* `--lens-model TEXT`
* `--library-id TEXT`
* `--make TEXT`
* `--model TEXT`
* `--ocr TEXT`
* `--person-ids TEXT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--state TEXT`
* `--tag-ids TEXT`
* `--taken-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--taken-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type TEXT`
* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--updated-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--visibility TEXT`
* `--help`: Show this message and exit.

### `immich search search-assets`

Search assets by metadata

<a href="https://api.immich.app/endpoints/search/searchAssets">Immich API documentation</a>

**Usage**:

```console
$ immich search search-assets [OPTIONS]
```

**Options**:

* `--album-ids TEXT`
* `--checksum TEXT`
* `--city TEXT`
* `--country TEXT`
* `--created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--description TEXT`
* `--device-asset-id TEXT`
* `--device-id TEXT`
* `--encoded-video-path TEXT`
* `--id TEXT`
* `--is-encoded [true|false]`
* `--is-favorite [true|false]`
* `--is-motion [true|false]`
* `--is-not-in-album [true|false]`
* `--is-offline [true|false]`
* `--lens-model TEXT`
* `--library-id TEXT`
* `--make TEXT`
* `--model TEXT`
* `--ocr TEXT`
* `--order TEXT`
* `--original-file-name TEXT`
* `--original-path TEXT`
* `--page FLOAT RANGE`: [x&gt;=1]
* `--person-ids TEXT`
* `--preview-path TEXT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--size FLOAT RANGE`: [1&lt;=x&lt;=1000]
* `--state TEXT`
* `--tag-ids TEXT`
* `--taken-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--taken-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--thumbnail-path TEXT`
* `--trashed-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type TEXT`
* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--updated-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--visibility TEXT`
* `--with-deleted [true|false]`
* `--with-exif [true|false]`
* `--with-people [true|false]`
* `--with-stacked [true|false]`
* `--help`: Show this message and exit.

### `immich search search-large-assets`

Search large assets

<a href="https://api.immich.app/endpoints/search/searchLargeAssets">Immich API documentation</a>

**Usage**:

```console
$ immich search search-large-assets [OPTIONS]
```

**Options**:

* `--album-ids TEXT`
* `--city TEXT`
* `--country TEXT`
* `--created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--device-id TEXT`
* `--is-encoded [true|false]`
* `--is-favorite [true|false]`
* `--is-motion [true|false]`
* `--is-not-in-album [true|false]`
* `--is-offline [true|false]`
* `--lens-model TEXT`
* `--library-id TEXT`
* `--make TEXT`
* `--min-file-size INTEGER RANGE`: [x&gt;=0]
* `--model TEXT`
* `--ocr TEXT`
* `--person-ids TEXT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--size FLOAT RANGE`: [1&lt;=x&lt;=1000]
* `--state TEXT`
* `--tag-ids TEXT`
* `--taken-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--taken-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type [IMAGE|VIDEO|AUDIO|OTHER]`
* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--updated-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--visibility [archive|timeline|hidden|locked]`
* `--with-deleted [true|false]`
* `--with-exif [true|false]`
* `--help`: Show this message and exit.

### `immich search search-person`

Search people

<a href="https://api.immich.app/endpoints/search/searchPerson">Immich API documentation</a>

**Usage**:

```console
$ immich search search-person [OPTIONS]
```

**Options**:

* `--name TEXT`: [required]
* `--with-hidden [true|false]`
* `--help`: Show this message and exit.

### `immich search search-places`

Search places

<a href="https://api.immich.app/endpoints/search/searchPlaces">Immich API documentation</a>

**Usage**:

```console
$ immich search search-places [OPTIONS]
```

**Options**:

* `--name TEXT`: [required]
* `--help`: Show this message and exit.

### `immich search search-random`

Search random assets

<a href="https://api.immich.app/endpoints/search/searchRandom">Immich API documentation</a>

**Usage**:

```console
$ immich search search-random [OPTIONS]
```

**Options**:

* `--album-ids TEXT`
* `--city TEXT`
* `--country TEXT`
* `--created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--device-id TEXT`
* `--is-encoded [true|false]`
* `--is-favorite [true|false]`
* `--is-motion [true|false]`
* `--is-not-in-album [true|false]`
* `--is-offline [true|false]`
* `--lens-model TEXT`
* `--library-id TEXT`
* `--make TEXT`
* `--model TEXT`
* `--ocr TEXT`
* `--person-ids TEXT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--size FLOAT RANGE`: [1&lt;=x&lt;=1000]
* `--state TEXT`
* `--tag-ids TEXT`
* `--taken-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--taken-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type TEXT`
* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--updated-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--visibility TEXT`
* `--with-deleted [true|false]`
* `--with-exif [true|false]`
* `--with-people [true|false]`
* `--with-stacked [true|false]`
* `--help`: Show this message and exit.

### `immich search search-smart`

Smart asset search

<a href="https://api.immich.app/endpoints/search/searchSmart">Immich API documentation</a>

**Usage**:

```console
$ immich search search-smart [OPTIONS]
```

**Options**:

* `--album-ids TEXT`
* `--city TEXT`
* `--country TEXT`
* `--created-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--created-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--device-id TEXT`
* `--is-encoded [true|false]`
* `--is-favorite [true|false]`
* `--is-motion [true|false]`
* `--is-not-in-album [true|false]`
* `--is-offline [true|false]`
* `--language TEXT`
* `--lens-model TEXT`
* `--library-id TEXT`
* `--make TEXT`
* `--model TEXT`
* `--ocr TEXT`
* `--page FLOAT RANGE`: [x&gt;=1]
* `--person-ids TEXT`
* `--query TEXT`
* `--query-asset-id TEXT`
* `--rating FLOAT RANGE`: [-1&lt;=x&lt;=5]
* `--size FLOAT RANGE`: [1&lt;=x&lt;=1000]
* `--state TEXT`
* `--tag-ids TEXT`
* `--taken-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--taken-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--trashed-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--type TEXT`
* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--updated-before [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--visibility TEXT`
* `--with-deleted [true|false]`
* `--with-exif [true|false]`
* `--help`: Show this message and exit.

## `immich server`

Information about the current server deployment, including version and build information, available features, supported media types, and more.

<a href="https://api.immich.app/endpoints/server">Immich API documentation</a>

**Usage**:

```console
$ immich server [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `delete-server-license`: Delete server product key
* `get-about-info`: Get server information
* `get-apk-links`: Get APK links
* `get-server-config`: Get config
* `get-server-features`: Get features
* `get-server-license`: Get product key
* `get-server-statistics`: Get statistics
* `get-server-version`: Get server version
* `get-storage`: Get storage
* `get-supported-media-types`: Get supported media types
* `get-theme`: Get theme
* `get-version-check`: Get version check status
* `get-version-history`: Get version history
* `ping-server`: Ping
* `set-server-license`: Set server product key

### `immich server delete-server-license`

Delete server product key

<a href="https://api.immich.app/endpoints/server/deleteServerLicense">Immich API documentation</a>

**Usage**:

```console
$ immich server delete-server-license [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-about-info`

Get server information

<a href="https://api.immich.app/endpoints/server/getAboutInfo">Immich API documentation</a>

**Usage**:

```console
$ immich server get-about-info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-apk-links`

Get APK links

<a href="https://api.immich.app/endpoints/server/getApkLinks">Immich API documentation</a>

**Usage**:

```console
$ immich server get-apk-links [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-server-config`

Get config

<a href="https://api.immich.app/endpoints/server/getServerConfig">Immich API documentation</a>

**Usage**:

```console
$ immich server get-server-config [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-server-features`

Get features

<a href="https://api.immich.app/endpoints/server/getServerFeatures">Immich API documentation</a>

**Usage**:

```console
$ immich server get-server-features [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-server-license`

Get product key

<a href="https://api.immich.app/endpoints/server/getServerLicense">Immich API documentation</a>

**Usage**:

```console
$ immich server get-server-license [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-server-statistics`

Get statistics

<a href="https://api.immich.app/endpoints/server/getServerStatistics">Immich API documentation</a>

**Usage**:

```console
$ immich server get-server-statistics [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-server-version`

Get server version

<a href="https://api.immich.app/endpoints/server/getServerVersion">Immich API documentation</a>

**Usage**:

```console
$ immich server get-server-version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-storage`

Get storage

<a href="https://api.immich.app/endpoints/server/getStorage">Immich API documentation</a>

**Usage**:

```console
$ immich server get-storage [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-supported-media-types`

Get supported media types

<a href="https://api.immich.app/endpoints/server/getSupportedMediaTypes">Immich API documentation</a>

**Usage**:

```console
$ immich server get-supported-media-types [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-theme`

Get theme

<a href="https://api.immich.app/endpoints/server/getTheme">Immich API documentation</a>

**Usage**:

```console
$ immich server get-theme [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-version-check`

Get version check status

<a href="https://api.immich.app/endpoints/server/getVersionCheck">Immich API documentation</a>

**Usage**:

```console
$ immich server get-version-check [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server get-version-history`

Get version history

<a href="https://api.immich.app/endpoints/server/getVersionHistory">Immich API documentation</a>

**Usage**:

```console
$ immich server get-version-history [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server ping-server`

Ping

<a href="https://api.immich.app/endpoints/server/pingServer">Immich API documentation</a>

**Usage**:

```console
$ immich server ping-server [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich server set-server-license`

Set server product key

<a href="https://api.immich.app/endpoints/server/setServerLicense">Immich API documentation</a>

**Usage**:

```console
$ immich server set-server-license [OPTIONS]
```

**Options**:

* `--activation-key TEXT`: [required]
* `--license-key TEXT`: [required]
* `--help`: Show this message and exit.

## `immich sessions`

A session represents an authenticated login session for a user. Sessions also appear in the web application as &quot;Authorized devices&quot;.

<a href="https://api.immich.app/endpoints/sessions">Immich API documentation</a>

**Usage**:

```console
$ immich sessions [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-session`: Create a session
* `delete-all-sessions`: Delete all sessions
* `delete-session`: Delete a session
* `get-sessions`: Retrieve sessions
* `lock-session`: Lock a session
* `update-session`: Update a session

### `immich sessions create-session`

Create a session

<a href="https://api.immich.app/endpoints/sessions/createSession">Immich API documentation</a>

**Usage**:

```console
$ immich sessions create-session [OPTIONS]
```

**Options**:

* `--device-os TEXT`
* `--device-type TEXT`
* `--duration FLOAT RANGE`: session duration, in seconds  [x&gt;=1]
* `--help`: Show this message and exit.

### `immich sessions delete-all-sessions`

Delete all sessions

<a href="https://api.immich.app/endpoints/sessions/deleteAllSessions">Immich API documentation</a>

**Usage**:

```console
$ immich sessions delete-all-sessions [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich sessions delete-session`

Delete a session

<a href="https://api.immich.app/endpoints/sessions/deleteSession">Immich API documentation</a>

**Usage**:

```console
$ immich sessions delete-session [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich sessions get-sessions`

Retrieve sessions

<a href="https://api.immich.app/endpoints/sessions/getSessions">Immich API documentation</a>

**Usage**:

```console
$ immich sessions get-sessions [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich sessions lock-session`

Lock a session

<a href="https://api.immich.app/endpoints/sessions/lockSession">Immich API documentation</a>

**Usage**:

```console
$ immich sessions lock-session [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich sessions update-session`

Update a session

<a href="https://api.immich.app/endpoints/sessions/updateSession">Immich API documentation</a>

**Usage**:

```console
$ immich sessions update-session [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--is-pending-sync-reset [true|false]`
* `--help`: Show this message and exit.

## `immich shared-links`

A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.

<a href="https://api.immich.app/endpoints/shared-links">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add-shared-link-assets`: Add assets to a shared link
* `create-shared-link`: Create a shared link
* `get-all-shared-links`: Retrieve all shared links
* `get-my-shared-link`: Retrieve current shared link
* `get-shared-link-by-id`: Retrieve a shared link
* `remove-shared-link`: Delete a shared link
* `remove-shared-link-assets`: Remove assets from a shared link
* `update-shared-link`: Update a shared link

### `immich shared-links add-shared-link-assets`

Add assets to a shared link

<a href="https://api.immich.app/endpoints/shared-links/addSharedLinkAssets">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links add-shared-link-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--asset-ids TEXT`: [required]
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich shared-links create-shared-link`

Create a shared link

<a href="https://api.immich.app/endpoints/shared-links/createSharedLink">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links create-shared-link [OPTIONS]
```

**Options**:

* `--album-id TEXT`
* `--allow-download [true|false]`
* `--allow-upload [true|false]`
* `--asset-ids TEXT`
* `--description TEXT`
* `--expires-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--password TEXT`
* `--show-metadata [true|false]`
* `--slug TEXT`
* `--type TEXT`: [required]
* `--help`: Show this message and exit.

### `immich shared-links get-all-shared-links`

Retrieve all shared links

<a href="https://api.immich.app/endpoints/shared-links/getAllSharedLinks">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links get-all-shared-links [OPTIONS]
```

**Options**:

* `--album-id TEXT`
* `--help`: Show this message and exit.

### `immich shared-links get-my-shared-link`

Retrieve current shared link

<a href="https://api.immich.app/endpoints/shared-links/getMySharedLink">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links get-my-shared-link [OPTIONS]
```

**Options**:

* `--key TEXT`
* `--password TEXT`: password
* `--slug TEXT`
* `--token TEXT`
* `--help`: Show this message and exit.

### `immich shared-links get-shared-link-by-id`

Retrieve a shared link

<a href="https://api.immich.app/endpoints/shared-links/getSharedLinkById">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links get-shared-link-by-id [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich shared-links remove-shared-link`

Delete a shared link

<a href="https://api.immich.app/endpoints/shared-links/removeSharedLink">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links remove-shared-link [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich shared-links remove-shared-link-assets`

Remove assets from a shared link

<a href="https://api.immich.app/endpoints/shared-links/removeSharedLinkAssets">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links remove-shared-link-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--asset-ids TEXT`: [required]
* `--key TEXT`
* `--slug TEXT`
* `--help`: Show this message and exit.

### `immich shared-links update-shared-link`

Update a shared link

<a href="https://api.immich.app/endpoints/shared-links/updateSharedLink">Immich API documentation</a>

**Usage**:

```console
$ immich shared-links update-shared-link [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--allow-download [true|false]`
* `--allow-upload [true|false]`
* `--change-expiry-time [true|false]`: Few clients cannot send null to set the expiryTime to never.
Setting this flag and not sending expiryAt is considered as null instead.
Clients that can send null values can ignore this.
* `--description TEXT`
* `--expires-at [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`
* `--password TEXT`
* `--show-metadata [true|false]`
* `--slug TEXT`
* `--help`: Show this message and exit.

## `immich stacks`

A stack is a group of related assets. One asset is the &quot;primary&quot; asset, and the rest are &quot;child&quot; assets. On the main timeline, stack parents are included by default, while child assets are hidden.

<a href="https://api.immich.app/endpoints/stacks">Immich API documentation</a>

**Usage**:

```console
$ immich stacks [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-stack`: Create a stack
* `delete-stack`: Delete a stack
* `delete-stacks`: Delete stacks
* `get-stack`: Retrieve a stack
* `remove-asset-from-stack`: Remove an asset from a stack
* `search-stacks`: Retrieve stacks
* `update-stack`: Update a stack

### `immich stacks create-stack`

Create a stack

<a href="https://api.immich.app/endpoints/stacks/createStack">Immich API documentation</a>

**Usage**:

```console
$ immich stacks create-stack [OPTIONS]
```

**Options**:

* `--asset-ids TEXT`: first asset becomes the primary  [required]
* `--help`: Show this message and exit.

### `immich stacks delete-stack`

Delete a stack

<a href="https://api.immich.app/endpoints/stacks/deleteStack">Immich API documentation</a>

**Usage**:

```console
$ immich stacks delete-stack [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich stacks delete-stacks`

Delete stacks

<a href="https://api.immich.app/endpoints/stacks/deleteStacks">Immich API documentation</a>

**Usage**:

```console
$ immich stacks delete-stacks [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich stacks get-stack`

Retrieve a stack

<a href="https://api.immich.app/endpoints/stacks/getStack">Immich API documentation</a>

**Usage**:

```console
$ immich stacks get-stack [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich stacks remove-asset-from-stack`

Remove an asset from a stack

<a href="https://api.immich.app/endpoints/stacks/removeAssetFromStack">Immich API documentation</a>

**Usage**:

```console
$ immich stacks remove-asset-from-stack [OPTIONS] ASSET_ID ID
```

**Arguments**:

* `ASSET_ID`: [required]
* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich stacks search-stacks`

Retrieve stacks

<a href="https://api.immich.app/endpoints/stacks/searchStacks">Immich API documentation</a>

**Usage**:

```console
$ immich stacks search-stacks [OPTIONS]
```

**Options**:

* `--primary-asset-id TEXT`
* `--help`: Show this message and exit.

### `immich stacks update-stack`

Update a stack

<a href="https://api.immich.app/endpoints/stacks/updateStack">Immich API documentation</a>

**Usage**:

```console
$ immich stacks update-stack [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--primary-asset-id TEXT`
* `--help`: Show this message and exit.

## `immich sync`

A collection of endpoints for the new mobile synchronization implementation.

<a href="https://api.immich.app/endpoints/sync">Immich API documentation</a>

**Usage**:

```console
$ immich sync [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `delete-sync-ack`: Delete acknowledgements
* `get-delta-sync`: Get delta sync for user (DEPRECATED)
* `get-full-sync-for-user`: Get full sync for user (DEPRECATED)
* `get-sync-ack`: Retrieve acknowledgements
* `get-sync-stream`: Stream sync changes
* `send-sync-ack`: Acknowledge changes

### `immich sync delete-sync-ack`

Delete acknowledgements

<a href="https://api.immich.app/endpoints/sync/deleteSyncAck">Immich API documentation</a>

**Usage**:

```console
$ immich sync delete-sync-ack [OPTIONS]
```

**Options**:

* `--types [AuthUserV1|UserV1|UserDeleteV1|AssetV1|AssetDeleteV1|AssetExifV1|AssetMetadataV1|AssetMetadataDeleteV1|PartnerV1|PartnerDeleteV1|PartnerAssetV1|PartnerAssetBackfillV1|PartnerAssetDeleteV1|PartnerAssetExifV1|PartnerAssetExifBackfillV1|PartnerStackBackfillV1|PartnerStackDeleteV1|PartnerStackV1|AlbumV1|AlbumDeleteV1|AlbumUserV1|AlbumUserBackfillV1|AlbumUserDeleteV1|AlbumAssetCreateV1|AlbumAssetUpdateV1|AlbumAssetBackfillV1|AlbumAssetExifCreateV1|AlbumAssetExifUpdateV1|AlbumAssetExifBackfillV1|AlbumToAssetV1|AlbumToAssetDeleteV1|AlbumToAssetBackfillV1|MemoryV1|MemoryDeleteV1|MemoryToAssetV1|MemoryToAssetDeleteV1|StackV1|StackDeleteV1|PersonV1|PersonDeleteV1|AssetFaceV1|AssetFaceDeleteV1|UserMetadataV1|UserMetadataDeleteV1|SyncAckV1|SyncResetV1|SyncCompleteV1]`
* `--help`: Show this message and exit.

### `immich sync get-delta-sync`

Get delta sync for user

<a href="https://api.immich.app/endpoints/sync/getDeltaSync">Immich API documentation</a>

**Usage**:

```console
$ immich sync get-delta-sync [OPTIONS]
```

**Options**:

* `--updated-after [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--user-ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich sync get-full-sync-for-user`

Get full sync for user

<a href="https://api.immich.app/endpoints/sync/getFullSyncForUser">Immich API documentation</a>

**Usage**:

```console
$ immich sync get-full-sync-for-user [OPTIONS]
```

**Options**:

* `--last-id TEXT`
* `--limit INTEGER RANGE`: [x&gt;=1; required]
* `--updated-until [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: [required]
* `--user-id TEXT`
* `--help`: Show this message and exit.

### `immich sync get-sync-ack`

Retrieve acknowledgements

<a href="https://api.immich.app/endpoints/sync/getSyncAck">Immich API documentation</a>

**Usage**:

```console
$ immich sync get-sync-ack [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich sync get-sync-stream`

Stream sync changes

<a href="https://api.immich.app/endpoints/sync/getSyncStream">Immich API documentation</a>

**Usage**:

```console
$ immich sync get-sync-stream [OPTIONS]
```

**Options**:

* `--reset [true|false]`
* `--types [AlbumsV1|AlbumUsersV1|AlbumToAssetsV1|AlbumAssetsV1|AlbumAssetExifsV1|AssetsV1|AssetExifsV1|AssetMetadataV1|AuthUsersV1|MemoriesV1|MemoryToAssetsV1|PartnersV1|PartnerAssetsV1|PartnerAssetExifsV1|PartnerStacksV1|StacksV1|UsersV1|PeopleV1|AssetFacesV1|UserMetadataV1]`: [required]
* `--help`: Show this message and exit.

### `immich sync send-sync-ack`

Acknowledge changes

<a href="https://api.immich.app/endpoints/sync/sendSyncAck">Immich API documentation</a>

**Usage**:

```console
$ immich sync send-sync-ack [OPTIONS]
```

**Options**:

* `--acks TEXT`: [required]
* `--help`: Show this message and exit.

## `immich system-config`

Endpoints to view, modify, and validate the system configuration settings.

<a href="https://api.immich.app/endpoints/system-config">Immich API documentation</a>

**Usage**:

```console
$ immich system-config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-config`: Get system configuration
* `get-config-defaults`: Get system configuration defaults
* `get-storage-template-options`: Get storage template options
* `update-config`: Update system configuration

### `immich system-config get-config`

Get system configuration

<a href="https://api.immich.app/endpoints/system-config/getConfig">Immich API documentation</a>

**Usage**:

```console
$ immich system-config get-config [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-config get-config-defaults`

Get system configuration defaults

<a href="https://api.immich.app/endpoints/system-config/getConfigDefaults">Immich API documentation</a>

**Usage**:

```console
$ immich system-config get-config-defaults [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-config get-storage-template-options`

Get storage template options

<a href="https://api.immich.app/endpoints/system-config/getStorageTemplateOptions">Immich API documentation</a>

**Usage**:

```console
$ immich system-config get-storage-template-options [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-config update-config`

Update system configuration

<a href="https://api.immich.app/endpoints/system-config/updateConfig">Immich API documentation</a>

**Usage**:

```console
$ immich system-config update-config [OPTIONS]
```

**Options**:

* `--backup-database-cron-expression TEXT`: [required]
* `--backup-database-enabled`: [required]
* `--backup-database-keep-last-amount FLOAT RANGE`: [x&gt;=1; required]
* `--ffmpeg-accel TEXT`: [required]
* `--ffmpeg-accel-decode`: [required]
* `--ffmpeg-accepted-audio-codecs [mp3|aac|libopus|pcm_s16le]`: [required]
* `--ffmpeg-accepted-containers [mov|mp4|ogg|webm]`: [required]
* `--ffmpeg-accepted-video-codecs [h264|hevc|vp9|av1]`: [required]
* `--ffmpeg-bframes INTEGER RANGE`: [-1&lt;=x&lt;=16; required]
* `--ffmpeg-cq-mode TEXT`: [required]
* `--ffmpeg-crf INTEGER RANGE`: [0&lt;=x&lt;=51; required]
* `--ffmpeg-gop-size INTEGER RANGE`: [x&gt;=0; required]
* `--ffmpeg-max-bitrate TEXT`: [required]
* `--ffmpeg-preferred-hw-device TEXT`: [required]
* `--ffmpeg-preset TEXT`: [required]
* `--ffmpeg-refs INTEGER RANGE`: [0&lt;=x&lt;=6; required]
* `--ffmpeg-target-audio-codec TEXT`: [required]
* `--ffmpeg-target-resolution TEXT`: [required]
* `--ffmpeg-target-video-codec TEXT`: [required]
* `--ffmpeg-temporal-aq`: [required]
* `--ffmpeg-threads INTEGER RANGE`: [x&gt;=0; required]
* `--ffmpeg-tonemap TEXT`: [required]
* `--ffmpeg-transcode TEXT`: [required]
* `--ffmpeg-two-pass`: [required]
* `--image-colorspace TEXT`: [required]
* `--image-extract-embedded`: [required]
* `--image-fullsize-enabled`: [required]
* `--image-fullsize-format TEXT`: [required]
* `--image-fullsize-quality INTEGER RANGE`: [1&lt;=x&lt;=100; required]
* `--image-preview-format TEXT`: [required]
* `--image-preview-quality INTEGER RANGE`: [1&lt;=x&lt;=100; required]
* `--image-preview-size INTEGER RANGE`: [x&gt;=1; required]
* `--image-thumbnail-format TEXT`: [required]
* `--image-thumbnail-quality INTEGER RANGE`: [1&lt;=x&lt;=100; required]
* `--image-thumbnail-size INTEGER RANGE`: [x&gt;=1; required]
* `--job-background-task-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-face-detection-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-library-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-metadata-extraction-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-migration-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-notifications-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-ocr-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-search-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-sidecar-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-smart-search-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-thumbnail-generation-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-video-conversion-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--job-workflow-concurrency INTEGER RANGE`: [x&gt;=1; required]
* `--library-scan-cron-expression TEXT`: [required]
* `--library-scan-enabled`: [required]
* `--library-watch-enabled`: [required]
* `--logging-enabled`: [required]
* `--logging-level TEXT`: [required]
* `--machine-learning-availability-checks-enabled`: [required]
* `--machine-learning-availability-checks-interval FLOAT`: [required]
* `--machine-learning-availability-checks-timeout FLOAT`: [required]
* `--machine-learning-clip-enabled`: [required]
* `--machine-learning-clip-model-name TEXT`: [required]
* `--machine-learning-duplicate-detection-enabled`: [required]
* `--machine-learning-duplicate-detection-max-distance FLOAT RANGE`: [0.001&lt;=x&lt;=0.1; required]
* `--machine-learning-enabled`: [required]
* `--machine-learning-facial-recognition-enabled`: [required]
* `--machine-learning-facial-recognition-max-distance FLOAT RANGE`: [0.1&lt;=x&lt;=2; required]
* `--machine-learning-facial-recognition-min-faces INTEGER RANGE`: [x&gt;=1; required]
* `--machine-learning-facial-recognition-min-score FLOAT RANGE`: [0.1&lt;=x&lt;=1; required]
* `--machine-learning-facial-recognition-model-name TEXT`: [required]
* `--machine-learning-ocr-enabled`: [required]
* `--machine-learning-ocr-max-resolution INTEGER RANGE`: [x&gt;=1; required]
* `--machine-learning-ocr-min-detection-score FLOAT RANGE`: [0.1&lt;=x&lt;=1; required]
* `--machine-learning-ocr-min-recognition-score FLOAT RANGE`: [0.1&lt;=x&lt;=1; required]
* `--machine-learning-ocr-model-name TEXT`: [required]
* `--machine-learning-urls TEXT`: [required]
* `--map-dark-style TEXT`: [required]
* `--map-enabled`: [required]
* `--map-light-style TEXT`: [required]
* `--metadata-faces-import`: [required]
* `--new-version-check-enabled`: [required]
* `--nightly-tasks-cluster-new-faces`: [required]
* `--nightly-tasks-database-cleanup`: [required]
* `--nightly-tasks-generate-memories`: [required]
* `--nightly-tasks-missing-thumbnails`: [required]
* `--nightly-tasks-start-time TEXT`: [required]
* `--nightly-tasks-sync-quota-usage`: [required]
* `--notifications-smtp-enabled`: [required]
* `--notifications-smtp-from TEXT`: [required]
* `--notifications-smtp-reply-to TEXT`: [required]
* `--notifications-smtp-transport-host TEXT`: [required]
* `--notifications-smtp-transport-ignore-cert`: [required]
* `--notifications-smtp-transport-password TEXT`: [required]
* `--notifications-smtp-transport-port FLOAT RANGE`: [0&lt;=x&lt;=65535; required]
* `--notifications-smtp-transport-secure`: [required]
* `--notifications-smtp-transport-username TEXT`: [required]
* `--oauth-auto-launch`: [required]
* `--oauth-auto-register`: [required]
* `--oauth-button-text TEXT`: [required]
* `--oauth-client-id TEXT`: [required]
* `--oauth-client-secret TEXT`: [required]
* `--oauth-default-storage-quota INTEGER RANGE`: [x&gt;=0; required]
* `--oauth-enabled`: [required]
* `--oauth-issuer-url TEXT`: [required]
* `--oauth-mobile-override-enabled`: [required]
* `--oauth-mobile-redirect-uri TEXT`: [required]
* `--oauth-profile-signing-algorithm TEXT`: [required]
* `--oauth-role-claim TEXT`: [required]
* `--oauth-scope TEXT`: [required]
* `--oauth-signing-algorithm TEXT`: [required]
* `--oauth-storage-label-claim TEXT`: [required]
* `--oauth-storage-quota-claim TEXT`: [required]
* `--oauth-timeout INTEGER RANGE`: [x&gt;=1; required]
* `--oauth-token-endpoint-auth-method TEXT`: [required]
* `--password-login-enabled`: [required]
* `--reverse-geocoding-enabled`: [required]
* `--server-external-domain TEXT`: [required]
* `--server-login-page-message TEXT`: [required]
* `--server-public-users`: [required]
* `--storage-template-enabled`: [required]
* `--storage-template-hash-verification-enabled`: [required]
* `--storage-template-template TEXT`: [required]
* `--templates-email-album-invite-template TEXT`: [required]
* `--templates-email-album-update-template TEXT`: [required]
* `--templates-email-welcome-template TEXT`: [required]
* `--theme-custom-css TEXT`: [required]
* `--trash-days INTEGER RANGE`: [x&gt;=0; required]
* `--trash-enabled`: [required]
* `--user-delete-delay INTEGER RANGE`: [x&gt;=1; required]
* `--help`: Show this message and exit.

## `immich system-metadata`

Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.

<a href="https://api.immich.app/endpoints/system-metadata">Immich API documentation</a>

**Usage**:

```console
$ immich system-metadata [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-admin-onboarding`: Retrieve admin onboarding
* `get-reverse-geocoding-state`: Retrieve reverse geocoding state
* `get-version-check-state`: Retrieve version check state
* `update-admin-onboarding`: Update admin onboarding

### `immich system-metadata get-admin-onboarding`

Retrieve admin onboarding

<a href="https://api.immich.app/endpoints/system-metadata/getAdminOnboarding">Immich API documentation</a>

**Usage**:

```console
$ immich system-metadata get-admin-onboarding [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-metadata get-reverse-geocoding-state`

Retrieve reverse geocoding state

<a href="https://api.immich.app/endpoints/system-metadata/getReverseGeocodingState">Immich API documentation</a>

**Usage**:

```console
$ immich system-metadata get-reverse-geocoding-state [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-metadata get-version-check-state`

Retrieve version check state

<a href="https://api.immich.app/endpoints/system-metadata/getVersionCheckState">Immich API documentation</a>

**Usage**:

```console
$ immich system-metadata get-version-check-state [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich system-metadata update-admin-onboarding`

Update admin onboarding

<a href="https://api.immich.app/endpoints/system-metadata/updateAdminOnboarding">Immich API documentation</a>

**Usage**:

```console
$ immich system-metadata update-admin-onboarding [OPTIONS]
```

**Options**:

* `--is-onboarded`: [required]
* `--help`: Show this message and exit.

## `immich tags`

A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.

<a href="https://api.immich.app/endpoints/tags">Immich API documentation</a>

**Usage**:

```console
$ immich tags [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `bulk-tag-assets`: Tag assets
* `create-tag`: Create a tag
* `delete-tag`: Delete a tag
* `get-all-tags`: Retrieve tags
* `get-tag-by-id`: Retrieve a tag
* `tag-assets`: Tag assets
* `untag-assets`: Untag assets
* `update-tag`: Update a tag
* `upsert-tags`: Upsert tags

### `immich tags bulk-tag-assets`

Tag assets

<a href="https://api.immich.app/endpoints/tags/bulkTagAssets">Immich API documentation</a>

**Usage**:

```console
$ immich tags bulk-tag-assets [OPTIONS]
```

**Options**:

* `--asset-ids TEXT`: [required]
* `--tag-ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich tags create-tag`

Create a tag

<a href="https://api.immich.app/endpoints/tags/createTag">Immich API documentation</a>

**Usage**:

```console
$ immich tags create-tag [OPTIONS]
```

**Options**:

* `--color TEXT`
* `--name TEXT`: [required]
* `--parent-id TEXT`
* `--help`: Show this message and exit.

### `immich tags delete-tag`

Delete a tag

<a href="https://api.immich.app/endpoints/tags/deleteTag">Immich API documentation</a>

**Usage**:

```console
$ immich tags delete-tag [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich tags get-all-tags`

Retrieve tags

<a href="https://api.immich.app/endpoints/tags/getAllTags">Immich API documentation</a>

**Usage**:

```console
$ immich tags get-all-tags [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich tags get-tag-by-id`

Retrieve a tag

<a href="https://api.immich.app/endpoints/tags/getTagById">Immich API documentation</a>

**Usage**:

```console
$ immich tags get-tag-by-id [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich tags tag-assets`

Tag assets

<a href="https://api.immich.app/endpoints/tags/tagAssets">Immich API documentation</a>

**Usage**:

```console
$ immich tags tag-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich tags untag-assets`

Untag assets

<a href="https://api.immich.app/endpoints/tags/untagAssets">Immich API documentation</a>

**Usage**:

```console
$ immich tags untag-assets [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich tags update-tag`

Update a tag

<a href="https://api.immich.app/endpoints/tags/updateTag">Immich API documentation</a>

**Usage**:

```console
$ immich tags update-tag [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--color TEXT`
* `--help`: Show this message and exit.

### `immich tags upsert-tags`

Upsert tags

<a href="https://api.immich.app/endpoints/tags/upsertTags">Immich API documentation</a>

**Usage**:

```console
$ immich tags upsert-tags [OPTIONS]
```

**Options**:

* `--tags TEXT`: [required]
* `--help`: Show this message and exit.

## `immich timeline`

Specialized endpoints related to the timeline implementation used in the web application. External applications or tools should not use or rely on these endpoints, as they are subject to change without notice.

<a href="https://api.immich.app/endpoints/timeline">Immich API documentation</a>

**Usage**:

```console
$ immich timeline [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-time-bucket`: Get time bucket
* `get-time-buckets`: Get time buckets

### `immich timeline get-time-bucket`

Get time bucket

<a href="https://api.immich.app/endpoints/timeline/getTimeBucket">Immich API documentation</a>

**Usage**:

```console
$ immich timeline get-time-bucket [OPTIONS]
```

**Options**:

* `--album-id TEXT`: Filter assets belonging to a specific album
* `--is-favorite [true|false]`: Filter by favorite status (true for favorites only, false for non-favorites only)
* `--is-trashed [true|false]`: Filter by trash status (true for trashed assets only, false for non-trashed only)
* `--key TEXT`
* `--order [asc|desc]`: Sort order for assets within time buckets (ASC for oldest first, DESC for newest first)
* `--person-id TEXT`: Filter assets containing a specific person (face recognition)
* `--slug TEXT`
* `--tag-id TEXT`: Filter assets with a specific tag
* `--time-bucket TEXT`: Time bucket identifier in YYYY-MM-DD format (e.g., &quot;2024-01-01&quot; for January 2024)2024-01-01  [required]
* `--user-id TEXT`: Filter assets by specific user ID
* `--visibility [archive|timeline|hidden|locked]`: Filter by asset visibility status (ARCHIVE, TIMELINE, HIDDEN, LOCKED)
* `--with-coordinates [true|false]`: Include location data in the response
* `--with-partners [true|false]`: Include assets shared by partners
* `--with-stacked [true|false]`: Include stacked assets in the response. When true, only primary assets from stacks are returned.
* `--help`: Show this message and exit.

### `immich timeline get-time-buckets`

Get time buckets

<a href="https://api.immich.app/endpoints/timeline/getTimeBuckets">Immich API documentation</a>

**Usage**:

```console
$ immich timeline get-time-buckets [OPTIONS]
```

**Options**:

* `--album-id TEXT`: Filter assets belonging to a specific album
* `--is-favorite [true|false]`: Filter by favorite status (true for favorites only, false for non-favorites only)
* `--is-trashed [true|false]`: Filter by trash status (true for trashed assets only, false for non-trashed only)
* `--key TEXT`
* `--order [asc|desc]`: Sort order for assets within time buckets (ASC for oldest first, DESC for newest first)
* `--person-id TEXT`: Filter assets containing a specific person (face recognition)
* `--slug TEXT`
* `--tag-id TEXT`: Filter assets with a specific tag
* `--user-id TEXT`: Filter assets by specific user ID
* `--visibility [archive|timeline|hidden|locked]`: Filter by asset visibility status (ARCHIVE, TIMELINE, HIDDEN, LOCKED)
* `--with-coordinates [true|false]`: Include location data in the response
* `--with-partners [true|false]`: Include assets shared by partners
* `--with-stacked [true|false]`: Include stacked assets in the response. When true, only primary assets from stacks are returned.
* `--help`: Show this message and exit.

## `immich trash`

Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.

<a href="https://api.immich.app/endpoints/trash">Immich API documentation</a>

**Usage**:

```console
$ immich trash [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `empty-trash`: Empty trash
* `restore-assets`: Restore assets
* `restore-trash`: Restore trash

### `immich trash empty-trash`

Empty trash

<a href="https://api.immich.app/endpoints/trash/emptyTrash">Immich API documentation</a>

**Usage**:

```console
$ immich trash empty-trash [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich trash restore-assets`

Restore assets

<a href="https://api.immich.app/endpoints/trash/restoreAssets">Immich API documentation</a>

**Usage**:

```console
$ immich trash restore-assets [OPTIONS]
```

**Options**:

* `--ids TEXT`: [required]
* `--help`: Show this message and exit.

### `immich trash restore-trash`

Restore trash

<a href="https://api.immich.app/endpoints/trash/restoreTrash">Immich API documentation</a>

**Usage**:

```console
$ immich trash restore-trash [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich users`

Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.

<a href="https://api.immich.app/endpoints/users">Immich API documentation</a>

**Usage**:

```console
$ immich users [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-profile-image`: Create user profile image
* `delete-profile-image`: Delete user profile image
* `delete-user-license`: Delete user product key
* `delete-user-onboarding`: Delete user onboarding
* `get-my-preferences`: Get my preferences
* `get-my-user`: Get current user
* `get-profile-image`: Retrieve user profile image
* `get-user`: Retrieve a user
* `get-user-license`: Retrieve user product key
* `get-user-onboarding`: Retrieve user onboarding
* `search-users`: Get all users
* `set-user-license`: Set user product key
* `set-user-onboarding`: Update user onboarding
* `update-my-preferences`: Update my preferences
* `update-my-user`: Update current user
* `get-profile-image-to-file`: Download a user&#x27;s profile image and save...

### `immich users create-profile-image`

Create user profile image

<a href="https://api.immich.app/endpoints/users/createProfileImage">Immich API documentation</a>

**Usage**:

```console
$ immich users create-profile-image [OPTIONS]
```

**Options**:

* `--file PATH`: [required]
* `--help`: Show this message and exit.

### `immich users delete-profile-image`

Delete user profile image

<a href="https://api.immich.app/endpoints/users/deleteProfileImage">Immich API documentation</a>

**Usage**:

```console
$ immich users delete-profile-image [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users delete-user-license`

Delete user product key

<a href="https://api.immich.app/endpoints/users/deleteUserLicense">Immich API documentation</a>

**Usage**:

```console
$ immich users delete-user-license [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users delete-user-onboarding`

Delete user onboarding

<a href="https://api.immich.app/endpoints/users/deleteUserOnboarding">Immich API documentation</a>

**Usage**:

```console
$ immich users delete-user-onboarding [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users get-my-preferences`

Get my preferences

<a href="https://api.immich.app/endpoints/users/getMyPreferences">Immich API documentation</a>

**Usage**:

```console
$ immich users get-my-preferences [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users get-my-user`

Get current user

<a href="https://api.immich.app/endpoints/users/getMyUser">Immich API documentation</a>

**Usage**:

```console
$ immich users get-my-user [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users get-profile-image`

Retrieve user profile image

<a href="https://api.immich.app/endpoints/users/getProfileImage">Immich API documentation</a>

**Usage**:

```console
$ immich users get-profile-image [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users get-user`

Retrieve a user

<a href="https://api.immich.app/endpoints/users/getUser">Immich API documentation</a>

**Usage**:

```console
$ immich users get-user [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users get-user-license`

Retrieve user product key

<a href="https://api.immich.app/endpoints/users/getUserLicense">Immich API documentation</a>

**Usage**:

```console
$ immich users get-user-license [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users get-user-onboarding`

Retrieve user onboarding

<a href="https://api.immich.app/endpoints/users/getUserOnboarding">Immich API documentation</a>

**Usage**:

```console
$ immich users get-user-onboarding [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users search-users`

Get all users

<a href="https://api.immich.app/endpoints/users/searchUsers">Immich API documentation</a>

**Usage**:

```console
$ immich users search-users [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich users set-user-license`

Set user product key

<a href="https://api.immich.app/endpoints/users/setUserLicense">Immich API documentation</a>

**Usage**:

```console
$ immich users set-user-license [OPTIONS]
```

**Options**:

* `--activation-key TEXT`: [required]
* `--license-key TEXT`: [required]
* `--help`: Show this message and exit.

### `immich users set-user-onboarding`

Update user onboarding

<a href="https://api.immich.app/endpoints/users/setUserOnboarding">Immich API documentation</a>

**Usage**:

```console
$ immich users set-user-onboarding [OPTIONS]
```

**Options**:

* `--is-onboarded`: [required]
* `--help`: Show this message and exit.

### `immich users update-my-preferences`

Update my preferences

<a href="https://api.immich.app/endpoints/users/updateMyPreferences">Immich API documentation</a>

**Usage**:

```console
$ immich users update-my-preferences [OPTIONS]
```

**Options**:

* `--albums-default-asset-order TEXT`
* `--avatar-color TEXT`
* `--cast-g-cast-enabled [true|false]`
* `--download-archive-size INTEGER RANGE`: [x&gt;=1]
* `--download-include-embedded-videos [true|false]`
* `--email-notifications-album-invite [true|false]`
* `--email-notifications-album-update [true|false]`
* `--email-notifications-enabled [true|false]`
* `--folders-enabled [true|false]`
* `--folders-sidebar-web [true|false]`
* `--memories-duration INTEGER RANGE`: [x&gt;=1]
* `--memories-enabled [true|false]`
* `--people-enabled [true|false]`
* `--people-sidebar-web [true|false]`
* `--purchase-hide-buy-button-until TEXT`
* `--purchase-show-support-badge [true|false]`
* `--ratings-enabled [true|false]`
* `--shared-links-enabled [true|false]`
* `--shared-links-sidebar-web [true|false]`
* `--tags-enabled [true|false]`
* `--tags-sidebar-web [true|false]`
* `--help`: Show this message and exit.

### `immich users update-my-user`

Update current user

<a href="https://api.immich.app/endpoints/users/updateMyUser">Immich API documentation</a>

**Usage**:

```console
$ immich users update-my-user [OPTIONS]
```

**Options**:

* `--avatar-color TEXT`
* `--email TEXT`
* `--name TEXT`
* `--password TEXT`
* `--help`: Show this message and exit.

### `immich users get-profile-image-to-file`

Download a user&#x27;s profile image and save it to a file.

Downloads the profile image for the specified user and saves it to the specified output directory.
The filename can be specified or will be derived from the response headers.

**Usage**:

```console
$ immich users get-profile-image-to-file [OPTIONS] ID OUT_DIR
```

**Arguments**:

* `ID`: User ID (UUID)  [required]
* `OUT_DIR`: Output directory for the profile image file  [required]

**Options**:

* `--filename TEXT`: Filename to use (defaults to original filename or profile-{user_id})
* `--show-progress`: Show progress bar while downloading
* `--help`: Show this message and exit.

## `immich users-admin`

Administrative endpoints for managing users, including creating, updating, deleting, and restoring users. Also includes endpoints for resetting passwords and PIN codes.

<a href="https://api.immich.app/endpoints/users-admin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-user-admin`: Create a user
* `delete-user-admin`: Delete a user
* `get-user-admin`: Retrieve a user
* `get-user-preferences-admin`: Retrieve user preferences
* `get-user-sessions-admin`: Retrieve user sessions
* `get-user-statistics-admin`: Retrieve user statistics
* `restore-user-admin`: Restore a deleted user
* `search-users-admin`: Search users
* `update-user-admin`: Update a user
* `update-user-preferences-admin`: Update user preferences

### `immich users-admin create-user-admin`

Create a user

<a href="https://api.immich.app/endpoints/users-admin/createUserAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin create-user-admin [OPTIONS]
```

**Options**:

* `--avatar-color TEXT`
* `--email TEXT`: [required]
* `--is-admin [true|false]`
* `--name TEXT`: [required]
* `--notify [true|false]`
* `--password TEXT`: [required]
* `--quota-size-in-bytes INTEGER RANGE`: [x&gt;=0]
* `--should-change-password [true|false]`
* `--storage-label TEXT`
* `--help`: Show this message and exit.

### `immich users-admin delete-user-admin`

Delete a user

<a href="https://api.immich.app/endpoints/users-admin/deleteUserAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin delete-user-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--force [true|false]`
* `--help`: Show this message and exit.

### `immich users-admin get-user-admin`

Retrieve a user

<a href="https://api.immich.app/endpoints/users-admin/getUserAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin get-user-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users-admin get-user-preferences-admin`

Retrieve user preferences

<a href="https://api.immich.app/endpoints/users-admin/getUserPreferencesAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin get-user-preferences-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users-admin get-user-sessions-admin`

Retrieve user sessions

<a href="https://api.immich.app/endpoints/users-admin/getUserSessionsAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin get-user-sessions-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users-admin get-user-statistics-admin`

Retrieve user statistics

<a href="https://api.immich.app/endpoints/users-admin/getUserStatisticsAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin get-user-statistics-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--is-favorite [true|false]`
* `--is-trashed [true|false]`
* `--visibility [archive|timeline|hidden|locked]`
* `--help`: Show this message and exit.

### `immich users-admin restore-user-admin`

Restore a deleted user

<a href="https://api.immich.app/endpoints/users-admin/restoreUserAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin restore-user-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich users-admin search-users-admin`

Search users

<a href="https://api.immich.app/endpoints/users-admin/searchUsersAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin search-users-admin [OPTIONS]
```

**Options**:

* `--id TEXT`
* `--with-deleted [true|false]`
* `--help`: Show this message and exit.

### `immich users-admin update-user-admin`

Update a user

<a href="https://api.immich.app/endpoints/users-admin/updateUserAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin update-user-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--avatar-color TEXT`
* `--email TEXT`
* `--is-admin [true|false]`
* `--name TEXT`
* `--password TEXT`
* `--pin-code TEXT`: Example: 123456
* `--quota-size-in-bytes INTEGER RANGE`: [x&gt;=0]
* `--should-change-password [true|false]`
* `--storage-label TEXT`
* `--help`: Show this message and exit.

### `immich users-admin update-user-preferences-admin`

Update user preferences

<a href="https://api.immich.app/endpoints/users-admin/updateUserPreferencesAdmin">Immich API documentation</a>

**Usage**:

```console
$ immich users-admin update-user-preferences-admin [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--albums-default-asset-order TEXT`
* `--avatar-color TEXT`
* `--cast-g-cast-enabled [true|false]`
* `--download-archive-size INTEGER RANGE`: [x&gt;=1]
* `--download-include-embedded-videos [true|false]`
* `--email-notifications-album-invite [true|false]`
* `--email-notifications-album-update [true|false]`
* `--email-notifications-enabled [true|false]`
* `--folders-enabled [true|false]`
* `--folders-sidebar-web [true|false]`
* `--memories-duration INTEGER RANGE`: [x&gt;=1]
* `--memories-enabled [true|false]`
* `--people-enabled [true|false]`
* `--people-sidebar-web [true|false]`
* `--purchase-hide-buy-button-until TEXT`
* `--purchase-show-support-badge [true|false]`
* `--ratings-enabled [true|false]`
* `--shared-links-enabled [true|false]`
* `--shared-links-sidebar-web [true|false]`
* `--tags-enabled [true|false]`
* `--tags-sidebar-web [true|false]`
* `--help`: Show this message and exit.

## `immich views`

Endpoints for specialized views, such as the folder view.

<a href="https://api.immich.app/endpoints/views">Immich API documentation</a>

**Usage**:

```console
$ immich views [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-assets-by-original-path`: Retrieve assets by original path
* `get-unique-original-paths`: Retrieve unique paths

### `immich views get-assets-by-original-path`

Retrieve assets by original path

<a href="https://api.immich.app/endpoints/views/getAssetsByOriginalPath">Immich API documentation</a>

**Usage**:

```console
$ immich views get-assets-by-original-path [OPTIONS]
```

**Options**:

* `--path TEXT`: [required]
* `--help`: Show this message and exit.

### `immich views get-unique-original-paths`

Retrieve unique paths

<a href="https://api.immich.app/endpoints/views/getUniqueOriginalPaths">Immich API documentation</a>

**Usage**:

```console
$ immich views get-unique-original-paths [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `immich workflows`

A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.

<a href="https://api.immich.app/endpoints/workflows">Immich API documentation</a>

**Usage**:

```console
$ immich workflows [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create-workflow`: Create a workflow
* `delete-workflow`: Delete a workflow
* `get-workflow`: Retrieve a workflow
* `get-workflows`: List all workflows
* `update-workflow`: Update a workflow

### `immich workflows create-workflow`

Create a workflow

<a href="https://api.immich.app/endpoints/workflows/createWorkflow">Immich API documentation</a>

**Usage**:

```console
$ immich workflows create-workflow [OPTIONS]
```

**Options**:

* `--actions TEXT`: As a JSON string  [required]
* `--description TEXT`
* `--enabled [true|false]`
* `--filters TEXT`: As a JSON string  [required]
* `--name TEXT`: [required]
* `--trigger-type TEXT`: [required]
* `--help`: Show this message and exit.

### `immich workflows delete-workflow`

Delete a workflow

<a href="https://api.immich.app/endpoints/workflows/deleteWorkflow">Immich API documentation</a>

**Usage**:

```console
$ immich workflows delete-workflow [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich workflows get-workflow`

Retrieve a workflow

<a href="https://api.immich.app/endpoints/workflows/getWorkflow">Immich API documentation</a>

**Usage**:

```console
$ immich workflows get-workflow [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `immich workflows get-workflows`

List all workflows

<a href="https://api.immich.app/endpoints/workflows/getWorkflows">Immich API documentation</a>

**Usage**:

```console
$ immich workflows get-workflows [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `immich workflows update-workflow`

Update a workflow

<a href="https://api.immich.app/endpoints/workflows/updateWorkflow">Immich API documentation</a>

**Usage**:

```console
$ immich workflows update-workflow [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--actions TEXT`: As a JSON string
* `--description TEXT`
* `--enabled [true|false]`
* `--filters TEXT`: As a JSON string
* `--name TEXT`
* `--help`: Show this message and exit.
