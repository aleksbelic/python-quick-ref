# What's New (3.10–3.15)

A tour of the language and standard-library changes of recent Python releases, grouped by theme. Python ships one feature release every October, and each release is supported for about five years. Always confirm details in the official *What's New* document for the version you use.

## Release overview

| Version | Highlights |
| --- | --- |
| **3.10** (2021) | `match` statement, `X | Y` in type hints, parenthesized `with`, clearer error messages |
| **3.11** (2022) | much faster, exception groups and `except*`, `tomllib`, `add_note()`, `Self` type |
| **3.12** (2023) | `type` statement and `def f[T]()` generics syntax, more flexible f-strings, `itertools.batched` |
| **3.13** (2024) | experimental free-threaded (no-GIL) build, experimental JIT, new interactive shell |
| **3.14** (2025) | template strings, lazy annotation evaluation, free-threading officially supported, `concurrent.interpreters` |
| **3.15** (Oct 2026) | `lazy` imports, built-in `frozendict` and `sentinel`, UTF-8 by default, unpacking in comprehensions, sampling profiler |

## Python 3.14

### Template strings (t-strings)

A `t'...'` literal looks like an f-string but does **not** produce a `str`. It produces a `Template` object that keeps the literal parts and the interpolated values *separate*, so a library can process them safely before combining (escaping HTML, quoting SQL parameters, and so on). That makes them the safe way to build structured text from user input.

```python
name = '<script>'
page = t'<p>Hello {name}</p>'   # a Template, not a finished string
# a library function decides how to escape `name` and render the result
```

### Lazy annotations

Annotations are no longer evaluated at definition time but when something asks for them, so forward references work without quotes. See [Type Hints](type-hints.md).

### Free-threading and sub-interpreters

The free-threaded build became an officially supported option, and `concurrent.interpreters` exposes isolated interpreters. See [Concurrency](concurrency.md).

### Smaller syntax change

`except ValueError, TypeError:` (no parentheses, no `as`) is accepted. See [Try–Except](try-except.md#exception-groups-and-except).

## Python 3.15

### Lazy imports

Marking an import `lazy` postpones loading the module until the name is first used, which shortens start-up for programs with many rarely-used dependencies.

```python
lazy import json         # nothing is imported yet
data = json.dumps({})    # imported now, on first use
```

Normal imports still run immediately; see [Imports & Packages](imports.md#what-import-does).

### `frozendict`

A built-in **immutable, hashable mapping** (hashable when its values are). Use it for constants and as a dict key or set member where a plain `dict` is not allowed. See [Mutable vs Immutable](mutable-immutable.md).

```python
settings = frozendict({'debug': False, 'retries': 3})
# settings['debug'] = True   # TypeError: it cannot be changed
```

### `sentinel`

A built-in way to create unique "no value given" markers, a cleaner replacement for the `_MISSING = object()` idiom, with a readable `repr` and proper identity semantics. Use it where `None` is itself a valid argument.

```python
MISSING = sentinel('MISSING')


def get(key, default=MISSING):
    ...
```

### UTF-8 by default

Text files opened without an explicit `encoding` now use UTF-8 on every platform, ending a classic Windows-versus-Linux difference. See [Text & Encoding](unicode.md).

### Unpacking in comprehensions

`*` (and `**`) can be used directly inside comprehensions and generator expressions to flatten, replacing a two-level loop.

```python
lists = [[1, 2], [3], [4, 5]]
flat = [*items for items in lists]   # [1, 2, 3, 4, 5]
```

### Tooling

A dedicated `profiling` package groups the profilers, including **Tachyon**, a low-overhead *sampling* profiler that can attach to a running process. The experimental JIT compiler is faster again, error messages suggest likely fixes, and the type system gains `TypedDict` extra items and `TypeForm`.

## How to use a new feature safely

- Check the minimum Python version your project supports (`requires-python` in `pyproject.toml`).
- Features marked "3.x+" in this reference raise `SyntaxError` or `AttributeError` on older interpreters.
- A new syntax feature (`match`, `except*`, `lazy`) cannot be backported; a library feature sometimes can via a PyPI package.

!!! note "Verify against the official notes"
    This page is a summary written to teach concepts. For exact semantics and edge cases, read the release's *What's New in Python* page on docs.python.org.
