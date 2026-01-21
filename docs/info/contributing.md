# Contributing

This repository is **auto-generated** from the Immich OpenAPI specification.

## Pull requests

Pull requests are welcome! However, **modifications to auto-generated code will be rejected**.

### Prerequisites

We manage the project with [mise](https://mise.jdx.dev). To get started, install mise and run `mise setup`. Then, you can run any task with `mise run <task>`. To see all available tasks, run `mise tasks ls`.

### PR checklist

Before submitting a pull request, please ensure:

1. Run `mise run ci:check` to verify all checks pass
2. Run all tests (see [Testing](#testing))

### Auto-generated code restrictions

The following directories contain auto-generated code and **must not be modified**:

- `immich/client/generated/` - Auto-generated client
- `immich/cli/commands/` - Auto-generated CLI commands

### Testing

To run tests, run any of the `mise run test:*` tasks.
Make sure all tests pass before submitting a pull request.
If you don't have a local Immich server and cannot run End-to-End tests, please mention this in the pull request.

## Where to report issues

- **Immich API/spec problems** (missing/incorrect endpoints, schema issues, breaking API changes): open an issue in the [upstream Immich repository](https://github.com/immich-app/immich/issues).
- **Generation issues** (bad codegen output, typing problems introduced by generation, workflow automation problems): open an issue [here](https://github.com/timonrieger/immich-py/issues).

When reporting, include:

- The `IMMICH-VERSION` from this repo
- The Immich server version you are running
- A minimal reproduction (request/response or endpoint + payload)
