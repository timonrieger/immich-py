# Getting Started

## Installation

You need Python 3.10–3.14 installed to be able to use this CLI.

=== "uv"

    ``` bash
    uv add immich --extra cli
    ```

=== "pip"

    ``` bash
    pip install immich[cli]
    ```

### Shell completion

Install shell completion for easier command-line usage. The command auto-detects the shell and installs the completion for it.

<div class="termy">

```console
$ immich --install-completion

fish completion installed in ~/.config/fish/completions/immich.fish
Completion will take effect once you restart the terminal
```

You will get auto-completion for the commands and options when hitting the <kbd>Tab</kbd> key.

</div>

!!! note "Performance"
    Due to the size of the CLI and Python's runtime overhead, the auto-completion is not as fast as I hoped it could be (see [typer#231](https://github.com/fastapi/typer/issues/231)).

## Setup

1. Have your Immich server running or use the [demo server](https://demo.immich.app).
2. Get an API key from your [Immich account settings](https://my.immich.app/user-settings?isOpen=api-keys).

## Create a profile

Using profiles allows you to use the CLI with different servers and reuse configurations easily.

<div class="termy">

```console
$ immich setup

# Enter your server URL: $ https://demo.immich.app/api
# Enter your API key: $ ********

Profile 'default' created successfully!
```

</div>

!!! note "Validation"
    The server is validated when you run `immich setup`. The CLI will fail if the server is not reachable.

See [`immich setup`](reference.md#immich-setup) for the full command reference.

## First commands

That's it! You can now run interact with the Immich server using the CLI.

<div class="termy">

```console
$ immich server get-about-info

{
  "build": "20375083601",
  "version": "v2.4.1",
}
```

</div>

You can also get the information in a different format, e.g. as a table:

<div class="termy">

```console
$ immich --format table server get-about-info

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Key      ┃ Value          ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ build    │ 20375083601    │
│ version  │ v2.4.1         │
└──────────┴────────────────┘
```

</div>

To see all available commands, run `immich --help` or see the [reference](reference.md).
