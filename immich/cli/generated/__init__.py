"""Generated CLI commands (auto-generated, do not edit)."""

from __future__ import annotations

from typing import Any
import typer

from immich.cli.generated.apps import activities
from immich.cli.generated.apps import albums
from immich.cli.generated.apps import api_keys
from immich.cli.generated.apps import assets
from immich.cli.generated.apps import authentication
from immich.cli.generated.apps import authentication_admin
from immich.cli.generated.apps import download
from immich.cli.generated.apps import duplicates
from immich.cli.generated.apps import faces
from immich.cli.generated.apps import jobs
from immich.cli.generated.apps import libraries
from immich.cli.generated.apps import maintenance_admin
from immich.cli.generated.apps import map
from immich.cli.generated.apps import memories
from immich.cli.generated.apps import notifications
from immich.cli.generated.apps import notifications_admin
from immich.cli.generated.apps import partners
from immich.cli.generated.apps import people
from immich.cli.generated.apps import plugins
from immich.cli.generated.apps import queues
from immich.cli.generated.apps import search
from immich.cli.generated.apps import server
from immich.cli.generated.apps import sessions
from immich.cli.generated.apps import shared_links
from immich.cli.generated.apps import stacks
from immich.cli.generated.apps import sync
from immich.cli.generated.apps import system_config
from immich.cli.generated.apps import system_metadata
from immich.cli.generated.apps import tags
from immich.cli.generated.apps import timeline
from immich.cli.generated.apps import trash
from immich.cli.generated.apps import users
from immich.cli.generated.apps import users_admin
from immich.cli.generated.apps import views
from immich.cli.generated.apps import workflows

APPS: dict[str, typer.Typer] = {
    "activities": activities.app,
    "albums": albums.app,
    "api-keys": api_keys.app,
    "assets": assets.app,
    "authentication": authentication.app,
    "authentication-admin": authentication_admin.app,
    "download": download.app,
    "duplicates": duplicates.app,
    "faces": faces.app,
    "jobs": jobs.app,
    "libraries": libraries.app,
    "maintenance-admin": maintenance_admin.app,
    "map": map.app,
    "memories": memories.app,
    "notifications": notifications.app,
    "notifications-admin": notifications_admin.app,
    "partners": partners.app,
    "people": people.app,
    "plugins": plugins.app,
    "queues": queues.app,
    "search": search.app,
    "server": server.app,
    "sessions": sessions.app,
    "shared-links": shared_links.app,
    "stacks": stacks.app,
    "sync": sync.app,
    "system-config": system_config.app,
    "system-metadata": system_metadata.app,
    "tags": tags.app,
    "timeline": timeline.app,
    "trash": trash.app,
    "users": users.app,
    "users-admin": users_admin.app,
    "views": views.app,
    "workflows": workflows.app,
}