from pathlib import Path

DEVICE_ID = "immich-py"
DEMO_API_URL = "https://demo.immich.app/api"
API_KEY_URL = "https://my.immich.app/user-settings?isOpen=api-keys"
CONFIG_DIR = Path.home() / ".immich-py"
CONFIG_FILE = CONFIG_DIR / "config.toml"
DEFAULT_PROFILE = "default"
DEFAULT_FORMAT = "pretty"

# Environment variables
IMMICH_FORMAT = "IMMICH_FORMAT"
IMMICH_API_URL = "IMMICH_API_URL"
IMMICH_API_KEY = "IMMICH_API_KEY"  # nosec: B105
IMMICH_ACCESS_TOKEN = "IMMICH_ACCESS_TOKEN"  # nosec: B105
IMMICH_PROFILE = "IMMICH_PROFILE"

# Strings that indicate secret values
SECRET_KEYS = ["api_key", "access_token"]
