# Python Quick Reference

[![Documentation](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml/badge.svg)](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml)

A quick reference for the Python programming language: short lessons — one topic per page — built with [Zensical](https://zensical.org).

**Read it online: [abelic.com/python-quick-ref](https://abelic.com/python-quick-ref)**

## What's inside

| Section | Topics |
| --- | --- |
| Setup | installing Python, virtual environments, tooling (uv, ruff, type checkers) |
| Basics | syntax, variables, data types, casting, operators, conditions |
| Data Structures | strings, lists, tuples, sets, dicts, comprehensions, `collections`, mutability |
| Control Flow | loops, try/except |
| Functions & OOP | functions, generators, decorators, classes, dunders, dataclasses, type hints |
| I/O & Modules | input/output, formatting, files & `pathlib`, CSV, JSON, dates, regex, imports, CLI scripts, logging |
| Cheat Sheet | built-ins, methods, format specs, exceptions |
| Examples | Fibonacci, palindrome, primes, word counter, CSV summary, file renamer |

## Requirements

Python `3.11` or newer (required by Zensical).

## Development

Set up the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

Serve the project for development:

```bash
zensical serve
```

Now point your browser to `localhost:8000` for preview.

Build the project for production:

```bash
zensical build --clean
```

## Quality checks

The same checks run in CI on every pull request, and gate deployment on `main`:

```
python -m tools.check_snippets          # run every Python snippet in docs/
zensical build --clean --strict         # fail on warnings and broken links
```

## Project layout

```
docs/               Markdown pages (the site content)
docs/examples/      example programs and the testing chapter
zensical.toml       site configuration: navigation, theme, redirects
```

## Writing docs

- One topic per page; add it to `nav` in `zensical.toml` and to `docs/index.md`.
- Keep the tone terse: a sentence of explanation, a short snippet, an optional `!!! tip` or `!!! warning "Gotcha: ..."` callout.
- Python snippets in a page run top to bottom as one script, so later blocks can use earlier variables.
- A block with a title (<code>```python title="my_math.py"</code>) is written to that path first — use it for modules, packages, and data files the page's other snippets need.
- Put `<!-- no-run -->` on the line above a block that must not run (interactive entry points, placeholders). Put `<!-- check: skip -->` anywhere in a page to skip it entirely.
- Example pages show code from `src/examples/`; `tests/test_docs_sync.py` fails if the two drift apart.
- Renamed or moved a page? Add it to `[project.plugins.redirects.redirect_maps]` so old links keep working.

## License

[MIT](LICENSE)
