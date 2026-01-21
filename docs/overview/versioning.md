# Versioning

This package follows **[Semantic Versioning](https://semver.org)**. Some important notes:

- **Package version is not the server version**: `immich` package `x.y.z` is the client's own version.
- **Upstream breaking changes ⇒ major bump**: Breaking Immich changes produce a new **major** version of this package.
- **Supported Immich server version**: [IMMICH-VERSION](https://github.com/timonrieger/immich-py/blob/main/IMMICH-VERSION) tracks the Immich version the client was generated from. To find a compatible package version for your server's version, see [COMPATIBILITY.csv](https://github.com/timonrieger/immich-py/blob/main/COMPATIBILITY.csv).
