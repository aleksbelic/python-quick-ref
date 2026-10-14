# File Renamer

Add a prefix to every file in a folder, with a dry-run mode that only reports what *would* change. Uses [`pathlib`](../files.md#pathlib).

```python
from pathlib import Path


def add_prefix(folder: Path, prefix: str, dry_run: bool = True) -> list[tuple[Path, Path]]:
    """Plan (and optionally perform) renaming every file in `folder` to `<prefix><name>`.

    Returns the (old, new) pairs. With `dry_run=True` nothing is renamed.
    """
    renames = [
        (path, path.with_name(prefix + path.name))
        for path in sorted(folder.iterdir())
        if path.is_file() and not path.name.startswith(prefix)
    ]
    if not dry_run:
        for old, new in renames:
            old.rename(new)
    return renames
```

```python
from pathlib import Path

photos = Path('photos')

for old, new in add_prefix(photos, '2026_'):  # dry run: nothing is renamed
    print(f'{old.name} -> {new.name}')
# beach.jpg -> 2026_beach.jpg
# city.jpg -> 2026_city.jpg

add_prefix(photos, '2026_', dry_run=False)  # now really rename
print(sorted(p.name for p in photos.iterdir()))  # ['2026_beach.jpg', '2026_city.jpg']
```

!!! note "Needs a folder to run"
    The snippet assumes a `photos/` folder with files in it — create one, or point it at any test folder, to run it. It defaults to a dry run, so nothing is renamed.

!!! warning "Make destructive scripts safe by default"
    `dry_run=True` is the default, so calling the function without thinking never touches your files. Skipping names that already have the prefix makes it safe to run twice.
