# Versioning

This package follows **[Semantic Versioning](https://semver.org)**. Some important notes:

1. Package version is not the server version: The `immich` package version `x.y.z` is the client's own version and does not correspond to the Immich server version. This allows the client to have its own release cycle independent of server updates.
2. Upstream breaking changes ⇒ major bump: Breaking changes in the Immich API produce a new **major** version of this package, ensuring that major version upgrades indicate potential compatibility issues that require code changes.
3. Supported Immich server version: The [IMMICH-VERSION](https://github.com/timonrieger/immich-py/blob/main/IMMICH-VERSION) file tracks the Immich server version the client was generated from. To find a compatible package version for your server's version, see [COMPATIBILITY.csv](https://github.com/timonrieger/immich-py/blob/main/COMPATIBILITY.csv).
