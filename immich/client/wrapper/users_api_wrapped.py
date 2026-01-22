from __future__ import annotations

from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from immich.client.generated.api.users_api import UsersApi
from immich.client.types import HeadersType
from immich.client.utils.download import download_file, resolve_output_filename


class UsersApiWrapped(UsersApi):
    """Wrapper for the UsersApi that provides convenience methods."""

    async def get_profile_image_to_file(
        self,
        id: UUID,
        out_dir: Path,
        filename: Optional[str] = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Download a user's profile image and save it to a file.

        :param id: The user ID.
        :param out_dir: The directory to write the profile image to.
        :param filename: The filename to use. If not provided, we try to derive it from the headers
            or default to "profile-" + user_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `get_profile_image_without_preload_content` method.

        For exact request/response behavior, inspect `UsersApi.get_profile_image_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[HeadersType]):
            return self.get_profile_image_without_preload_content(
                id=id,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"profile-{id}",
            ),
            show_progress=show_progress,
        )
