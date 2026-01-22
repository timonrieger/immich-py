# Environment Variables

The Immich CLI supports environment variables as an alternative to command-line flags or profile settings.

## Configuration Priority

Priority order (highest to lowest):

1. Command-line flags (`--api-key`, `--base-url`, etc.)
2. **Environment variables** (this page)
3. Profile settings (from `immich setup`)

## Available Environment Variables

| Environment Variable | Description | Command-line Flag |
|---------------------|-------------|-------------------|
| `IMMICH_API_URL` | Server URL | `--base-url` |
| `IMMICH_API_KEY` | API key | `--api-key` |
| `IMMICH_ACCESS_TOKEN` | Access token | `--access-token` |
| `IMMICH_PROFILE` | Profile name | `--profile` |
| `IMMICH_FORMAT` | Output format (`pretty`, `json`, `table`) | `--format` |

See the [CLI Reference](./reference.md) for full details on each option.
