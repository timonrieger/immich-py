from pathlib import Path

DEVICE_ID = "immich-py"
API_KEY_URL = "https://my.immich.app/user-settings?isOpen=api-keys"
CONFIG_DIR = Path.home() / ".immich-py"
CONFIG_FILE = CONFIG_DIR / "config.toml"
DEFAULT_PROFILE = "default"

# Environment variables
IMMICH_FORMAT = "IMMICH_FORMAT"
IMMICH_API_URL = "IMMICH_API_URL"
IMMICH_API_KEY = "IMMICH_API_KEY"  # nosec: B105
IMMICH_ACCESS_TOKEN = "IMMICH_ACCESS_TOKEN"  # nosec: B105

# Strings that indicate secret values
SECRET_KEYS = ["api_key", "access_token"]
