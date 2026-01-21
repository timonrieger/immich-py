# Contributing

This repository is **auto-generated** from the Immich OpenAPI specification.

## Pull requests

Pull requests are welcome! However, **modifications to auto-generated code will be rejected**.

### PR checklist

Before submitting a pull request, please ensure:

1. Install [mise](https://mise.jdx.dev)
2. Run `mise run ci:check` to verify all checks pass
3. To see all available tasks, run `mise tasks ls`

### Auto-generated code restrictions

The following directories contain auto-generated code and **must not be modified**:

- `immich/client/` - Auto-generated client
- `immich/cli/commands/` - Auto-generated CLI commands

## Where to report issues

- **Immich API/spec problems** (missing/incorrect endpoints, schema issues, breaking API changes): open an issue in the [upstream Immich repository](https://github.com/immich-app/immich/issues).
- **Generation issues** (bad codegen output, typing problems introduced by generation, workflow automation problems): open an issue [here](https://github.com/timonrieger/immich-py/issues).

When reporting, include:

- The `IMMICH-VERSION` from this repo
- The Immich server version you are running
- A minimal reproduction (request/response or endpoint + payload)
