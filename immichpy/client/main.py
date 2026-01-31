from __future__ import annotations

from typing import Optional

from aiohttp import ClientSession

from immichpy.client.generated.api_client import ApiClient
from immichpy.client.generated.configuration import Configuration

from immichpy.client.generated.api.activities_api import ActivitiesApi
from immichpy.client.generated.api.albums_api import AlbumsApi
from immichpy.client.generated.api.api_keys_api import APIKeysApi
from immichpy.client.wrapper.assets_api_wrapped import AssetsApiWrapped
from immichpy.client.generated.api.authentication_admin_api import (
    AuthenticationAdminApi,
)
from immichpy.client.generated.api.authentication_api import AuthenticationApi
from immichpy.client.generated.api.database_backups_admin_api import (
    DatabaseBackupsAdminApi,
)
from immichpy.client.generated.api.deprecated_api import DeprecatedApi
from immichpy.client.wrapper.download_api_wrapped import DownloadApiWrapped
from immichpy.client.generated.api.duplicates_api import DuplicatesApi
from immichpy.client.generated.api.faces_api import FacesApi
from immichpy.client.generated.api.jobs_api import JobsApi
from immichpy.client.generated.api.libraries_api import LibrariesApi
from immichpy.client.generated.api.maintenance_admin_api import MaintenanceAdminApi
from immichpy.client.generated.api.map_api import MapApi
from immichpy.client.generated.api.memories_api import MemoriesApi
from immichpy.client.generated.api.notifications_admin_api import NotificationsAdminApi
from immichpy.client.generated.api.notifications_api import NotificationsApi
from immichpy.client.generated.api.partners_api import PartnersApi
from immichpy.client.generated.api.people_api import PeopleApi
from immichpy.client.generated.api.plugins_api import PluginsApi
from immichpy.client.generated.api.queues_api import QueuesApi
from immichpy.client.generated.api.search_api import SearchApi
from immichpy.client.generated.api.server_api import ServerApi
from immichpy.client.generated.api.sessions_api import SessionsApi
from immichpy.client.generated.api.shared_links_api import SharedLinksApi
from immichpy.client.generated.api.stacks_api import StacksApi
from immichpy.client.generated.api.sync_api import SyncApi
from immichpy.client.generated.api.system_config_api import SystemConfigApi
from immichpy.client.generated.api.system_metadata_api import SystemMetadataApi
from immichpy.client.generated.api.tags_api import TagsApi
from immichpy.client.generated.api.timeline_api import TimelineApi
from immichpy.client.generated.api.trash_api import TrashApi
from immichpy.client.generated.api.users_admin_api import UsersAdminApi
from immichpy.client.wrapper.users_api_wrapped import UsersApiWrapped
from immichpy.client.generated.api.views_api import ViewsApi
from immichpy.client.generated.api.workflows_api import WorkflowsApi


def _normalize_base_url(base_url: str) -> str:
    return base_url.strip().rstrip("/")


def _build_configuration(
    *,
    api_key: Optional[str],
    access_token: Optional[str],
    base_url: str,
) -> Configuration:
    config = Configuration(host=_normalize_base_url(base_url))
    if api_key:
        config.api_key["api_key"] = api_key.strip()
    if access_token:
        config.access_token = access_token.strip()
    return config


class AsyncClient:
    """
    Async client for the Immich API.
    """

    activities: ActivitiesApi
    """An activity is a like or a comment made by a user on an asset or album.

    See [ActivitiesApi][immichpy.client.generated.api.activities_api.ActivitiesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/activities) for more information.
    """

    albums: AlbumsApi
    """An album is a collection of assets that can be shared with other users or via shared links.

    See [AlbumsApi][immichpy.client.generated.api.albums_api.AlbumsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/albums) for more information.
    """

    api_keys: APIKeysApi
    """An api key can be used to programmatically access the Immich API.

    See [APIKeysApi][immichpy.client.generated.api.api_keys_api.APIKeysApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/api-keys) for more information.
    """

    assets: AssetsApiWrapped
    """An asset is an image or video that has been uploaded to Immich.

    See [AssetsApiWrapped][immichpy.client.wrapper.assets_api_wrapped.AssetsApiWrapped] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/assets) for more information.
    """

    auth: AuthenticationApi
    """Endpoints related to user authentication, including OAuth.

    See [AuthenticationApi][immichpy.client.generated.api.authentication_api.AuthenticationApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/authentication) for more information.
    """

    auth_admin: AuthenticationAdminApi
    """Administrative endpoints related to authentication.

    See [AuthenticationAdminApi][immichpy.client.generated.api.authentication_admin_api.AuthenticationAdminApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/authentication-(admin)) for more information.
    """

    deprecated: DeprecatedApi
    """Deprecated endpoints that are planned for removal in the next major release.

    See [DeprecatedApi][immichpy.client.generated.api.deprecated_api.DeprecatedApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/deprecated) for more information.
    """

    download: DownloadApiWrapped
    """Endpoints for downloading assets or collections of assets.

    See [DownloadApiWrapped][immichpy.client.wrapper.download_api_wrapped.DownloadApiWrapped] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/download) for more information.
    """

    duplicates: DuplicatesApi
    """Endpoints for managing and identifying duplicate assets.

    See [DuplicatesApi][immichpy.client.generated.api.duplicates_api.DuplicatesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/duplicates) for more information.
    """

    faces: FacesApi
    """A face is a detected human face within an asset, which can be associated with a person. Faces are normally detected via machine learning, but can also be created via manually.

    See [FacesApi][immichpy.client.generated.api.faces_api.FacesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/faces) for more information.
    """

    jobs: JobsApi
    """Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

    See [JobsApi][immichpy.client.generated.api.jobs_api.JobsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/jobs) for more information.
    """

    libraries: LibrariesApi
    """An external library is made up of input file paths or expressions that are scanned for asset files. Discovered files are automatically imported. Assets much be unique within a library, but can be duplicated across libraries. Each user has a default upload library, and can have one or more external libraries.

    See [LibrariesApi][immichpy.client.generated.api.libraries_api.LibrariesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/libraries) for more information.
    """

    maintenance_admin: MaintenanceAdminApi
    """Maintenance mode allows you to put Immich in a read-only state to perform various operations.

    See [MaintenanceAdminApi][immichpy.client.generated.api.maintenance_admin_api.MaintenanceAdminApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/maintenance-(admin)) for more information.
    """

    map: MapApi
    """Map endpoints include supplemental functionality related to geolocation, such as reverse geocoding and retrieving map markers for assets with geolocation data.

    See [MapApi][immichpy.client.generated.api.map_api.MapApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/map) for more information.
    """

    memories: MemoriesApi
    """A memory is a specialized collection of assets with dedicated viewing implementations in the web and mobile clients. A memory includes fields related to visibility and are automatically generated per user via a background job.

    See [MemoriesApi][immichpy.client.generated.api.memories_api.MemoriesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/memories) for more information.
    """

    notifications: NotificationsApi
    """A notification is a specialized message sent to users to inform them of important events. Currently, these notifications are only shown in the Immich web application.

    See [NotificationsApi][immichpy.client.generated.api.notifications_api.NotificationsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/notifications) for more information.
    """

    notifications_admin: NotificationsAdminApi
    """Notification administrative endpoints.

    See [NotificationsAdminApi][immichpy.client.generated.api.notifications_admin_api.NotificationsAdminApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/notifications-(admin)) for more information.
    """

    partners: PartnersApi
    """A partner is a link with another user that allows sharing of assets between two users.

    See [PartnersApi][immichpy.client.generated.api.partners_api.PartnersApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/partners) for more information.
    """

    people: PeopleApi
    """A person is a collection of faces, which can be favorited and named. A person can also be merged into another person. People are automatically created via the face recognition job.

    See [PeopleApi][immichpy.client.generated.api.people_api.PeopleApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/people) for more information.
    """

    plugins: PluginsApi
    """A plugin is an installed module that makes filters and actions available for the workflow feature.

    See [PluginsApi][immichpy.client.generated.api.plugins_api.PluginsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/plugins) for more information.
    """

    queues: QueuesApi
    """Queues and background jobs are used for processing tasks asynchronously. Queues can be paused and resumed as needed.

    See [QueuesApi][immichpy.client.generated.api.queues_api.QueuesApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/queues) for more information.
    """

    search: SearchApi
    """Endpoints related to searching assets via text, smart search, optical character recognition (OCR), and other filters like person, album, and other metadata. Search endpoints usually support pagination and sorting.

    See [SearchApi][immichpy.client.generated.api.search_api.SearchApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/search) for more information.
    """

    server: ServerApi
    """Information about the current server deployment, including version and build information, available features, supported media types, and more.

    See [ServerApi][immichpy.client.generated.api.server_api.ServerApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/server) for more information.
    """

    sessions: SessionsApi
    """A session represents an authenticated login session for a user. Sessions also appear in the web application as "Authorized devices".

    See [SessionsApi][immichpy.client.generated.api.sessions_api.SessionsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/sessions) for more information.
    """

    shared_links: SharedLinksApi
    """A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.

    See [SharedLinksApi][immichpy.client.generated.api.shared_links_api.SharedLinksApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/shared-links) for more information.
    """

    stacks: StacksApi
    """A stack is a group of related assets. One asset is the "primary" asset, and the rest are "child" assets. On the main timeline, stack parents are included by default, while child assets are hidden.

    See [StacksApi][immichpy.client.generated.api.stacks_api.StacksApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/stacks) for more information.
    """

    sync: SyncApi
    """A collection of endpoints for the new mobile synchronization implementation.

    See [SyncApi][immichpy.client.generated.api.sync_api.SyncApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/sync) for more information.
    """

    system_config: SystemConfigApi
    """Endpoints to view, modify, and validate the system configuration settings.

    See [SystemConfigApi][immichpy.client.generated.api.system_config_api.SystemConfigApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/system-config) for more information.
    """

    system_metadata: SystemMetadataApi
    """Endpoints to view, modify, and validate the system metadata, which includes information about things like admin onboarding status.

    See [SystemMetadataApi][immichpy.client.generated.api.system_metadata_api.SystemMetadataApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/system-metadata) for more information.
    """

    tags: TagsApi
    """A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.

    See [TagsApi][immichpy.client.generated.api.tags_api.TagsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/tags) for more information.
    """

    timeline: TimelineApi
    """Specialized endpoints related to the timeline implementation used in the web application. External applications or tools should not use or rely on these endpoints, as they are subject to change without notice.

    See [TimelineApi][immichpy.client.generated.api.timeline_api.TimelineApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/timeline) for more information.
    """

    trash: TrashApi
    """Endpoints for managing the trash can, which includes assets that have been discarded. Items in the trash are automatically deleted after a configured amount of time.

    See [TrashApi][immichpy.client.generated.api.trash_api.TrashApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/trash) for more information.
    """

    users_admin: UsersAdminApi
    """Administrative endpoints for managing users, including creating, updating, deleting, and restoring users. Also includes endpoints for resetting passwords and PIN codes.

    See [UsersAdminApi][immichpy.client.generated.api.users_admin_api.UsersAdminApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/users-(admin)) for more information.
    """

    users: UsersApiWrapped
    """Endpoints for viewing and updating the current users, including product key information, profile picture data, onboarding progress, and more.

    See [UsersApiWrapped][immichpy.client.wrapper.users_api_wrapped.UsersApiWrapped] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/users) for more information.
    """

    views: ViewsApi
    """Endpoints for specialized views, such as the folder view.

    See [ViewsApi][immichpy.client.generated.api.views_api.ViewsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/views) for more information.
    """

    workflows: WorkflowsApi
    """A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.

    See [WorkflowsApi][immichpy.client.generated.api.workflows_api.WorkflowsApi] for available methods and [Immich API Documentation](https://api.immich.app/endpoints/workflows) for more information.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None,
        base_url: str,
        http_client: Optional[ClientSession] = None,
    ) -> None:
        """
        :param api_key: The API key to use for authentication.
        :param access_token: The access token to use for authentication.
        :param base_url: The base URL of the Immich API.
        :param http_client: Inject your own connection session if you want to control networking.
        :param retries: The number of times to retry a HTTP request if it fails. Defaults to None, meaning no retries.
        """
        self._owns_http_client = http_client is None
        self._injected_http_client = http_client
        self.config = _build_configuration(
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
        )
        self.base_client = ApiClient(configuration=self.config)
        self.base_client.user_agent = "immichpy"

        # Allow caller to inject a pre-configured aiohttp session.
        if http_client is not None:
            self.base_client.rest_client.pool_manager = http_client

        # API groups (single upstream API, not microservices)
        self.activities = ActivitiesApi(self.base_client)
        self.albums = AlbumsApi(self.base_client)
        self.api_keys = APIKeysApi(self.base_client)
        self.assets = AssetsApiWrapped(self.base_client)
        self.auth = AuthenticationApi(self.base_client)
        self.auth_admin = AuthenticationAdminApi(self.base_client)
        self.backups = DatabaseBackupsAdminApi(self.base_client)
        self.deprecated = DeprecatedApi(self.base_client)
        self.download = DownloadApiWrapped(self.base_client)
        self.duplicates = DuplicatesApi(self.base_client)
        self.faces = FacesApi(self.base_client)
        self.jobs = JobsApi(self.base_client)
        self.libraries = LibrariesApi(self.base_client)
        self.maintenance_admin = MaintenanceAdminApi(self.base_client)
        self.map = MapApi(self.base_client)
        self.memories = MemoriesApi(self.base_client)
        self.notifications = NotificationsApi(self.base_client)
        self.notifications_admin = NotificationsAdminApi(self.base_client)
        self.partners = PartnersApi(self.base_client)
        self.people = PeopleApi(self.base_client)
        self.plugins = PluginsApi(self.base_client)
        self.queues = QueuesApi(self.base_client)
        self.search = SearchApi(self.base_client)
        self.server = ServerApi(self.base_client)
        self.sessions = SessionsApi(self.base_client)
        self.shared_links = SharedLinksApi(self.base_client)
        self.stacks = StacksApi(self.base_client)
        self.sync = SyncApi(self.base_client)
        self.system_config = SystemConfigApi(self.base_client)
        self.system_metadata = SystemMetadataApi(self.base_client)
        self.tags = TagsApi(self.base_client)
        self.timeline = TimelineApi(self.base_client)
        self.trash = TrashApi(self.base_client)
        self.users = UsersApiWrapped(self.base_client)
        self.users_admin = UsersAdminApi(self.base_client)
        self.views = ViewsApi(self.base_client)
        self.workflows = WorkflowsApi(self.base_client)

    async def close(self) -> None:
        """Close the client and release resources."""

        rest_client = self.base_client.rest_client
        session = rest_client.pool_manager

        # Always detach so base_client doesn't hold stale refs
        rest_client.pool_manager = None

        # Only close if WE created it
        if self._owns_http_client and session is not None and not session.closed:
            await session.close()

        # Now close higher-level stuff that does NOT own the session
        await self.base_client.close()

    async def __aenter__(self) -> "AsyncClient":
        """Enter the context manager."""
        if self._injected_http_client is None:
            self._injected_http_client = ClientSession()
        self.base_client.rest_client.pool_manager = self._injected_http_client
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the context manager."""
        await self.close()
