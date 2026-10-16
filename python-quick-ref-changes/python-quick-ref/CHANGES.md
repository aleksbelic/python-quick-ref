# Changes

Unzip over the repository root (the folder structure matches the repo).
Only Markdown and `zensical.toml`/`README.md` were touched. No `.py` files were added.
Verified with `zensical build --clean --strict` (Zensical 0.0.70): no issues found.

## Delete these files (replaced by theory pages)

```bash
git rm -r docs/examples
```

- docs/examples/fibonacci.md, palindrome.md, prime-number.md, word-counter.md
  -> ideas folded into docs/complexity.md ("Patterns worth recognising")
- docs/examples/csv-summary.md, file-renamer.md, testing.md
  -> ideas folded into docs/testing.md and docs/complexity.md

## Added (11 new theory pages)

how-python-works, numbers, unicode (Text & Encoding), scope-closures, iterators,
context-managers, oop-concepts, complexity, concurrency, testing, modern-python.

## Bugs fixed

- decorators.md: `repeat(0)` crashed with UnboundLocalError.
- formatting.md: tip implied `format()` is safe for untrusted templates (it is not).
- mutable-immutable.md: "only immutable objects can be dict keys" is inaccurate (hashability).
- loops.md: text said `while True`, example used `for`.
- files.md / unicode.md: UTF-8 is now the default encoding in Python 3.15.
- 5 headings + 2 admonition titles showed `__init__`, `__main__`, `__all__`, ... as bold text
  without underscores (dunders must be wrapped in backticks).
- cheatsheet.md: `d \| other`, `a \| b`, `X \| Y`, `dict \| dict` rendered with a visible backslash.
- scripts.md: leftover `<!-- no-run -->` markers for a tool that does not exist.
- virtual-env.md: duplicated command, Linux-only path used before activation, "from the project root" for `deactivate`.
- python-installation.md: wording tied to "this project"; warning that distro Python may be older than 3.11.
- dunders.md: `__add__` now returns NotImplemented for foreign types.
