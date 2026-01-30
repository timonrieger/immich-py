## Versioning Model

This package follows [Semantic Versioning](https://semver.org).

The package version (`x.y.z`) reflects the **client library**, not the Immich server. Versions are managed independently so the client can evolve on its own release cycle.

## How Upstream Changes Affect Releases

Changes in the Immich API trigger a new release of this package. The type of version bump depends on how those changes impact the client’s public API:

- **Major**: Breaking changes that require users to modify their code
- **Minor**: Backward-compatible additions (e.g., new endpoints or models)
- **Patch**: Internal sync updates or upstream changes that do not affect the client’s public surface

In short, version numbers indicate **client impact**, not the size of the server update.

## Immich Server Compatibility

The [`IMMICH-VERSION`](https://github.com/timonrieger/immich-py/blob/main/IMMICH-VERSION) file records the Immich server version the client was generated from.

To determine which package version works with your server, refer to [`COMPATIBILITY.csv`](https://github.com/timonrieger/immich-py/blob/main/COMPATIBILITY.csv).
