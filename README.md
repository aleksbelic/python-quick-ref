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

Set up the environment (check yours is `3.11` or newer first):

```bash
python3 --version           # check Python version
python3 -m venv .venv       # create a virtual environment
source .venv/bin/activate   # activate it
pip install .               # install dependencies
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

These run in CI on every push to `main`:

```
zensical build --clean --strict         # fail on warnings and broken links
```

## Project layout

```
docs/               Markdown pages (the site content)
docs/examples/      example programs and the testing chapter
zensical.toml       site configuration: navigation, theme
```

## Writing docs

- One topic per page; add it to `nav` in `zensical.toml` and to `docs/index.md`.
- Keep the tone terse: a sentence of explanation, a short snippet, an optional `!!! tip` or `!!! warning "Gotcha: ..."` callout.
- Keep snippets self-contained and paste-and-run: no external files, no stdin, no `sys.exit()`. If a snippet needs a fixture to run, say so in a `!!! note`.

## License

[MIT](LICENSE)
