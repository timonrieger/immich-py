# Examples

This page contains practical examples of using the Immich CLI for common tasks.
> Have an example? You’re welcome to suggest it on [GitHub issues](https://github.com/timonrieger/immich-py/issues).

## List all albums and parse with jq

Get all albums and their name and ID:

<div class="termy">

```console
$ immich albums get-all-albums | jq -r '.[] | "\(.album_name) \(.id)"'
Animal Portraits ff09c49f-525d-4216-bc5a-8ff070bca149
Vacation 2023 851c8f67-9bf3-48f5-8130-59da9ab17c06
Selfies c980670b-69d1-42ee-b4a5-86947f169d99
```

</div>

## Download an album archive

Download an album archive to a directory with progress bar:

<div class="termy">

```console
> immich download download-archive-to-file out/ \
 --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --show-progress

---> 100%

[
  "out/archive-d73aaebe-f8d2-486d-b0f0-a0a64c75320b.zip"
]
```

</div>

## Upload assets

Upload assets to your Immich server. Use `--dry-run` to preview what would be uploaded:

<div class="termy">

```console
$ immich assets upload ~/timelapse.mp4 --dry-run
{
  "uploaded": [
    {
      "asset": {
        "id": "ba199326-210b-492c-b5cb-4fc54e00f032",
        "status": "created"
      },
      "filepath": "~/timelapse.mp4"
    }
  ],
  "rejected": [],
  "failed": [],
  "stats": {
    "total": 1,
    "uploaded": 1,
    "rejected": 0,
    "failed": 0
  }
}
```

</div>

## List all people with names

Get all people and filter to only show those with names:

<div class="termy">

```console
$ immich people get-all-people | jq '.people[] | select(.name != "")'
{
  "birth_date": null,
  "color": null,
  "id": "6130d2d5-5f96-4aa0-9725-36929c5c8f19",
  "is_favorite": false,
  "is_hidden": false,
  "name": "Timon",
  "thumbnail_path": "/data/thumbs/0245136d-b027-4144-a764-81ecca080cf8/
    61/30/6130d2d5-5f96-4aa0-9725-36929c5c8f19.jpeg",
  "updated_at": "2026-01-20 22:30:00.771000+00:00"
}
```

</div>

## List all users

Get all users in a table format:

<div class="termy">

```console
$ immich --format table users search-users
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ avatar_color       │ green                                │
│ email              │ admin@immich.cloud                   │
│ id                 │ f1c0dc5f-a938-4480-a27f-dcb127c421c6 │
│ name               │ admin                                │
│ profile_changed_at │ 2026-01-09 00:03:59.798000+00:00     │
│ profile_image_path │                                      │
└────────────────────┴──────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ avatar_color       │ primary                              │
│ email              │ demo@immich.app                      │
│ id                 │ 6733f307-4f31-43b0-906c-95ea45d4680e │
│ name               │ demo                                 │
│ profile_changed_at │ 2025-11-11 16:45:16.871000+00:00     │
│ profile_image_path │                                      │
└────────────────────┴──────────────────────────────────────┘
```

</div>
