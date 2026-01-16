"""Generated CLI commands for System config tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import typer

from immich.cli.runtime import load_file_bytes, deserialize_request_body, parse_complex_list, print_response, run_command, set_nested

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
    result = run_command(client, client.system_config, 'get_config', **kwargs)
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
    result = run_command(client, client.system_config, 'get_config_defaults', **kwargs)
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
    result = run_command(client, client.system_config, 'get_storage_template_options', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)

@app.command("update-config")
def update_config(
    ctx: typer.Context,
    backup_database_cron_expression: str = typer.Option(..., "--backup.database.cronExpression"),
    backup_database_enabled: bool = typer.Option(..., "--backup.database.enabled"),
    backup_database_keep_last_amount: float = typer.Option(..., "--backup.database.keepLastAmount"),
    ffmpeg_accel: str = typer.Option(..., "--ffmpeg.accel"),
    ffmpeg_accel_decode: bool = typer.Option(..., "--ffmpeg.accelDecode"),
    ffmpeg_accepted_audio_codecs: list[str] = typer.Option(..., "--ffmpeg.acceptedAudioCodecs"),
    ffmpeg_accepted_containers: list[str] = typer.Option(..., "--ffmpeg.acceptedContainers"),
    ffmpeg_accepted_video_codecs: list[str] = typer.Option(..., "--ffmpeg.acceptedVideoCodecs"),
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
    has_flags = any([backup_database_cron_expression, backup_database_enabled, backup_database_keep_last_amount, ffmpeg_accel, ffmpeg_accel_decode, ffmpeg_accepted_audio_codecs, ffmpeg_accepted_containers, ffmpeg_accepted_video_codecs, ffmpeg_bframes, ffmpeg_cq_mode, ffmpeg_crf, ffmpeg_gop_size, ffmpeg_max_bitrate, ffmpeg_preferred_hw_device, ffmpeg_preset, ffmpeg_refs, ffmpeg_target_audio_codec, ffmpeg_target_resolution, ffmpeg_target_video_codec, ffmpeg_temporal_aq, ffmpeg_threads, ffmpeg_tonemap, ffmpeg_transcode, ffmpeg_two_pass, image_colorspace, image_extract_embedded, image_fullsize_enabled, image_fullsize_format, image_fullsize_quality, image_preview_format, image_preview_quality, image_preview_size, image_thumbnail_format, image_thumbnail_quality, image_thumbnail_size, job_background_task_concurrency, job_editor_concurrency, job_face_detection_concurrency, job_library_concurrency, job_metadata_extraction_concurrency, job_migration_concurrency, job_notifications_concurrency, job_ocr_concurrency, job_search_concurrency, job_sidecar_concurrency, job_smart_search_concurrency, job_thumbnail_generation_concurrency, job_video_conversion_concurrency, job_workflow_concurrency, library_scan_cron_expression, library_scan_enabled, library_watch_enabled, logging_enabled, logging_level, machine_learning_availability_checks_enabled, machine_learning_availability_checks_interval, machine_learning_availability_checks_timeout, machine_learning_clip_enabled, machine_learning_clip_model_name, machine_learning_duplicate_detection_enabled, machine_learning_duplicate_detection_max_distance, machine_learning_enabled, machine_learning_facial_recognition_enabled, machine_learning_facial_recognition_max_distance, machine_learning_facial_recognition_min_faces, machine_learning_facial_recognition_min_score, machine_learning_facial_recognition_model_name, machine_learning_ocr_enabled, machine_learning_ocr_max_resolution, machine_learning_ocr_min_detection_score, machine_learning_ocr_min_recognition_score, machine_learning_ocr_model_name, machine_learning_urls, map_dark_style, map_enabled, map_light_style, metadata_faces_import_, new_version_check_enabled, nightly_tasks_cluster_new_faces, nightly_tasks_database_cleanup, nightly_tasks_generate_memories, nightly_tasks_missing_thumbnails, nightly_tasks_start_time, nightly_tasks_sync_quota_usage, notifications_smtp_enabled, notifications_smtp_from_, notifications_smtp_reply_to, notifications_smtp_transport_host, notifications_smtp_transport_ignore_cert, notifications_smtp_transport_password, notifications_smtp_transport_port, notifications_smtp_transport_secure, notifications_smtp_transport_username, oauth_auto_launch, oauth_auto_register, oauth_button_text, oauth_client_id, oauth_client_secret, oauth_default_storage_quota, oauth_enabled, oauth_issuer_url, oauth_mobile_override_enabled, oauth_mobile_redirect_uri, oauth_profile_signing_algorithm, oauth_role_claim, oauth_scope, oauth_signing_algorithm, oauth_storage_label_claim, oauth_storage_quota_claim, oauth_timeout, oauth_token_endpoint_auth_method, password_login_enabled, reverse_geocoding_enabled, server_external_domain, server_login_page_message, server_public_users, storage_template_enabled, storage_template_hash_verification_enabled, storage_template_template, templates_email_album_invite_template, templates_email_album_update_template, templates_email_welcome_template, theme_custom_css, trash_days, trash_enabled, user_delete_delay])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([backup_database_cron_expression, backup_database_enabled, backup_database_keep_last_amount, ffmpeg_accel, ffmpeg_accel_decode, ffmpeg_accepted_audio_codecs, ffmpeg_accepted_containers, ffmpeg_accepted_video_codecs, ffmpeg_bframes, ffmpeg_cq_mode, ffmpeg_crf, ffmpeg_gop_size, ffmpeg_max_bitrate, ffmpeg_preferred_hw_device, ffmpeg_preset, ffmpeg_refs, ffmpeg_target_audio_codec, ffmpeg_target_resolution, ffmpeg_target_video_codec, ffmpeg_temporal_aq, ffmpeg_threads, ffmpeg_tonemap, ffmpeg_transcode, ffmpeg_two_pass, image_colorspace, image_extract_embedded, image_fullsize_enabled, image_fullsize_format, image_fullsize_quality, image_preview_format, image_preview_quality, image_preview_size, image_thumbnail_format, image_thumbnail_quality, image_thumbnail_size, job_background_task_concurrency, job_editor_concurrency, job_face_detection_concurrency, job_library_concurrency, job_metadata_extraction_concurrency, job_migration_concurrency, job_notifications_concurrency, job_ocr_concurrency, job_search_concurrency, job_sidecar_concurrency, job_smart_search_concurrency, job_thumbnail_generation_concurrency, job_video_conversion_concurrency, job_workflow_concurrency, library_scan_cron_expression, library_scan_enabled, library_watch_enabled, logging_enabled, logging_level, machine_learning_availability_checks_enabled, machine_learning_availability_checks_interval, machine_learning_availability_checks_timeout, machine_learning_clip_enabled, machine_learning_clip_model_name, machine_learning_duplicate_detection_enabled, machine_learning_duplicate_detection_max_distance, machine_learning_enabled, machine_learning_facial_recognition_enabled, machine_learning_facial_recognition_max_distance, machine_learning_facial_recognition_min_faces, machine_learning_facial_recognition_min_score, machine_learning_facial_recognition_model_name, machine_learning_ocr_enabled, machine_learning_ocr_max_resolution, machine_learning_ocr_min_detection_score, machine_learning_ocr_min_recognition_score, machine_learning_ocr_model_name, machine_learning_urls, map_dark_style, map_enabled, map_light_style, metadata_faces_import_, new_version_check_enabled, nightly_tasks_cluster_new_faces, nightly_tasks_database_cleanup, nightly_tasks_generate_memories, nightly_tasks_missing_thumbnails, nightly_tasks_start_time, nightly_tasks_sync_quota_usage, notifications_smtp_enabled, notifications_smtp_from_, notifications_smtp_reply_to, notifications_smtp_transport_host, notifications_smtp_transport_ignore_cert, notifications_smtp_transport_password, notifications_smtp_transport_port, notifications_smtp_transport_secure, notifications_smtp_transport_username, oauth_auto_launch, oauth_auto_register, oauth_button_text, oauth_client_id, oauth_client_secret, oauth_default_storage_quota, oauth_enabled, oauth_issuer_url, oauth_mobile_override_enabled, oauth_mobile_redirect_uri, oauth_profile_signing_algorithm, oauth_role_claim, oauth_scope, oauth_signing_algorithm, oauth_storage_label_claim, oauth_storage_quota_claim, oauth_timeout, oauth_token_endpoint_auth_method, password_login_enabled, reverse_geocoding_enabled, server_external_domain, server_login_page_message, server_public_users, storage_template_enabled, storage_template_hash_verification_enabled, storage_template_template, templates_email_album_invite_template, templates_email_album_update_template, templates_email_welcome_template, theme_custom_css, trash_days, trash_enabled, user_delete_delay]):
        json_data = {}
        set_nested(json_data, ['backup', 'database', 'cronExpression'], backup_database_cron_expression)
        set_nested(json_data, ['backup', 'database', 'enabled'], backup_database_enabled)
        set_nested(json_data, ['backup', 'database', 'keepLastAmount'], backup_database_keep_last_amount)
        set_nested(json_data, ['ffmpeg', 'accel'], ffmpeg_accel)
        set_nested(json_data, ['ffmpeg', 'accelDecode'], ffmpeg_accel_decode)
        set_nested(json_data, ['ffmpeg', 'acceptedAudioCodecs'], ffmpeg_accepted_audio_codecs)
        set_nested(json_data, ['ffmpeg', 'acceptedContainers'], ffmpeg_accepted_containers)
        set_nested(json_data, ['ffmpeg', 'acceptedVideoCodecs'], ffmpeg_accepted_video_codecs)
        set_nested(json_data, ['ffmpeg', 'bframes'], ffmpeg_bframes)
        set_nested(json_data, ['ffmpeg', 'cqMode'], ffmpeg_cq_mode)
        set_nested(json_data, ['ffmpeg', 'crf'], ffmpeg_crf)
        set_nested(json_data, ['ffmpeg', 'gopSize'], ffmpeg_gop_size)
        set_nested(json_data, ['ffmpeg', 'maxBitrate'], ffmpeg_max_bitrate)
        set_nested(json_data, ['ffmpeg', 'preferredHwDevice'], ffmpeg_preferred_hw_device)
        set_nested(json_data, ['ffmpeg', 'preset'], ffmpeg_preset)
        set_nested(json_data, ['ffmpeg', 'refs'], ffmpeg_refs)
        set_nested(json_data, ['ffmpeg', 'targetAudioCodec'], ffmpeg_target_audio_codec)
        set_nested(json_data, ['ffmpeg', 'targetResolution'], ffmpeg_target_resolution)
        set_nested(json_data, ['ffmpeg', 'targetVideoCodec'], ffmpeg_target_video_codec)
        set_nested(json_data, ['ffmpeg', 'temporalAQ'], ffmpeg_temporal_aq)
        set_nested(json_data, ['ffmpeg', 'threads'], ffmpeg_threads)
        set_nested(json_data, ['ffmpeg', 'tonemap'], ffmpeg_tonemap)
        set_nested(json_data, ['ffmpeg', 'transcode'], ffmpeg_transcode)
        set_nested(json_data, ['ffmpeg', 'twoPass'], ffmpeg_two_pass)
        set_nested(json_data, ['image', 'colorspace'], image_colorspace)
        set_nested(json_data, ['image', 'extractEmbedded'], image_extract_embedded)
        set_nested(json_data, ['image', 'fullsize', 'enabled'], image_fullsize_enabled)
        set_nested(json_data, ['image', 'fullsize', 'format'], image_fullsize_format)
        set_nested(json_data, ['image', 'fullsize', 'quality'], image_fullsize_quality)
        set_nested(json_data, ['image', 'preview', 'format'], image_preview_format)
        set_nested(json_data, ['image', 'preview', 'quality'], image_preview_quality)
        set_nested(json_data, ['image', 'preview', 'size'], image_preview_size)
        set_nested(json_data, ['image', 'thumbnail', 'format'], image_thumbnail_format)
        set_nested(json_data, ['image', 'thumbnail', 'quality'], image_thumbnail_quality)
        set_nested(json_data, ['image', 'thumbnail', 'size'], image_thumbnail_size)
        set_nested(json_data, ['job', 'backgroundTask', 'concurrency'], job_background_task_concurrency)
        set_nested(json_data, ['job', 'editor', 'concurrency'], job_editor_concurrency)
        set_nested(json_data, ['job', 'faceDetection', 'concurrency'], job_face_detection_concurrency)
        set_nested(json_data, ['job', 'library', 'concurrency'], job_library_concurrency)
        set_nested(json_data, ['job', 'metadataExtraction', 'concurrency'], job_metadata_extraction_concurrency)
        set_nested(json_data, ['job', 'migration', 'concurrency'], job_migration_concurrency)
        set_nested(json_data, ['job', 'notifications', 'concurrency'], job_notifications_concurrency)
        set_nested(json_data, ['job', 'ocr', 'concurrency'], job_ocr_concurrency)
        set_nested(json_data, ['job', 'search', 'concurrency'], job_search_concurrency)
        set_nested(json_data, ['job', 'sidecar', 'concurrency'], job_sidecar_concurrency)
        set_nested(json_data, ['job', 'smartSearch', 'concurrency'], job_smart_search_concurrency)
        set_nested(json_data, ['job', 'thumbnailGeneration', 'concurrency'], job_thumbnail_generation_concurrency)
        set_nested(json_data, ['job', 'videoConversion', 'concurrency'], job_video_conversion_concurrency)
        set_nested(json_data, ['job', 'workflow', 'concurrency'], job_workflow_concurrency)
        set_nested(json_data, ['library', 'scan', 'cronExpression'], library_scan_cron_expression)
        set_nested(json_data, ['library', 'scan', 'enabled'], library_scan_enabled)
        set_nested(json_data, ['library', 'watch', 'enabled'], library_watch_enabled)
        set_nested(json_data, ['logging', 'enabled'], logging_enabled)
        set_nested(json_data, ['logging', 'level'], logging_level)
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'enabled'], machine_learning_availability_checks_enabled)
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'interval'], machine_learning_availability_checks_interval)
        set_nested(json_data, ['machineLearning', 'availabilityChecks', 'timeout'], machine_learning_availability_checks_timeout)
        set_nested(json_data, ['machineLearning', 'clip', 'enabled'], machine_learning_clip_enabled)
        set_nested(json_data, ['machineLearning', 'clip', 'modelName'], machine_learning_clip_model_name)
        set_nested(json_data, ['machineLearning', 'duplicateDetection', 'enabled'], machine_learning_duplicate_detection_enabled)
        set_nested(json_data, ['machineLearning', 'duplicateDetection', 'maxDistance'], machine_learning_duplicate_detection_max_distance)
        set_nested(json_data, ['machineLearning', 'enabled'], machine_learning_enabled)
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'enabled'], machine_learning_facial_recognition_enabled)
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'maxDistance'], machine_learning_facial_recognition_max_distance)
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'minFaces'], machine_learning_facial_recognition_min_faces)
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'minScore'], machine_learning_facial_recognition_min_score)
        set_nested(json_data, ['machineLearning', 'facialRecognition', 'modelName'], machine_learning_facial_recognition_model_name)
        set_nested(json_data, ['machineLearning', 'ocr', 'enabled'], machine_learning_ocr_enabled)
        set_nested(json_data, ['machineLearning', 'ocr', 'maxResolution'], machine_learning_ocr_max_resolution)
        set_nested(json_data, ['machineLearning', 'ocr', 'minDetectionScore'], machine_learning_ocr_min_detection_score)
        set_nested(json_data, ['machineLearning', 'ocr', 'minRecognitionScore'], machine_learning_ocr_min_recognition_score)
        set_nested(json_data, ['machineLearning', 'ocr', 'modelName'], machine_learning_ocr_model_name)
        set_nested(json_data, ['machineLearning', 'urls'], machine_learning_urls)
        set_nested(json_data, ['map', 'darkStyle'], map_dark_style)
        set_nested(json_data, ['map', 'enabled'], map_enabled)
        set_nested(json_data, ['map', 'lightStyle'], map_light_style)
        set_nested(json_data, ['metadata', 'faces', 'import'], metadata_faces_import_)
        set_nested(json_data, ['newVersionCheck', 'enabled'], new_version_check_enabled)
        set_nested(json_data, ['nightlyTasks', 'clusterNewFaces'], nightly_tasks_cluster_new_faces)
        set_nested(json_data, ['nightlyTasks', 'databaseCleanup'], nightly_tasks_database_cleanup)
        set_nested(json_data, ['nightlyTasks', 'generateMemories'], nightly_tasks_generate_memories)
        set_nested(json_data, ['nightlyTasks', 'missingThumbnails'], nightly_tasks_missing_thumbnails)
        set_nested(json_data, ['nightlyTasks', 'startTime'], nightly_tasks_start_time)
        set_nested(json_data, ['nightlyTasks', 'syncQuotaUsage'], nightly_tasks_sync_quota_usage)
        set_nested(json_data, ['notifications', 'smtp', 'enabled'], notifications_smtp_enabled)
        set_nested(json_data, ['notifications', 'smtp', 'from'], notifications_smtp_from_)
        set_nested(json_data, ['notifications', 'smtp', 'replyTo'], notifications_smtp_reply_to)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'host'], notifications_smtp_transport_host)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'ignoreCert'], notifications_smtp_transport_ignore_cert)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'password'], notifications_smtp_transport_password)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'port'], notifications_smtp_transport_port)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'secure'], notifications_smtp_transport_secure)
        set_nested(json_data, ['notifications', 'smtp', 'transport', 'username'], notifications_smtp_transport_username)
        set_nested(json_data, ['oauth', 'autoLaunch'], oauth_auto_launch)
        set_nested(json_data, ['oauth', 'autoRegister'], oauth_auto_register)
        set_nested(json_data, ['oauth', 'buttonText'], oauth_button_text)
        set_nested(json_data, ['oauth', 'clientId'], oauth_client_id)
        set_nested(json_data, ['oauth', 'clientSecret'], oauth_client_secret)
        set_nested(json_data, ['oauth', 'defaultStorageQuota'], oauth_default_storage_quota)
        set_nested(json_data, ['oauth', 'enabled'], oauth_enabled)
        set_nested(json_data, ['oauth', 'issuerUrl'], oauth_issuer_url)
        set_nested(json_data, ['oauth', 'mobileOverrideEnabled'], oauth_mobile_override_enabled)
        set_nested(json_data, ['oauth', 'mobileRedirectUri'], oauth_mobile_redirect_uri)
        set_nested(json_data, ['oauth', 'profileSigningAlgorithm'], oauth_profile_signing_algorithm)
        set_nested(json_data, ['oauth', 'roleClaim'], oauth_role_claim)
        set_nested(json_data, ['oauth', 'scope'], oauth_scope)
        set_nested(json_data, ['oauth', 'signingAlgorithm'], oauth_signing_algorithm)
        set_nested(json_data, ['oauth', 'storageLabelClaim'], oauth_storage_label_claim)
        set_nested(json_data, ['oauth', 'storageQuotaClaim'], oauth_storage_quota_claim)
        set_nested(json_data, ['oauth', 'timeout'], oauth_timeout)
        set_nested(json_data, ['oauth', 'tokenEndpointAuthMethod'], oauth_token_endpoint_auth_method)
        set_nested(json_data, ['passwordLogin', 'enabled'], password_login_enabled)
        set_nested(json_data, ['reverseGeocoding', 'enabled'], reverse_geocoding_enabled)
        set_nested(json_data, ['server', 'externalDomain'], server_external_domain)
        set_nested(json_data, ['server', 'loginPageMessage'], server_login_page_message)
        set_nested(json_data, ['server', 'publicUsers'], server_public_users)
        set_nested(json_data, ['storageTemplate', 'enabled'], storage_template_enabled)
        set_nested(json_data, ['storageTemplate', 'hashVerificationEnabled'], storage_template_hash_verification_enabled)
        set_nested(json_data, ['storageTemplate', 'template'], storage_template_template)
        set_nested(json_data, ['templates', 'email', 'albumInviteTemplate'], templates_email_album_invite_template)
        set_nested(json_data, ['templates', 'email', 'albumUpdateTemplate'], templates_email_album_update_template)
        set_nested(json_data, ['templates', 'email', 'welcomeTemplate'], templates_email_welcome_template)
        set_nested(json_data, ['theme', 'customCss'], theme_custom_css)
        set_nested(json_data, ['trash', 'days'], trash_days)
        set_nested(json_data, ['trash', 'enabled'], trash_enabled)
        set_nested(json_data, ['user', 'deleteDelay'], user_delete_delay)
        from immich.client.models.system_config_dto import SystemConfigDto
        system_config_dto = deserialize_request_body(json_data, SystemConfigDto)
        kwargs['system_config_dto'] = system_config_dto
    client = ctx.obj['client']
    result = run_command(client, client.system_config, 'update_config', **kwargs)
    format_mode = ctx.obj.get('format', 'pretty')
    print_response(result, format_mode)
