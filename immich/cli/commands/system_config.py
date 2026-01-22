"""Generated CLI commands for System config tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immich import AsyncClient

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.generated.models import *

app = typer.Typer(
    help="""Endpoints to view, modify, and validate the system configuration settings.\n\n[link=https://api.immich.app/endpoints/system-config]Immich API documentation[/link]"""
)


@app.command("get-config", deprecated=False, rich_help_panel="API commands")
def get_config(
    ctx: typer.Context,
) -> None:
    """Get system configuration

    [link=https://api.immich.app/endpoints/system-config/getConfig]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.system_config, "get_config", ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-config-defaults", deprecated=False, rich_help_panel="API commands")
def get_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get system configuration defaults

    [link=https://api.immich.app/endpoints/system-config/getConfigDefaults]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_config, "get_config_defaults", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command(
    "get-storage-template-options", deprecated=False, rich_help_panel="API commands"
)
def get_storage_template_options(
    ctx: typer.Context,
) -> None:
    """Get storage template options

    [link=https://api.immich.app/endpoints/system-config/getStorageTemplateOptions]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client, client.system_config, "get_storage_template_options", ctx, **kwargs
    )
    print_response(result, ctx)


@app.command("update-config", deprecated=False, rich_help_panel="API commands")
def update_config(
    ctx: typer.Context,
    backup_database_cron_expression: str = typer.Option(
        ..., "--backup-database-cron-expression", help=""""""
    ),
    backup_database_enabled: bool = typer.Option(
        ..., "--backup-database-enabled", help=""""""
    ),
    backup_database_keep_last_amount: float = typer.Option(
        ..., "--backup-database-keep-last-amount", help="""""", min=1
    ),
    ffmpeg_accel: str = typer.Option(..., "--ffmpeg-accel", help=""""""),
    ffmpeg_accel_decode: bool = typer.Option(..., "--ffmpeg-accel-decode", help=""""""),
    ffmpeg_accepted_audio_codecs: list[AudioCodec] = typer.Option(
        ..., "--ffmpeg-accepted-audio-codecs", help=""""""
    ),
    ffmpeg_accepted_containers: list[VideoContainer] = typer.Option(
        ..., "--ffmpeg-accepted-containers", help=""""""
    ),
    ffmpeg_accepted_video_codecs: list[VideoCodec] = typer.Option(
        ..., "--ffmpeg-accepted-video-codecs", help=""""""
    ),
    ffmpeg_bframes: int = typer.Option(
        ..., "--ffmpeg-bframes", help="""""", min=-1, max=16
    ),
    ffmpeg_cq_mode: str = typer.Option(..., "--ffmpeg-cq-mode", help=""""""),
    ffmpeg_crf: int = typer.Option(..., "--ffmpeg-crf", help="""""", min=0, max=51),
    ffmpeg_gop_size: int = typer.Option(..., "--ffmpeg-gop-size", help="""""", min=0),
    ffmpeg_max_bitrate: str = typer.Option(..., "--ffmpeg-max-bitrate", help=""""""),
    ffmpeg_preferred_hw_device: str = typer.Option(
        ..., "--ffmpeg-preferred-hw-device", help=""""""
    ),
    ffmpeg_preset: str = typer.Option(..., "--ffmpeg-preset", help=""""""),
    ffmpeg_refs: int = typer.Option(..., "--ffmpeg-refs", help="""""", min=0, max=6),
    ffmpeg_target_audio_codec: str = typer.Option(
        ..., "--ffmpeg-target-audio-codec", help=""""""
    ),
    ffmpeg_target_resolution: str = typer.Option(
        ..., "--ffmpeg-target-resolution", help=""""""
    ),
    ffmpeg_target_video_codec: str = typer.Option(
        ..., "--ffmpeg-target-video-codec", help=""""""
    ),
    ffmpeg_temporal_aq: bool = typer.Option(..., "--ffmpeg-temporal-aq", help=""""""),
    ffmpeg_threads: int = typer.Option(..., "--ffmpeg-threads", help="""""", min=0),
    ffmpeg_tonemap: str = typer.Option(..., "--ffmpeg-tonemap", help=""""""),
    ffmpeg_transcode: str = typer.Option(..., "--ffmpeg-transcode", help=""""""),
    ffmpeg_two_pass: bool = typer.Option(..., "--ffmpeg-two-pass", help=""""""),
    image_colorspace: str = typer.Option(..., "--image-colorspace", help=""""""),
    image_extract_embedded: bool = typer.Option(
        ..., "--image-extract-embedded", help=""""""
    ),
    image_fullsize_enabled: bool = typer.Option(
        ..., "--image-fullsize-enabled", help=""""""
    ),
    image_fullsize_format: str = typer.Option(
        ..., "--image-fullsize-format", help=""""""
    ),
    image_fullsize_quality: int = typer.Option(
        ..., "--image-fullsize-quality", help="""""", min=1, max=100
    ),
    image_preview_format: str = typer.Option(
        ..., "--image-preview-format", help=""""""
    ),
    image_preview_quality: int = typer.Option(
        ..., "--image-preview-quality", help="""""", min=1, max=100
    ),
    image_preview_size: int = typer.Option(
        ..., "--image-preview-size", help="""""", min=1
    ),
    image_thumbnail_format: str = typer.Option(
        ..., "--image-thumbnail-format", help=""""""
    ),
    image_thumbnail_quality: int = typer.Option(
        ..., "--image-thumbnail-quality", help="""""", min=1, max=100
    ),
    image_thumbnail_size: int = typer.Option(
        ..., "--image-thumbnail-size", help="""""", min=1
    ),
    job_background_task_concurrency: int = typer.Option(
        ..., "--job-background-task-concurrency", help="""""", min=1
    ),
    job_face_detection_concurrency: int = typer.Option(
        ..., "--job-face-detection-concurrency", help="""""", min=1
    ),
    job_library_concurrency: int = typer.Option(
        ..., "--job-library-concurrency", help="""""", min=1
    ),
    job_metadata_extraction_concurrency: int = typer.Option(
        ..., "--job-metadata-extraction-concurrency", help="""""", min=1
    ),
    job_migration_concurrency: int = typer.Option(
        ..., "--job-migration-concurrency", help="""""", min=1
    ),
    job_notifications_concurrency: int = typer.Option(
        ..., "--job-notifications-concurrency", help="""""", min=1
    ),
    job_ocr_concurrency: int = typer.Option(
        ..., "--job-ocr-concurrency", help="""""", min=1
    ),
    job_search_concurrency: int = typer.Option(
        ..., "--job-search-concurrency", help="""""", min=1
    ),
    job_sidecar_concurrency: int = typer.Option(
        ..., "--job-sidecar-concurrency", help="""""", min=1
    ),
    job_smart_search_concurrency: int = typer.Option(
        ..., "--job-smart-search-concurrency", help="""""", min=1
    ),
    job_thumbnail_generation_concurrency: int = typer.Option(
        ..., "--job-thumbnail-generation-concurrency", help="""""", min=1
    ),
    job_video_conversion_concurrency: int = typer.Option(
        ..., "--job-video-conversion-concurrency", help="""""", min=1
    ),
    job_workflow_concurrency: int = typer.Option(
        ..., "--job-workflow-concurrency", help="""""", min=1
    ),
    library_scan_cron_expression: str = typer.Option(
        ..., "--library-scan-cron-expression", help=""""""
    ),
    library_scan_enabled: bool = typer.Option(
        ..., "--library-scan-enabled", help=""""""
    ),
    library_watch_enabled: bool = typer.Option(
        ..., "--library-watch-enabled", help=""""""
    ),
    logging_enabled: bool = typer.Option(..., "--logging-enabled", help=""""""),
    logging_level: str = typer.Option(..., "--logging-level", help=""""""),
    machine_learning_availability_checks_enabled: bool = typer.Option(
        ..., "--machine-learning-availability-checks-enabled", help=""""""
    ),
    machine_learning_availability_checks_interval: float = typer.Option(
        ..., "--machine-learning-availability-checks-interval", help=""""""
    ),
    machine_learning_availability_checks_timeout: float = typer.Option(
        ..., "--machine-learning-availability-checks-timeout", help=""""""
    ),
    machine_learning_clip_enabled: bool = typer.Option(
        ..., "--machine-learning-clip-enabled", help=""""""
    ),
    machine_learning_clip_model_name: str = typer.Option(
        ..., "--machine-learning-clip-model-name", help=""""""
    ),
    machine_learning_duplicate_detection_enabled: bool = typer.Option(
        ..., "--machine-learning-duplicate-detection-enabled", help=""""""
    ),
    machine_learning_duplicate_detection_max_distance: float = typer.Option(
        ...,
        "--machine-learning-duplicate-detection-max-distance",
        help="""""",
        min=0.001,
        max=0.1,
    ),
    machine_learning_enabled: bool = typer.Option(
        ..., "--machine-learning-enabled", help=""""""
    ),
    machine_learning_facial_recognition_enabled: bool = typer.Option(
        ..., "--machine-learning-facial-recognition-enabled", help=""""""
    ),
    machine_learning_facial_recognition_max_distance: float = typer.Option(
        ...,
        "--machine-learning-facial-recognition-max-distance",
        help="""""",
        min=0.1,
        max=2,
    ),
    machine_learning_facial_recognition_min_faces: int = typer.Option(
        ..., "--machine-learning-facial-recognition-min-faces", help="""""", min=1
    ),
    machine_learning_facial_recognition_min_score: float = typer.Option(
        ...,
        "--machine-learning-facial-recognition-min-score",
        help="""""",
        min=0.1,
        max=1,
    ),
    machine_learning_facial_recognition_model_name: str = typer.Option(
        ..., "--machine-learning-facial-recognition-model-name", help=""""""
    ),
    machine_learning_ocr_enabled: bool = typer.Option(
        ..., "--machine-learning-ocr-enabled", help=""""""
    ),
    machine_learning_ocr_max_resolution: int = typer.Option(
        ..., "--machine-learning-ocr-max-resolution", help="""""", min=1
    ),
    machine_learning_ocr_min_detection_score: float = typer.Option(
        ..., "--machine-learning-ocr-min-detection-score", help="""""", min=0.1, max=1
    ),
    machine_learning_ocr_min_recognition_score: float = typer.Option(
        ..., "--machine-learning-ocr-min-recognition-score", help="""""", min=0.1, max=1
    ),
    machine_learning_ocr_model_name: str = typer.Option(
        ..., "--machine-learning-ocr-model-name", help=""""""
    ),
    machine_learning_urls: list[str] = typer.Option(
        ..., "--machine-learning-urls", help=""""""
    ),
    map_dark_style: str = typer.Option(..., "--map-dark-style", help=""""""),
    map_enabled: bool = typer.Option(..., "--map-enabled", help=""""""),
    map_light_style: str = typer.Option(..., "--map-light-style", help=""""""),
    metadata_faces_import_: bool = typer.Option(
        ..., "--metadata-faces-import", help=""""""
    ),
    new_version_check_enabled: bool = typer.Option(
        ..., "--new-version-check-enabled", help=""""""
    ),
    nightly_tasks_cluster_new_faces: bool = typer.Option(
        ..., "--nightly-tasks-cluster-new-faces", help=""""""
    ),
    nightly_tasks_database_cleanup: bool = typer.Option(
        ..., "--nightly-tasks-database-cleanup", help=""""""
    ),
    nightly_tasks_generate_memories: bool = typer.Option(
        ..., "--nightly-tasks-generate-memories", help=""""""
    ),
    nightly_tasks_missing_thumbnails: bool = typer.Option(
        ..., "--nightly-tasks-missing-thumbnails", help=""""""
    ),
    nightly_tasks_start_time: str = typer.Option(
        ..., "--nightly-tasks-start-time", help=""""""
    ),
    nightly_tasks_sync_quota_usage: bool = typer.Option(
        ..., "--nightly-tasks-sync-quota-usage", help=""""""
    ),
    notifications_smtp_enabled: bool = typer.Option(
        ..., "--notifications-smtp-enabled", help=""""""
    ),
    notifications_smtp_from_: str = typer.Option(
        ..., "--notifications-smtp-from", help=""""""
    ),
    notifications_smtp_reply_to: str = typer.Option(
        ..., "--notifications-smtp-reply-to", help=""""""
    ),
    notifications_smtp_transport_host: str = typer.Option(
        ..., "--notifications-smtp-transport-host", help=""""""
    ),
    notifications_smtp_transport_ignore_cert: bool = typer.Option(
        ..., "--notifications-smtp-transport-ignore-cert", help=""""""
    ),
    notifications_smtp_transport_password: str = typer.Option(
        ..., "--notifications-smtp-transport-password", help=""""""
    ),
    notifications_smtp_transport_port: float = typer.Option(
        ..., "--notifications-smtp-transport-port", help="""""", min=0, max=65535
    ),
    notifications_smtp_transport_secure: bool = typer.Option(
        ..., "--notifications-smtp-transport-secure", help=""""""
    ),
    notifications_smtp_transport_username: str = typer.Option(
        ..., "--notifications-smtp-transport-username", help=""""""
    ),
    oauth_auto_launch: bool = typer.Option(..., "--oauth-auto-launch", help=""""""),
    oauth_auto_register: bool = typer.Option(..., "--oauth-auto-register", help=""""""),
    oauth_button_text: str = typer.Option(..., "--oauth-button-text", help=""""""),
    oauth_client_id: str = typer.Option(..., "--oauth-client-id", help=""""""),
    oauth_client_secret: str = typer.Option(..., "--oauth-client-secret", help=""""""),
    oauth_default_storage_quota: int = typer.Option(
        ..., "--oauth-default-storage-quota", help="""""", min=0
    ),
    oauth_enabled: bool = typer.Option(..., "--oauth-enabled", help=""""""),
    oauth_issuer_url: str = typer.Option(..., "--oauth-issuer-url", help=""""""),
    oauth_mobile_override_enabled: bool = typer.Option(
        ..., "--oauth-mobile-override-enabled", help=""""""
    ),
    oauth_mobile_redirect_uri: str = typer.Option(
        ..., "--oauth-mobile-redirect-uri", help=""""""
    ),
    oauth_profile_signing_algorithm: str = typer.Option(
        ..., "--oauth-profile-signing-algorithm", help=""""""
    ),
    oauth_role_claim: str = typer.Option(..., "--oauth-role-claim", help=""""""),
    oauth_scope: str = typer.Option(..., "--oauth-scope", help=""""""),
    oauth_signing_algorithm: str = typer.Option(
        ..., "--oauth-signing-algorithm", help=""""""
    ),
    oauth_storage_label_claim: str = typer.Option(
        ..., "--oauth-storage-label-claim", help=""""""
    ),
    oauth_storage_quota_claim: str = typer.Option(
        ..., "--oauth-storage-quota-claim", help=""""""
    ),
    oauth_timeout: int = typer.Option(..., "--oauth-timeout", help="""""", min=1),
    oauth_token_endpoint_auth_method: str = typer.Option(
        ..., "--oauth-token-endpoint-auth-method", help=""""""
    ),
    password_login_enabled: bool = typer.Option(
        ..., "--password-login-enabled", help=""""""
    ),
    reverse_geocoding_enabled: bool = typer.Option(
        ..., "--reverse-geocoding-enabled", help=""""""
    ),
    server_external_domain: str = typer.Option(
        ..., "--server-external-domain", help=""""""
    ),
    server_login_page_message: str = typer.Option(
        ..., "--server-login-page-message", help=""""""
    ),
    server_public_users: bool = typer.Option(..., "--server-public-users", help=""""""),
    storage_template_enabled: bool = typer.Option(
        ..., "--storage-template-enabled", help=""""""
    ),
    storage_template_hash_verification_enabled: bool = typer.Option(
        ..., "--storage-template-hash-verification-enabled", help=""""""
    ),
    storage_template_template: str = typer.Option(
        ..., "--storage-template-template", help=""""""
    ),
    templates_email_album_invite_template: str = typer.Option(
        ..., "--templates-email-album-invite-template", help=""""""
    ),
    templates_email_album_update_template: str = typer.Option(
        ..., "--templates-email-album-update-template", help=""""""
    ),
    templates_email_welcome_template: str = typer.Option(
        ..., "--templates-email-welcome-template", help=""""""
    ),
    theme_custom_css: str = typer.Option(..., "--theme-custom-css", help=""""""),
    trash_days: int = typer.Option(..., "--trash-days", help="""""", min=0),
    trash_enabled: bool = typer.Option(..., "--trash-enabled", help=""""""),
    user_delete_delay: int = typer.Option(
        ..., "--user-delete-delay", help="""""", min=1
    ),
) -> None:
    """Update system configuration

    [link=https://api.immich.app/endpoints/system-config/updateConfig]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(
        json_data, ["backup_database_cron_expression"], backup_database_cron_expression
    )
    set_nested(json_data, ["backup_database_enabled"], backup_database_enabled)
    set_nested(
        json_data,
        ["backup_database_keep_last_amount"],
        backup_database_keep_last_amount,
    )
    set_nested(json_data, ["ffmpeg_accel"], ffmpeg_accel)
    set_nested(json_data, ["ffmpeg_accel_decode"], ffmpeg_accel_decode)
    set_nested(
        json_data, ["ffmpeg_accepted_audio_codecs"], ffmpeg_accepted_audio_codecs
    )
    set_nested(json_data, ["ffmpeg_accepted_containers"], ffmpeg_accepted_containers)
    set_nested(
        json_data, ["ffmpeg_accepted_video_codecs"], ffmpeg_accepted_video_codecs
    )
    set_nested(json_data, ["ffmpeg_bframes"], ffmpeg_bframes)
    set_nested(json_data, ["ffmpeg_cq_mode"], ffmpeg_cq_mode)
    set_nested(json_data, ["ffmpeg_crf"], ffmpeg_crf)
    set_nested(json_data, ["ffmpeg_gop_size"], ffmpeg_gop_size)
    set_nested(json_data, ["ffmpeg_max_bitrate"], ffmpeg_max_bitrate)
    set_nested(json_data, ["ffmpeg_preferred_hw_device"], ffmpeg_preferred_hw_device)
    set_nested(json_data, ["ffmpeg_preset"], ffmpeg_preset)
    set_nested(json_data, ["ffmpeg_refs"], ffmpeg_refs)
    set_nested(json_data, ["ffmpeg_target_audio_codec"], ffmpeg_target_audio_codec)
    set_nested(json_data, ["ffmpeg_target_resolution"], ffmpeg_target_resolution)
    set_nested(json_data, ["ffmpeg_target_video_codec"], ffmpeg_target_video_codec)
    set_nested(json_data, ["ffmpeg_temporal_aq"], ffmpeg_temporal_aq)
    set_nested(json_data, ["ffmpeg_threads"], ffmpeg_threads)
    set_nested(json_data, ["ffmpeg_tonemap"], ffmpeg_tonemap)
    set_nested(json_data, ["ffmpeg_transcode"], ffmpeg_transcode)
    set_nested(json_data, ["ffmpeg_two_pass"], ffmpeg_two_pass)
    set_nested(json_data, ["image_colorspace"], image_colorspace)
    set_nested(json_data, ["image_extract_embedded"], image_extract_embedded)
    set_nested(json_data, ["image_fullsize_enabled"], image_fullsize_enabled)
    set_nested(json_data, ["image_fullsize_format"], image_fullsize_format)
    set_nested(json_data, ["image_fullsize_quality"], image_fullsize_quality)
    set_nested(json_data, ["image_preview_format"], image_preview_format)
    set_nested(json_data, ["image_preview_quality"], image_preview_quality)
    set_nested(json_data, ["image_preview_size"], image_preview_size)
    set_nested(json_data, ["image_thumbnail_format"], image_thumbnail_format)
    set_nested(json_data, ["image_thumbnail_quality"], image_thumbnail_quality)
    set_nested(json_data, ["image_thumbnail_size"], image_thumbnail_size)
    set_nested(
        json_data, ["job_background_task_concurrency"], job_background_task_concurrency
    )
    set_nested(
        json_data, ["job_face_detection_concurrency"], job_face_detection_concurrency
    )
    set_nested(json_data, ["job_library_concurrency"], job_library_concurrency)
    set_nested(
        json_data,
        ["job_metadata_extraction_concurrency"],
        job_metadata_extraction_concurrency,
    )
    set_nested(json_data, ["job_migration_concurrency"], job_migration_concurrency)
    set_nested(
        json_data, ["job_notifications_concurrency"], job_notifications_concurrency
    )
    set_nested(json_data, ["job_ocr_concurrency"], job_ocr_concurrency)
    set_nested(json_data, ["job_search_concurrency"], job_search_concurrency)
    set_nested(json_data, ["job_sidecar_concurrency"], job_sidecar_concurrency)
    set_nested(
        json_data, ["job_smart_search_concurrency"], job_smart_search_concurrency
    )
    set_nested(
        json_data,
        ["job_thumbnail_generation_concurrency"],
        job_thumbnail_generation_concurrency,
    )
    set_nested(
        json_data,
        ["job_video_conversion_concurrency"],
        job_video_conversion_concurrency,
    )
    set_nested(json_data, ["job_workflow_concurrency"], job_workflow_concurrency)
    set_nested(
        json_data, ["library_scan_cron_expression"], library_scan_cron_expression
    )
    set_nested(json_data, ["library_scan_enabled"], library_scan_enabled)
    set_nested(json_data, ["library_watch_enabled"], library_watch_enabled)
    set_nested(json_data, ["logging_enabled"], logging_enabled)
    set_nested(json_data, ["logging_level"], logging_level)
    set_nested(
        json_data,
        ["machine_learning_availability_checks_enabled"],
        machine_learning_availability_checks_enabled,
    )
    set_nested(
        json_data,
        ["machine_learning_availability_checks_interval"],
        machine_learning_availability_checks_interval,
    )
    set_nested(
        json_data,
        ["machine_learning_availability_checks_timeout"],
        machine_learning_availability_checks_timeout,
    )
    set_nested(
        json_data, ["machine_learning_clip_enabled"], machine_learning_clip_enabled
    )
    set_nested(
        json_data,
        ["machine_learning_clip_model_name"],
        machine_learning_clip_model_name,
    )
    set_nested(
        json_data,
        ["machine_learning_duplicate_detection_enabled"],
        machine_learning_duplicate_detection_enabled,
    )
    set_nested(
        json_data,
        ["machine_learning_duplicate_detection_max_distance"],
        machine_learning_duplicate_detection_max_distance,
    )
    set_nested(json_data, ["machine_learning_enabled"], machine_learning_enabled)
    set_nested(
        json_data,
        ["machine_learning_facial_recognition_enabled"],
        machine_learning_facial_recognition_enabled,
    )
    set_nested(
        json_data,
        ["machine_learning_facial_recognition_max_distance"],
        machine_learning_facial_recognition_max_distance,
    )
    set_nested(
        json_data,
        ["machine_learning_facial_recognition_min_faces"],
        machine_learning_facial_recognition_min_faces,
    )
    set_nested(
        json_data,
        ["machine_learning_facial_recognition_min_score"],
        machine_learning_facial_recognition_min_score,
    )
    set_nested(
        json_data,
        ["machine_learning_facial_recognition_model_name"],
        machine_learning_facial_recognition_model_name,
    )
    set_nested(
        json_data, ["machine_learning_ocr_enabled"], machine_learning_ocr_enabled
    )
    set_nested(
        json_data,
        ["machine_learning_ocr_max_resolution"],
        machine_learning_ocr_max_resolution,
    )
    set_nested(
        json_data,
        ["machine_learning_ocr_min_detection_score"],
        machine_learning_ocr_min_detection_score,
    )
    set_nested(
        json_data,
        ["machine_learning_ocr_min_recognition_score"],
        machine_learning_ocr_min_recognition_score,
    )
    set_nested(
        json_data, ["machine_learning_ocr_model_name"], machine_learning_ocr_model_name
    )
    set_nested(json_data, ["machine_learning_urls"], machine_learning_urls)
    set_nested(json_data, ["map_dark_style"], map_dark_style)
    set_nested(json_data, ["map_enabled"], map_enabled)
    set_nested(json_data, ["map_light_style"], map_light_style)
    set_nested(json_data, ["metadata_faces_import_"], metadata_faces_import_)
    set_nested(json_data, ["new_version_check_enabled"], new_version_check_enabled)
    set_nested(
        json_data, ["nightly_tasks_cluster_new_faces"], nightly_tasks_cluster_new_faces
    )
    set_nested(
        json_data, ["nightly_tasks_database_cleanup"], nightly_tasks_database_cleanup
    )
    set_nested(
        json_data, ["nightly_tasks_generate_memories"], nightly_tasks_generate_memories
    )
    set_nested(
        json_data,
        ["nightly_tasks_missing_thumbnails"],
        nightly_tasks_missing_thumbnails,
    )
    set_nested(json_data, ["nightly_tasks_start_time"], nightly_tasks_start_time)
    set_nested(
        json_data, ["nightly_tasks_sync_quota_usage"], nightly_tasks_sync_quota_usage
    )
    set_nested(json_data, ["notifications_smtp_enabled"], notifications_smtp_enabled)
    set_nested(json_data, ["notifications_smtp_from_"], notifications_smtp_from_)
    set_nested(json_data, ["notifications_smtp_reply_to"], notifications_smtp_reply_to)
    set_nested(
        json_data,
        ["notifications_smtp_transport_host"],
        notifications_smtp_transport_host,
    )
    set_nested(
        json_data,
        ["notifications_smtp_transport_ignore_cert"],
        notifications_smtp_transport_ignore_cert,
    )
    set_nested(
        json_data,
        ["notifications_smtp_transport_password"],
        notifications_smtp_transport_password,
    )
    set_nested(
        json_data,
        ["notifications_smtp_transport_port"],
        notifications_smtp_transport_port,
    )
    set_nested(
        json_data,
        ["notifications_smtp_transport_secure"],
        notifications_smtp_transport_secure,
    )
    set_nested(
        json_data,
        ["notifications_smtp_transport_username"],
        notifications_smtp_transport_username,
    )
    set_nested(json_data, ["oauth_auto_launch"], oauth_auto_launch)
    set_nested(json_data, ["oauth_auto_register"], oauth_auto_register)
    set_nested(json_data, ["oauth_button_text"], oauth_button_text)
    set_nested(json_data, ["oauth_client_id"], oauth_client_id)
    set_nested(json_data, ["oauth_client_secret"], oauth_client_secret)
    set_nested(json_data, ["oauth_default_storage_quota"], oauth_default_storage_quota)
    set_nested(json_data, ["oauth_enabled"], oauth_enabled)
    set_nested(json_data, ["oauth_issuer_url"], oauth_issuer_url)
    set_nested(
        json_data, ["oauth_mobile_override_enabled"], oauth_mobile_override_enabled
    )
    set_nested(json_data, ["oauth_mobile_redirect_uri"], oauth_mobile_redirect_uri)
    set_nested(
        json_data, ["oauth_profile_signing_algorithm"], oauth_profile_signing_algorithm
    )
    set_nested(json_data, ["oauth_role_claim"], oauth_role_claim)
    set_nested(json_data, ["oauth_scope"], oauth_scope)
    set_nested(json_data, ["oauth_signing_algorithm"], oauth_signing_algorithm)
    set_nested(json_data, ["oauth_storage_label_claim"], oauth_storage_label_claim)
    set_nested(json_data, ["oauth_storage_quota_claim"], oauth_storage_quota_claim)
    set_nested(json_data, ["oauth_timeout"], oauth_timeout)
    set_nested(
        json_data,
        ["oauth_token_endpoint_auth_method"],
        oauth_token_endpoint_auth_method,
    )
    set_nested(json_data, ["password_login_enabled"], password_login_enabled)
    set_nested(json_data, ["reverse_geocoding_enabled"], reverse_geocoding_enabled)
    set_nested(json_data, ["server_external_domain"], server_external_domain)
    set_nested(json_data, ["server_login_page_message"], server_login_page_message)
    set_nested(json_data, ["server_public_users"], server_public_users)
    set_nested(json_data, ["storage_template_enabled"], storage_template_enabled)
    set_nested(
        json_data,
        ["storage_template_hash_verification_enabled"],
        storage_template_hash_verification_enabled,
    )
    set_nested(json_data, ["storage_template_template"], storage_template_template)
    set_nested(
        json_data,
        ["templates_email_album_invite_template"],
        templates_email_album_invite_template,
    )
    set_nested(
        json_data,
        ["templates_email_album_update_template"],
        templates_email_album_update_template,
    )
    set_nested(
        json_data,
        ["templates_email_welcome_template"],
        templates_email_welcome_template,
    )
    set_nested(json_data, ["theme_custom_css"], theme_custom_css)
    set_nested(json_data, ["trash_days"], trash_days)
    set_nested(json_data, ["trash_enabled"], trash_enabled)
    set_nested(json_data, ["user_delete_delay"], user_delete_delay)
    system_config_dto = SystemConfigDto.model_validate(json_data)
    kwargs["system_config_dto"] = system_config_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client, client.system_config, "update_config", ctx, **kwargs)
    print_response(result, ctx)
