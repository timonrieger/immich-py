"""Generated CLI commands (auto-generated, do not edit)."""

from __future__ import annotations

from typing import Any
import typer

from immich.cli.generated.apps import api_keys
from immich.cli.generated.apps import activities
from immich.cli.generated.apps import albums
from immich.cli.generated.apps import assets
from immich.cli.generated.apps import authentication
from immich.cli.generated.apps import authentication_(admin)
from immich.cli.generated.apps import download
from immich.cli.generated.apps import duplicates
from immich.cli.generated.apps import faces
from immich.cli.generated.apps import jobs
from immich.cli.generated.apps import libraries
from immich.cli.generated.apps import maintenance_(admin)
from immich.cli.generated.apps import map
from immich.cli.generated.apps import memories
from immich.cli.generated.apps import notifications
from immich.cli.generated.apps import notifications_(admin)
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
from immich.cli.generated.apps import users_(admin)
from immich.cli.generated.apps import views
from immich.cli.generated.apps import workflows

APPS: dict[str, typer.Typer] = {
    "API keys": api_keys.app,
    "Activities": activities.app,
    "Albums": albums.app,
    "Assets": assets.app,
    "Authentication": authentication.app,
    "Authentication (admin)": authentication_(admin).app,
    "Download": download.app,
    "Duplicates": duplicates.app,
    "Faces": faces.app,
    "Jobs": jobs.app,
    "Libraries": libraries.app,
    "Maintenance (admin)": maintenance_(admin).app,
    "Map": map.app,
    "Memories": memories.app,
    "Notifications": notifications.app,
    "Notifications (admin)": notifications_(admin).app,
    "Partners": partners.app,
    "People": people.app,
    "Plugins": plugins.app,
    "Queues": queues.app,
    "Search": search.app,
    "Server": server.app,
    "Sessions": sessions.app,
    "Shared links": shared_links.app,
    "Stacks": stacks.app,
    "Sync": sync.app,
    "System config": system_config.app,
    "System metadata": system_metadata.app,
    "Tags": tags.app,
    "Timeline": timeline.app,
    "Trash": trash.app,
    "Users": users.app,
    "Users (admin)": users_(admin).app,
    "Views": views.app,
    "Workflows": workflows.app,
}