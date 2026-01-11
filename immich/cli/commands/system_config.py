"""Generated CLI commands for System config tag (auto-generated, do not edit)."""

from __future__ import annotations

import json
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, print_response, run_command, set_nested

app = typer.Typer(help="""Endpoints to view, modify, and validate the system configuration settings.

Docs: https://api.immich.app/endpoints/system-config""", context_settings={'help_option_names': ['-h', '--help']})

@app.command("get-config")
def get_config(
    ctx: typer.Context,
) -> None:
    """Get system configuration

Docs: https://api.immich.app/endpoints/system-config/getConfig
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-config-defaults")
def get_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get system configuration defaults

Docs: https://api.immich.app/endpoints/system-config/getConfigDefaults
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_config_defaults', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("get-storage-template-options")
def get_storage_template_options(
    ctx: typer.Context,
) -> None:
    """Get storage template options

Docs: https://api.immich.app/endpoints/system-config/getStorageTemplateOptions
    """
    kwargs = {}
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'get_storage_template_options', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-config")
def update_config(
    ctx: typer.Context,
    json_str: str | None = typer.Option(None, "--json", help="Inline JSON request body"),
    backup_database_cron_expression: str = typer.Option(..., "--backup.database.cronExpression"),
    backup_database_enabled: bool = typer.Option(..., "--backup.database.enabled"),
    backup_database_keep_last_amount: float = typer.Option(..., "--backup.database.keepLastAmount"),
    ffmpeg_accel: str = typer.Option(..., "--ffmpeg.accel"),
    ffmpeg_accel_decode: bool = typer.Option(..., "--ffmpeg.accelDecode"),
    ffmpeg_accepted_audio_codecs: list[str] = typer.Option(..., "--ffmpeg.acceptedAudioCodecs", help="JSON string for ffmpeg.acceptedAudioCodecs"),
    ffmpeg_accepted_containers: list[str] = typer.Option(..., "--ffmpeg.acceptedContainers", help="JSON string for ffmpeg.acceptedContainers"),
    ffmpeg_accepted_video_codecs: list[str] = typer.Option(..., "--ffmpeg.acceptedVideoCodecs", help="JSON string for ffmpeg.acceptedVideoCodecs"),
    ffmpeg_bframes: int = typer.Option(..., "--ffmpeg.bframes"),
    ffmpeg_cq_mode: str = typer.Option(..., "--ffmpeg.cqMode"),
    ffmpeg_crf: int = typer.Option(..., "--ffmpeg.crf"),
    ffmpeg_gop_size: int = typer.Option(..., "--ffmpeg.gopSize"),
    ffmpeg_max_bitrate: str = typer.Option(..., "--ffmpeg.maxBitrate"),
    ffmpeg_preferred_hw_device: str = typer.Option(..., "--ffmpeg.preferredHwDevice"),
    ffmpeg_preset: str = typer.Option(..., "--ffmpeg.preset"),
    ffmpeg_refs: int = typer.Option(..., "--ffmpeg.refs"),
    ffmpeg_target_audio_codec: str = typer.Option(..., "--ffmpeg.targetAudioCodec"),
    ffmpeg_target_resolution: str = typer.Option(..., "--ffmpeg.targetResolution"),
    ffmpeg_target_video_codec: str = typer.Option(..., "--ffmpeg.targetVideoCodec"),
    ffmpeg_temporal_aq: bool = typer.Option(..., "--ffmpeg.temporalAQ"),
    ffmpeg_threads: int = typer.Option(..., "--ffmpeg.threads"),
    ffmpeg_tonemap: str = typer.Option(..., "--ffmpeg.tonemap"),
    ffmpeg_transcode: str = typer.Option(..., "--ffmpeg.transcode"),
    ffmpeg_two_pass: bool = typer.Option(..., "--ffmpeg.twoPass"),
    image_colorspace: str = typer.Option(..., "--image.colorspace"),
    image_extract_embedded: bool = typer.Option(..., "--image.extractEmbedded"),
    image_fullsize_enabled: bool = typer.Option(..., "--image.fullsize.enabled"),
    image_fullsize_format: str = typer.Option(..., "--image.fullsize.format"),
    image_fullsize_quality: int = typer.Option(..., "--image.fullsize.quality"),
    image_preview_format: str = typer.Option(..., "--image.preview.format"),
    image_preview_quality: int = typer.Option(..., "--image.preview.quality"),
    image_preview_size: int = typer.Option(..., "--image.preview.size"),
    image_thumbnail_format: str = typer.Option(..., "--image.thumbnail.format"),
    image_thumbnail_quality: int = typer.Option(..., "--image.thumbnail.quality"),
    image_thumbnail_size: int = typer.Option(..., "--image.thumbnail.size"),
    job_background_task_concurrency: int = typer.Option(..., "--job.backgroundTask.concurrency"),
    job_editor_concurrency: int = typer.Option(..., "--job.editor.concurrency"),
    job_face_detection_concurrency: int = typer.Option(..., "--job.faceDetection.concurrency"),
    job_library_concurrency: int = typer.Option(..., "--job.library.concurrency"),
    job_metadata_extraction_concurrency: int = typer.Option(..., "--job.metadataExtraction.concurrency"),
    job_migration_concurrency: int = typer.Option(..., "--job.migration.concurrency"),
    job_notifications_concurrency: int = typer.Option(..., "--job.notifications.concurrency"),
    job_ocr_concurrency: int = typer.Option(..., "--job.ocr.concurrency"),
    job_search_concurrency: int = typer.Option(..., "--job.search.concurrency"),
    job_sidecar_concurrency: int = typer.Option(..., "--job.sidecar.concurrency"),
    job_smart_search_concurrency: int = typer.Option(..., "--job.smartSearch.concurrency"),
    job_thumbnail_generation_concurrency: int = typer.Option(..., "--job.thumbnailGeneration.concurrency"),
    job_video_conversion_concurrency: int = typer.Option(..., "--job.videoConversion.concurrency"),
    job_workflow_concurrency: int = typer.Option(..., "--job.workflow.concurrency"),
    library_scan_cron_expression: str = typer.Option(..., "--library.scan.cronExpression"),
    library_scan_enabled: bool = typer.Option(..., "--library.scan.enabled"),
    library_watch_enabled: bool = typer.Option(..., "--library.watch.enabled"),
    logging_enabled: bool = typer.Option(..., "--logging.enabled"),
    logging_level: str = typer.Option(..., "--logging.level"),
    machine_learning_availability_checks_enabled: bool = typer.Option(..., "--machineLearning.availabilityChecks.enabled"),
    machine_learning_availability_checks_interval: float = typer.Option(..., "--machineLearning.availabilityChecks.interval"),
    machine_learning_availability_checks_timeout: float = typer.Option(..., "--machineLearning.availabilityChecks.timeout"),
    machine_learning_clip_enabled: bool = typer.Option(..., "--machineLearning.clip.enabled"),
    machine_learning_clip_model_name: str = typer.Option(..., "--machineLearning.clip.modelName"),
    machine_learning_duplicate_detection_enabled: bool = typer.Option(..., "--machineLearning.duplicateDetection.enabled"),
    machine_learning_duplicate_detection_max_distance: float = typer.Option(..., "--machineLearning.duplicateDetection.maxDistance"),
    machine_learning_enabled: bool = typer.Option(..., "--machineLearning.enabled"),
    machine_learning_facial_recognition_enabled: bool = typer.Option(..., "--machineLearning.facialRecognition.enabled"),
    machine_learning_facial_recognition_max_distance: float = typer.Option(..., "--machineLearning.facialRecognition.maxDistance"),
    machine_learning_facial_recognition_min_faces: int = typer.Option(..., "--machineLearning.facialRecognition.minFaces"),
    machine_learning_facial_recognition_min_score: float = typer.Option(..., "--machineLearning.facialRecognition.minScore"),
    machine_learning_facial_recognition_model_name: str = typer.Option(..., "--machineLearning.facialRecognition.modelName"),
    machine_learning_ocr_enabled: bool = typer.Option(..., "--machineLearning.ocr.enabled"),
    machine_learning_ocr_max_resolution: int = typer.Option(..., "--machineLearning.ocr.maxResolution"),
    machine_learning_ocr_min_detection_score: float = typer.Option(..., "--machineLearning.ocr.minDetectionScore"),
    machine_learning_ocr_min_recognition_score: float = typer.Option(..., "--machineLearning.ocr.minRecognitionScore"),
    machine_learning_ocr_model_name: str = typer.Option(..., "--machineLearning.ocr.modelName"),
    machine_learning_urls: list[str] = typer.Option(..., "--machineLearning.urls"),
    map_dark_style: str = typer.Option(..., "--map.darkStyle"),
    map_enabled: bool = typer.Option(..., "--map.enabled"),
    map_light_style: str = typer.Option(..., "--map.lightStyle"),
    metadata_faces_import_: bool = typer.Option(..., "--metadata.faces.import"),
    new_version_check_enabled: bool = typer.Option(..., "--newVersionCheck.enabled"),
    nightly_tasks_cluster_new_faces: bool = typer.Option(..., "--nightlyTasks.clusterNewFaces"),
    nightly_tasks_database_cleanup: bool = typer.Option(..., "--nightlyTasks.databaseCleanup"),
    nightly_tasks_generate_memories: bool = typer.Option(..., "--nightlyTasks.generateMemories"),
    nightly_tasks_missing_thumbnails: bool = typer.Option(..., "--nightlyTasks.missingThumbnails"),
    nightly_tasks_start_time: str = typer.Option(..., "--nightlyTasks.startTime"),
    nightly_tasks_sync_quota_usage: bool = typer.Option(..., "--nightlyTasks.syncQuotaUsage"),
    notifications_smtp_enabled: bool = typer.Option(..., "--notifications.smtp.enabled"),
    notifications_smtp_from_: str = typer.Option(..., "--notifications.smtp.from"),
    notifications_smtp_reply_to: str = typer.Option(..., "--notifications.smtp.replyTo"),
    notifications_smtp_transport_host: str = typer.Option(..., "--notifications.smtp.transport.host"),
    notifications_smtp_transport_ignore_cert: bool = typer.Option(..., "--notifications.smtp.transport.ignoreCert"),
    notifications_smtp_transport_password: str = typer.Option(..., "--notifications.smtp.transport.password"),
    notifications_smtp_transport_port: float = typer.Option(..., "--notifications.smtp.transport.port"),
    notifications_smtp_transport_secure: bool = typer.Option(..., "--notifications.smtp.transport.secure"),
    notifications_smtp_transport_username: str = typer.Option(..., "--notifications.smtp.transport.username"),
    oauth_auto_launch: bool = typer.Option(..., "--oauth.autoLaunch"),
    oauth_auto_register: bool = typer.Option(..., "--oauth.autoRegister"),
    oauth_button_text: str = typer.Option(..., "--oauth.buttonText"),
    oauth_client_id: str = typer.Option(..., "--oauth.clientId"),
    oauth_client_secret: str = typer.Option(..., "--oauth.clientSecret"),
    oauth_default_storage_quota: int = typer.Option(..., "--oauth.defaultStorageQuota"),
    oauth_enabled: bool = typer.Option(..., "--oauth.enabled"),
    oauth_issuer_url: str = typer.Option(..., "--oauth.issuerUrl"),
    oauth_mobile_override_enabled: bool = typer.Option(..., "--oauth.mobileOverrideEnabled"),
    oauth_mobile_redirect_uri: str = typer.Option(..., "--oauth.mobileRedirectUri"),
    oauth_profile_signing_algorithm: str = typer.Option(..., "--oauth.profileSigningAlgorithm"),
    oauth_role_claim: str = typer.Option(..., "--oauth.roleClaim"),
    oauth_scope: str = typer.Option(..., "--oauth.scope"),
    oauth_signing_algorithm: str = typer.Option(..., "--oauth.signingAlgorithm"),
    oauth_storage_label_claim: str = typer.Option(..., "--oauth.storageLabelClaim"),
    oauth_storage_quota_claim: str = typer.Option(..., "--oauth.storageQuotaClaim"),
    oauth_timeout: int = typer.Option(..., "--oauth.timeout"),
    oauth_token_endpoint_auth_method: str = typer.Option(..., "--oauth.tokenEndpointAuthMethod"),
    password_login_enabled: bool = typer.Option(..., "--passwordLogin.enabled"),
    reverse_geocoding_enabled: bool = typer.Option(..., "--reverseGeocoding.enabled"),
    server_external_domain: str = typer.Option(..., "--server.externalDomain"),
    server_login_page_message: str = typer.Option(..., "--server.loginPageMessage"),
    server_public_users: bool = typer.Option(..., "--server.publicUsers"),
    storage_template_enabled: bool = typer.Option(..., "--storageTemplate.enabled"),
    storage_template_hash_verification_enabled: bool = typer.Option(..., "--storageTemplate.hashVerificationEnabled"),
    storage_template_template: str = typer.Option(..., "--storageTemplate.template"),
    templates_email_album_invite_template: str = typer.Option(..., "--templates.email.albumInviteTemplate"),
    templates_email_album_update_template: str = typer.Option(..., "--templates.email.albumUpdateTemplate"),
    templates_email_welcome_template: str = typer.Option(..., "--templates.email.welcomeTemplate"),
    theme_custom_css: str = typer.Option(..., "--theme.customCss"),
    trash_days: int = typer.Option(..., "--trash.days"),
    trash_enabled: bool = typer.Option(..., "--trash.enabled"),
    user_delete_delay: int = typer.Option(..., "--user.deleteDelay"),
) -> None:
    """Update system configuration

Docs: https://api.immich.app/endpoints/system-config/updateConfig
    """
    kwargs = {}
    # Check mutual exclusion between --json and dotted flags
    has_json = json_str is not None
    has_flags = any([backup_database_cron_expression, backup_database_enabled, backup_database_keep_last_amount, ffmpeg_accel, ffmpeg_accel_decode, ffmpeg_accepted_audio_codecs, ffmpeg_accepted_containers, ffmpeg_accepted_video_codecs, ffmpeg_bframes, ffmpeg_cq_mode, ffmpeg_crf, ffmpeg_gop_size, ffmpeg_max_bitrate, ffmpeg_preferred_hw_device, ffmpeg_preset, ffmpeg_refs, ffmpeg_target_audio_codec, ffmpeg_target_resolution, ffmpeg_target_video_codec, ffmpeg_temporal_aq, ffmpeg_threads, ffmpeg_tonemap, ffmpeg_transcode, ffmpeg_two_pass, image_colorspace, image_extract_embedded, image_fullsize_enabled, image_fullsize_format, image_fullsize_quality, image_preview_format, image_preview_quality, image_preview_size, image_thumbnail_format, image_thumbnail_quality, image_thumbnail_size, job_background_task_concurrency, job_editor_concurrency, job_face_detection_concurrency, job_library_concurrency, job_metadata_extraction_concurrency, job_migration_concurrency, job_notifications_concurrency, job_ocr_concurrency, job_search_concurrency, job_sidecar_concurrency, job_smart_search_concurrency, job_thumbnail_generation_concurrency, job_video_conversion_concurrency, job_workflow_concurrency, library_scan_cron_expression, library_scan_enabled, library_watch_enabled, logging_enabled, logging_level, machine_learning_availability_checks_enabled, machine_learning_availability_checks_interval, machine_learning_availability_checks_timeout, machine_learning_clip_enabled, machine_learning_clip_model_name, machine_learning_duplicate_detection_enabled, machine_learning_duplicate_detection_max_distance, machine_learning_enabled, machine_learning_facial_recognition_enabled, machine_learning_facial_recognition_max_distance, machine_learning_facial_recognition_min_faces, machine_learning_facial_recognition_min_score, machine_learning_facial_recognition_model_name, machine_learning_ocr_enabled, machine_learning_ocr_max_resolution, machine_learning_ocr_min_detection_score, machine_learning_ocr_min_recognition_score, machine_learning_ocr_model_name, machine_learning_urls, map_dark_style, map_enabled, map_light_style, metadata_faces_import_, new_version_check_enabled, nightly_tasks_cluster_new_faces, nightly_tasks_database_cleanup, nightly_tasks_generate_memories, nightly_tasks_missing_thumbnails, nightly_tasks_start_time, nightly_tasks_sync_quota_usage, notifications_smtp_enabled, notifications_smtp_from_, notifications_smtp_reply_to, notifications_smtp_transport_host, notifications_smtp_transport_ignore_cert, notifications_smtp_transport_password, notifications_smtp_transport_port, notifications_smtp_transport_secure, notifications_smtp_transport_username, oauth_auto_launch, oauth_auto_register, oauth_button_text, oauth_client_id, oauth_client_secret, oauth_default_storage_quota, oauth_enabled, oauth_issuer_url, oauth_mobile_override_enabled, oauth_mobile_redirect_uri, oauth_profile_signing_algorithm, oauth_role_claim, oauth_scope, oauth_signing_algorithm, oauth_storage_label_claim, oauth_storage_quota_claim, oauth_timeout, oauth_token_endpoint_auth_method, password_login_enabled, reverse_geocoding_enabled, server_external_domain, server_login_page_message, server_public_users, storage_template_enabled, storage_template_hash_verification_enabled, storage_template_template, templates_email_album_invite_template, templates_email_album_update_template, templates_email_welcome_template, theme_custom_css, trash_days, trash_enabled, user_delete_delay])
    if has_json and has_flags:
        raise SystemExit("Error: Cannot use both --json and dotted body flags together. Use one or the other.")
    if not has_json and not has_flags:
        raise SystemExit("Error: Request body is required. Provide --json or use dotted body flags.")
    if json_str is not None:
        json_data = json.loads(json_str)
        from immich.client.models.system_config_dto import SystemConfigDto
        system_config_dto = deserialize_request_body(json_data, SystemConfigDto)
        kwargs['system_config_dto'] = system_config_dto
    elif any([
        backup_database_cron_expression,
        backup_database_enabled,
        backup_database_keep_last_amount,
        ffmpeg_accel,
        ffmpeg_accel_decode,
        ffmpeg_accepted_audio_codecs,
        ffmpeg_accepted_containers,
        ffmpeg_accepted_video_codecs,
        ffmpeg_bframes,
        ffmpeg_cq_mode,
        ffmpeg_crf,
        ffmpeg_gop_size,
        ffmpeg_max_bitrate,
        ffmpeg_preferred_hw_device,
        ffmpeg_preset,
        ffmpeg_refs,
        ffmpeg_target_audio_codec,
        ffmpeg_target_resolution,
        ffmpeg_target_video_codec,
        ffmpeg_temporal_aq,
        ffmpeg_threads,
        ffmpeg_tonemap,
        ffmpeg_transcode,
        ffmpeg_two_pass,
        image_colorspace,
        image_extract_embedded,
        image_fullsize_enabled,
        image_fullsize_format,
        image_fullsize_quality,
        image_preview_format,
        image_preview_quality,
        image_preview_size,
        image_thumbnail_format,
        image_thumbnail_quality,
        image_thumbnail_size,
        job_background_task_concurrency,
        job_editor_concurrency,
        job_face_detection_concurrency,
        job_library_concurrency,
        job_metadata_extraction_concurrency,
        job_migration_concurrency,
        job_notifications_concurrency,
        job_ocr_concurrency,
        job_search_concurrency,
        job_sidecar_concurrency,
        job_smart_search_concurrency,
        job_thumbnail_generation_concurrency,
        job_video_conversion_concurrency,
        job_workflow_concurrency,
        library_scan_cron_expression,
        library_scan_enabled,
        library_watch_enabled,
        logging_enabled,
        logging_level,
        machine_learning_availability_checks_enabled,
        machine_learning_availability_checks_interval,
        machine_learning_availability_checks_timeout,
        machine_learning_clip_enabled,
        machine_learning_clip_model_name,
        machine_learning_duplicate_detection_enabled,
        machine_learning_duplicate_detection_max_distance,
        machine_learning_enabled,
        machine_learning_facial_recognition_enabled,
        machine_learning_facial_recognition_max_distance,
        machine_learning_facial_recognition_min_faces,
        machine_learning_facial_recognition_min_score,
        machine_learning_facial_recognition_model_name,
        machine_learning_ocr_enabled,
        machine_learning_ocr_max_resolution,
        machine_learning_ocr_min_detection_score,
        machine_learning_ocr_min_recognition_score,
        machine_learning_ocr_model_name,
        machine_learning_urls,
        map_dark_style,
        map_enabled,
        map_light_style,
        metadata_faces_import_,
        new_version_check_enabled,
        nightly_tasks_cluster_new_faces,
        nightly_tasks_database_cleanup,
        nightly_tasks_generate_memories,
        nightly_tasks_missing_thumbnails,
        nightly_tasks_start_time,
        nightly_tasks_sync_quota_usage,
        notifications_smtp_enabled,
        notifications_smtp_from_,
        notifications_smtp_reply_to,
        notifications_smtp_transport_host,
        notifications_smtp_transport_ignore_cert,
        notifications_smtp_transport_password,
        notifications_smtp_transport_port,
        notifications_smtp_transport_secure,
        notifications_smtp_transport_username,
        oauth_auto_launch,
        oauth_auto_register,
        oauth_button_text,
        oauth_client_id,
        oauth_client_secret,
        oauth_default_storage_quota,
        oauth_enabled,
        oauth_issuer_url,
        oauth_mobile_override_enabled,
        oauth_mobile_redirect_uri,
        oauth_profile_signing_algorithm,
        oauth_role_claim,
        oauth_scope,
        oauth_signing_algorithm,
        oauth_storage_label_claim,
        oauth_storage_quota_claim,
        oauth_timeout,
        oauth_token_endpoint_auth_method,
        password_login_enabled,
        reverse_geocoding_enabled,
        server_external_domain,
        server_login_page_message,
        server_public_users,
        storage_template_enabled,
        storage_template_hash_verification_enabled,
        storage_template_template,
        templates_email_album_invite_template,
        templates_email_album_update_template,
        templates_email_welcome_template,
        theme_custom_css,
        trash_days,
        trash_enabled,
        user_delete_delay,
    ]):
        # Build body from dotted flags
        json_data = {}
        if backup_database_cron_expression is None:
            raise SystemExit("Error: --backup.database.cronExpression is required")
        set_nested(json_data, ['backup', 'database', 'cronExpression'], backup_database_cron_expression)
        if backup_database_enabled is None:
            raise SystemExit("Error: --backup.database.enabled is required")
        set_nested(json_data, ['backup', 'database', 'enabled'], backup_database_enabled)
        if backup_database_keep_last_amount is None:
            raise SystemExit("Error: --backup.database.keepLastAmount is required")
        set_nested(json_data, ['backup', 'database', 'keepLastAmount'], backup_database_keep_last_amount)
        if ffmpeg_accel is None:
            raise SystemExit("Error: --ffmpeg.accel is required")
        set_nested(json_data, ['ffmpeg', 'accel'], ffmpeg_accel)
        if ffmpeg_accel_decode is None:
            raise SystemExit("Error: --ffmpeg.accelDecode is required")
        set_nested(json_data, ['ffmpeg', 'accelDecode'], ffmpeg_accel_decode)
        if ffmpeg_accepted_audio_codecs is None:
            raise SystemExit("Error: --ffmpeg.acceptedAudioCodecs is required")
        value_ffmpeg_accepted_audio_codecs = json.loads(ffmpeg_accepted_audio_codecs)
        set_nested(json_data, ['ffmpeg', 'acceptedAudioCodecs'], value_ffmpeg_accepted_audio_codecs)
        if ffmpeg_accepted_containers is None:
            raise SystemExit("Error: --ffmpeg.acceptedContainers is required")
        value_ffmpeg_accepted_containers = json.loads(ffmpeg_accepted_containers)
        set_nested(json_data, ['ffmpeg', 'acceptedContainers'], value_ffmpeg_accepted_containers)
        if ffmpeg_accepted_video_codecs is None:
            raise SystemExit("Error: --ffmpeg.acceptedVideoCodecs is required")
        value_ffmpeg_accepted_video_codecs = json.loads(ffmpeg_accepted_video_codecs)
        set_nested(json_data, ['ffmpeg', 'acceptedVideoCodecs'], value_ffmpeg_accepted_video_codecs)
        if ffmpeg_bframes is None:
            raise SystemExit("Error: --ffmpeg.bframes is required")
        set_nested(json_data, ['ffmpeg', 'bframes'], ffmpeg_bframes)
        if ffmpeg_cq_mode is None:
            raise SystemExit("Error: --ffmpeg.cqMode is required")
        set_nested(json_data, ['ffmpeg', 'cqMode'], ffmpeg_cq_mode)
        if ffmpeg_crf is None:
            raise SystemExit("Error: --ffmpeg.crf is required")
        set_nested(json_data, ['ffmpeg', 'crf'], ffmpeg_crf)
        if ffmpeg_gop_size is None:
            raise SystemExit("Error: --ffmpeg.gopSize is required")
        set_nested(json_data, ['ffmpeg', 'gopSize'], ffmpeg_gop_size)
        if ffmpeg_max_bitrate is None:
            raise SystemExit("Error: --ffmpeg.maxBitrate is required")
        set_nested(json_data, ['ffmpeg', 'maxBitrate'], ffmpeg_max_bitrate)
        if ffmpeg_preferred_hw_device is None:
            raise SystemExit("Error: --ffmpeg.preferredHwDevice is required")
        set_nested(json_data, ['ffmpeg', 'preferredHwDevice'], ffmpeg_preferred_hw_device)
        if ffmpeg_preset is None:
            raise SystemExit("Error: --ffmpeg.preset is required")
        set_nested(json_data, ['ffmpeg', 'preset'], ffmpeg_preset)
        if ffmpeg_refs is None:
            raise SystemExit("Error: --ffmpeg.refs is required")
        set_nested(json_data, ['ffmpeg', 'refs'], ffmpeg_refs)
        if ffmpeg_target_audio_codec is None:
            raise SystemExit("Error: --ffmpeg.targetAudioCodec is required")
        set_nested(json_data, ['ffmpeg', 'targetAudioCodec'], ffmpeg_target_audio_codec)
        if ffmpeg_target_resolution is None:
            raise SystemExit("Error: --ffmpeg.targetResolution is required")
        set_nested(json_data, ['ffmpeg', 'targetResolution'], ffmpeg_target_resolution)
        if ffmpeg_target_video_codec is None:
            raise SystemExit("Error: --ffmpeg.targetVideoCodec is required")
        set_nested(json_data, ['ffmpeg', 'targetVideoCodec'], ffmpeg_target_video_codec)
        if ffmpeg_temporal_aq is None:
            raise SystemExit("Error: --ffmpeg.temporalAQ is required")
        set_nested(json_data, ['ffmpeg', 'temporalAQ'], ffmpeg_temporal_aq)
        if ffmpeg_threads is None:
            raise SystemExit("Error: --ffmpeg.threads is required")
        set_nested(json_data, ['ffmpeg', 'threads'], ffmpeg_threads)
        if ffmpeg_tonemap is None:
            raise SystemExit("Error: --ffmpeg.tonemap is required")
        set_nested(json_data, ['ffmpeg', 'tonemap'], ffmpeg_tonemap)
        if ffmpeg_transcode is None:
            raise SystemExit("Error: --ffmpeg.transcode is required")
        set_nested(json_data, ['ffmpeg', 'transcode'], ffmpeg_transcode)
        if ffmpeg_two_pass is None:
            raise SystemExit("Error: --ffmpeg.twoPass is required")
        set_nested(json_data, ['ffmpeg', 'twoPass'], ffmpeg_two_pass)
        if image_colorspace is None:
            raise SystemExit("Error: --image.colorspace is required")
        set_nested(json_data, ['image', 'colorspace'], image_colorspace)
        if image_extract_embedded is None:
            raise SystemExit("Error: --image.extractEmbedded is required")
        set_nested(json_data, ['image', 'extractEmbedded'], image_extract_embedded)
        if image_fullsize_enabled is None:
            raise SystemExit("Error: --image.fullsize.enabled is required")
        set_nested(json_data, ['image', 'fullsize', 'enabled'], image_fullsize_enabled)
        if image_fullsize_format is None:
            raise SystemExit("Error: --image.fullsize.format is required")
        set_nested(json_data, ['image', 'fullsize', 'format'], image_fullsize_format)
        if image_fullsize_quality is None:
            raise SystemExit("Error: --image.fullsize.quality is required")
        set_nested(json_data, ['image', 'fullsize', 'quality'], image_fullsize_quality)
        if image_preview_format is None:
            raise SystemExit("Error: --image.preview.format is required")
        set_nested(json_data, ['image', 'preview', 'format'], image_preview_format)
        if image_preview_quality is None:
            raise SystemExit("Error: --image.preview.quality is required")
        set_nested(json_data, ['image', 'preview', 'quality'], image_preview_quality)
        if image_preview_size is None:
            raise SystemExit("Error: --image.preview.size is required")
        set_nested(json_data, ['image', 'preview', 'size'], image_preview_size)
        if image_thumbnail_format is None:
            raise SystemExit("Error: --image.thumbnail.format is required")
        set_nested(json_data, ['image', 'thumbnail', 'format'], image_thumbnail_format)
        if image_thumbnail_quality is None:
            raise SystemExit("Error: --image.thumbnail.quality is required")
        set_nested(json_data, ['image', 'thumbnail', 'quality'], image_thumbnail_quality)
        if image_thumbnail_size is None:
            raise SystemExit("Error: --image.thumbnail.size is required")
        set_nested(json_data, ['image', 'thumbnail', 'size'], image_thumbnail_size)
        if job_background_task_concurrency is None:
            raise SystemExit("Error: --job.backgroundTask.concurrency is required")
        set_nested(json_data, ['job', 'backgroundTask', 'concurrency'], job_background_task_concurrency)
        if job_editor_concurrency is None:
            raise SystemExit("Error: --job.editor.concurrency is required")
        set_nested(json_data, ['job', 'editor', 'concurrency'], job_editor_concurrency)
        if job_face_detection_concurrency is None:
            raise SystemExit("Error: --job.faceDetection.concurrency is required")
        set_nested(json_data, ['job', 'faceDetection', 'concurrency'], job_face_detection_concurrency)
        if job_library_concurrency is None:
            raise SystemExit("Error: --job.library.concurrency is required")
        set_nested(json_data, ['job', 'library', 'concurrency'], job_library_concurrency)
        if job_metadata_extraction_concurrency is None:
            raise SystemExit("Error: --job.metadataExtraction.concurrency is required")
        set_nested(json_data, ['job', 'metadataExtraction', 'concurrency'], job_metadata_extraction_concurrency)
        if job_migration_concurrency is None:
            raise SystemExit("Error: --job.migration.concurrency is required")
        set_nested(json_data, ['job', 'migration', 'concurrency'], job_migration_concurrency)
        if job_notifications_concurrency is None:
            raise SystemExit("Error: --job.notifications.concurrency is required")
        set_nested(json_data, ['job', 'notifications', 'concurrency'], job_notifications_concurrency)
        if job_ocr_concurrency is None:
            raise SystemExit("Error: --job.ocr.concurrency is required")
        set_nested(json_data, ['job', 'ocr', 'concurrency'], job_ocr_concurrency)
        if job_search_concurrency is None:
            raise SystemExit("Error: --job.search.concurrency is required")
        set_nested(json_data, ['job', 'search', 'concurrency'], job_search_concurrency)
        if job_sidecar_concurrency is None:
            raise SystemExit("Error: --job.sidecar.concurrency is required")
        set_nested(json_data, ['job', 'sidecar', 'concurrency'], job_sidecar_concurrency)
        if job_smart_search_concurrency is None:
            raise SystemExit("Error: --job.smartSearch.concurrency is required")
        set_nested(json_data, ['job', 'smartSearch', 'concurrency'], job_smart_search_concurrency)
        if job_thumbnail_generation_concurrency is None:
            raise SystemExit("Error: --job.thumbnailGeneration.concurrency is required")
        set_nested(json_data, ['job', 'thumbnailGeneration', 'concurrency'], job_thumbnail_generation_concurrency)
        if job_video_conversion_concurrency is None:
            raise SystemExit("Error: --job.videoConversion.concurrency is required")
        set_nested(json_data, ['job', 'videoConversion', 'concurrency'], job_video_conversion_concurrency)
        if job_workflow_concurrency is None:
            raise SystemExit("Error: --job.workflow.concurrency is required")
        set_nested(json_data, ['job', 'workflow', 'concurrency'], job_workflow_concurrency)
        if library_scan_cron_expression is None:
            raise SystemExit("Error: --library.scan.cronExpression is required")
        set_nested(json_data, ['library', 'scan', 'cronExpression'], library_scan_cron_expression)
        if library_scan_enabled is None:
            raise SystemExit("Error: --library.scan.enabled is required")
        set_nested(json_data, ['library', 'scan', 'enabled'], library_scan_enabled)
        if library_watch_enabled is None:
            raise SystemExit("Error: --library.watch.enabled is required")
        set_nested(json_data, ['library', 'watch', 'enabled'], library_watch_enabled)
        if logging_enabled is None:
            raise SystemExit("Error: --logging.enabled is required")
        set_nested(json_data, ['logging', 'enabled'], logging_enabled)
        if logging_level is None:
            raise SystemExit("Error: --logging.level is required")
        set_nested(json_data, ['logging', 'level'], logging_level)
        if machine_learning_availability_checks_enabled is None:
            raise SystemExit("Error: --machineLearning.availabilityChecks.enabled is required")
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'enabled'], machine_learning_availability_checks_enabled)
        if machine_learning_availability_checks_interval is None:
            raise SystemExit("Error: --machineLearning.availabilityChecks.interval is required")
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'interval'], machine_learning_availability_checks_interval)
        if machine_learning_availability_checks_timeout is None:
            raise SystemExit("Error: --machineLearning.availabilityChecks.timeout is required")
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'timeout'], machine_learning_availability_checks_timeout)
        if machine_learning_clip_enabled is None:
            raise SystemExit("Error: --machineLearning.clip.enabled is required")
        set_nested(json_data, ['machineLearning', 'clip', 'enabled'], machine_learning_clip_enabled)
        if machine_learning_clip_model_name is None:
            raise SystemExit("Error: --machineLearning.clip.modelName is required")
        set_nested(json_data, ['machineLearning', 'clip', 'modelName'], machine_learning_clip_model_name)
        if machine_learning_duplicate_detection_enabled is None:
            raise SystemExit("Error: --machineLearning.duplicateDetection.enabled is required")
        set_nested(json_data, ['machineLearning', 'duplicateDetection', 'enabled'], machine_learning_duplicate_detection_enabled)
        if machine_learning_duplicate_detection_max_distance is None:
            raise SystemExit("Error: --machineLearning.duplicateDetection.maxDistance is required")
        set_nested(json_data, ['machineLearning', 'duplicateDetection', 'maxDistance'], machine_learning_duplicate_detection_max_distance)
        if machine_learning_enabled is None:
            raise SystemExit("Error: --machineLearning.enabled is required")
        set_nested(json_data, ['machineLearning', 'enabled'], machine_learning_enabled)
        if machine_learning_facial_recognition_enabled is None:
            raise SystemExit("Error: --machineLearning.facialRecognition.enabled is required")
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'enabled'], machine_learning_facial_recognition_enabled)
        if machine_learning_facial_recognition_max_distance is None:
            raise SystemExit("Error: --machineLearning.facialRecognition.maxDistance is required")
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'maxDistance'], machine_learning_facial_recognition_max_distance)
        if machine_learning_facial_recognition_min_faces is None:
            raise SystemExit("Error: --machineLearning.facialRecognition.minFaces is required")
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'minFaces'], machine_learning_facial_recognition_min_faces)
        if machine_learning_facial_recognition_min_score is None:
            raise SystemExit("Error: --machineLearning.facialRecognition.minScore is required")
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'minScore'], machine_learning_facial_recognition_min_score)
        if machine_learning_facial_recognition_model_name is None:
            raise SystemExit("Error: --machineLearning.facialRecognition.modelName is required")
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'modelName'], machine_learning_facial_recognition_model_name)
        if machine_learning_ocr_enabled is None:
            raise SystemExit("Error: --machineLearning.ocr.enabled is required")
        set_nested(json_data, ['machineLearning', 'ocr', 'enabled'], machine_learning_ocr_enabled)
        if machine_learning_ocr_max_resolution is None:
            raise SystemExit("Error: --machineLearning.ocr.maxResolution is required")
        set_nested(json_data, ['machineLearning', 'ocr', 'maxResolution'], machine_learning_ocr_max_resolution)
        if machine_learning_ocr_min_detection_score is None:
            raise SystemExit("Error: --machineLearning.ocr.minDetectionScore is required")
        set_nested(json_data, ['machineLearning', 'ocr', 'minDetectionScore'], machine_learning_ocr_min_detection_score)
        if machine_learning_ocr_min_recognition_score is None:
            raise SystemExit("Error: --machineLearning.ocr.minRecognitionScore is required")
        set_nested(json_data, ['machineLearning', 'ocr', 'minRecognitionScore'], machine_learning_ocr_min_recognition_score)
        if machine_learning_ocr_model_name is None:
            raise SystemExit("Error: --machineLearning.ocr.modelName is required")
        set_nested(json_data, ['machineLearning', 'ocr', 'modelName'], machine_learning_ocr_model_name)
        if machine_learning_urls is None:
            raise SystemExit("Error: --machineLearning.urls is required")
        set_nested(json_data, ['machineLearning', 'urls'], machine_learning_urls)
        if map_dark_style is None:
            raise SystemExit("Error: --map.darkStyle is required")
        set_nested(json_data, ['map', 'darkStyle'], map_dark_style)
        if map_enabled is None:
            raise SystemExit("Error: --map.enabled is required")
        set_nested(json_data, ['map', 'enabled'], map_enabled)
        if map_light_style is None:
            raise SystemExit("Error: --map.lightStyle is required")
        set_nested(json_data, ['map', 'lightStyle'], map_light_style)
        if metadata_faces_import_ is None:
            raise SystemExit("Error: --metadata.faces.import is required")
        set_nested(json_data, ['metadata', 'faces', 'import'], metadata_faces_import_)
        if new_version_check_enabled is None:
            raise SystemExit("Error: --newVersionCheck.enabled is required")
        set_nested(json_data, ['newVersionCheck', 'enabled'], new_version_check_enabled)
        if nightly_tasks_cluster_new_faces is None:
            raise SystemExit("Error: --nightlyTasks.clusterNewFaces is required")
        set_nested(json_data, ['nightlyTasks', 'clusterNewFaces'], nightly_tasks_cluster_new_faces)
        if nightly_tasks_database_cleanup is None:
            raise SystemExit("Error: --nightlyTasks.databaseCleanup is required")
        set_nested(json_data, ['nightlyTasks', 'databaseCleanup'], nightly_tasks_database_cleanup)
        if nightly_tasks_generate_memories is None:
            raise SystemExit("Error: --nightlyTasks.generateMemories is required")
        set_nested(json_data, ['nightlyTasks', 'generateMemories'], nightly_tasks_generate_memories)
        if nightly_tasks_missing_thumbnails is None:
            raise SystemExit("Error: --nightlyTasks.missingThumbnails is required")
        set_nested(json_data, ['nightlyTasks', 'missingThumbnails'], nightly_tasks_missing_thumbnails)
        if nightly_tasks_start_time is None:
            raise SystemExit("Error: --nightlyTasks.startTime is required")
        set_nested(json_data, ['nightlyTasks', 'startTime'], nightly_tasks_start_time)
        if nightly_tasks_sync_quota_usage is None:
            raise SystemExit("Error: --nightlyTasks.syncQuotaUsage is required")
        set_nested(json_data, ['nightlyTasks', 'syncQuotaUsage'], nightly_tasks_sync_quota_usage)
        if notifications_smtp_enabled is None:
            raise SystemExit("Error: --notifications.smtp.enabled is required")
        set_nested(json_data, ['notifications', 'smtp', 'enabled'], notifications_smtp_enabled)
        if notifications_smtp_from_ is None:
            raise SystemExit("Error: --notifications.smtp.from is required")
        set_nested(json_data, ['notifications', 'smtp', 'from'], notifications_smtp_from_)
        if notifications_smtp_reply_to is None:
            raise SystemExit("Error: --notifications.smtp.replyTo is required")
        set_nested(json_data, ['notifications', 'smtp', 'replyTo'], notifications_smtp_reply_to)
        if notifications_smtp_transport_host is None:
            raise SystemExit("Error: --notifications.smtp.transport.host is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'host'], notifications_smtp_transport_host)
        if notifications_smtp_transport_ignore_cert is None:
            raise SystemExit("Error: --notifications.smtp.transport.ignoreCert is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'ignoreCert'], notifications_smtp_transport_ignore_cert)
        if notifications_smtp_transport_password is None:
            raise SystemExit("Error: --notifications.smtp.transport.password is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'password'], notifications_smtp_transport_password)
        if notifications_smtp_transport_port is None:
            raise SystemExit("Error: --notifications.smtp.transport.port is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'port'], notifications_smtp_transport_port)
        if notifications_smtp_transport_secure is None:
            raise SystemExit("Error: --notifications.smtp.transport.secure is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'secure'], notifications_smtp_transport_secure)
        if notifications_smtp_transport_username is None:
            raise SystemExit("Error: --notifications.smtp.transport.username is required")
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'username'], notifications_smtp_transport_username)
        if oauth_auto_launch is None:
            raise SystemExit("Error: --oauth.autoLaunch is required")
        set_nested(json_data, ['oauth', 'autoLaunch'], oauth_auto_launch)
        if oauth_auto_register is None:
            raise SystemExit("Error: --oauth.autoRegister is required")
        set_nested(json_data, ['oauth', 'autoRegister'], oauth_auto_register)
        if oauth_button_text is None:
            raise SystemExit("Error: --oauth.buttonText is required")
        set_nested(json_data, ['oauth', 'buttonText'], oauth_button_text)
        if oauth_client_id is None:
            raise SystemExit("Error: --oauth.clientId is required")
        set_nested(json_data, ['oauth', 'clientId'], oauth_client_id)
        if oauth_client_secret is None:
            raise SystemExit("Error: --oauth.clientSecret is required")
        set_nested(json_data, ['oauth', 'clientSecret'], oauth_client_secret)
        if oauth_default_storage_quota is None:
            raise SystemExit("Error: --oauth.defaultStorageQuota is required")
        set_nested(json_data, ['oauth', 'defaultStorageQuota'], oauth_default_storage_quota)
        if oauth_enabled is None:
            raise SystemExit("Error: --oauth.enabled is required")
        set_nested(json_data, ['oauth', 'enabled'], oauth_enabled)
        if oauth_issuer_url is None:
            raise SystemExit("Error: --oauth.issuerUrl is required")
        set_nested(json_data, ['oauth', 'issuerUrl'], oauth_issuer_url)
        if oauth_mobile_override_enabled is None:
            raise SystemExit("Error: --oauth.mobileOverrideEnabled is required")
        set_nested(json_data, ['oauth', 'mobileOverrideEnabled'], oauth_mobile_override_enabled)
        if oauth_mobile_redirect_uri is None:
            raise SystemExit("Error: --oauth.mobileRedirectUri is required")
        set_nested(json_data, ['oauth', 'mobileRedirectUri'], oauth_mobile_redirect_uri)
        if oauth_profile_signing_algorithm is None:
            raise SystemExit("Error: --oauth.profileSigningAlgorithm is required")
        set_nested(json_data, ['oauth', 'profileSigningAlgorithm'], oauth_profile_signing_algorithm)
        if oauth_role_claim is None:
            raise SystemExit("Error: --oauth.roleClaim is required")
        set_nested(json_data, ['oauth', 'roleClaim'], oauth_role_claim)
        if oauth_scope is None:
            raise SystemExit("Error: --oauth.scope is required")
        set_nested(json_data, ['oauth', 'scope'], oauth_scope)
        if oauth_signing_algorithm is None:
            raise SystemExit("Error: --oauth.signingAlgorithm is required")
        set_nested(json_data, ['oauth', 'signingAlgorithm'], oauth_signing_algorithm)
        if oauth_storage_label_claim is None:
            raise SystemExit("Error: --oauth.storageLabelClaim is required")
        set_nested(json_data, ['oauth', 'storageLabelClaim'], oauth_storage_label_claim)
        if oauth_storage_quota_claim is None:
            raise SystemExit("Error: --oauth.storageQuotaClaim is required")
        set_nested(json_data, ['oauth', 'storageQuotaClaim'], oauth_storage_quota_claim)
        if oauth_timeout is None:
            raise SystemExit("Error: --oauth.timeout is required")
        set_nested(json_data, ['oauth', 'timeout'], oauth_timeout)
        if oauth_token_endpoint_auth_method is None:
            raise SystemExit("Error: --oauth.tokenEndpointAuthMethod is required")
        set_nested(json_data, ['oauth', 'tokenEndpointAuthMethod'], oauth_token_endpoint_auth_method)
        if password_login_enabled is None:
            raise SystemExit("Error: --passwordLogin.enabled is required")
        set_nested(json_data, ['passwordLogin', 'enabled'], password_login_enabled)
        if reverse_geocoding_enabled is None:
            raise SystemExit("Error: --reverseGeocoding.enabled is required")
        set_nested(json_data, ['reverseGeocoding', 'enabled'], reverse_geocoding_enabled)
        if server_external_domain is None:
            raise SystemExit("Error: --server.externalDomain is required")
        set_nested(json_data, ['server', 'externalDomain'], server_external_domain)
        if server_login_page_message is None:
            raise SystemExit("Error: --server.loginPageMessage is required")
        set_nested(json_data, ['server', 'loginPageMessage'], server_login_page_message)
        if server_public_users is None:
            raise SystemExit("Error: --server.publicUsers is required")
        set_nested(json_data, ['server', 'publicUsers'], server_public_users)
        if storage_template_enabled is None:
            raise SystemExit("Error: --storageTemplate.enabled is required")
        set_nested(json_data, ['storageTemplate', 'enabled'], storage_template_enabled)
        if storage_template_hash_verification_enabled is None:
            raise SystemExit("Error: --storageTemplate.hashVerificationEnabled is required")
        set_nested(json_data, ['storageTemplate', 'hashVerificationEnabled'], storage_template_hash_verification_enabled)
        if storage_template_template is None:
            raise SystemExit("Error: --storageTemplate.template is required")
        set_nested(json_data, ['storageTemplate', 'template'], storage_template_template)
        if templates_email_album_invite_template is None:
            raise SystemExit("Error: --templates.email.albumInviteTemplate is required")
        set_nested(json_data, ['templates', 'email', 'albumInviteTemplate'], templates_email_album_invite_template)
        if templates_email_album_update_template is None:
            raise SystemExit("Error: --templates.email.albumUpdateTemplate is required")
        set_nested(json_data, ['templates', 'email', 'albumUpdateTemplate'], templates_email_album_update_template)
        if templates_email_welcome_template is None:
            raise SystemExit("Error: --templates.email.welcomeTemplate is required")
        set_nested(json_data, ['templates', 'email', 'welcomeTemplate'], templates_email_welcome_template)
        if theme_custom_css is None:
            raise SystemExit("Error: --theme.customCss is required")
        set_nested(json_data, ['theme', 'customCss'], theme_custom_css)
        if trash_days is None:
            raise SystemExit("Error: --trash.days is required")
        set_nested(json_data, ['trash', 'days'], trash_days)
        if trash_enabled is None:
            raise SystemExit("Error: --trash.enabled is required")
        set_nested(json_data, ['trash', 'enabled'], trash_enabled)
        if user_delete_delay is None:
            raise SystemExit("Error: --user.deleteDelay is required")
        set_nested(json_data, ['user', 'deleteDelay'], user_delete_delay)
        if json_data:
            from immich.client.models.system_config_dto import SystemConfigDto
            system_config_dto = deserialize_request_body(json_data, SystemConfigDto)
            kwargs['system_config_dto'] = system_config_dto
    client = ctx.obj['client']
    api_group = client.system_config
    result = run_command(client, api_group, 'update_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
