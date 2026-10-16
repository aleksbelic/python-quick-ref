# Python Quick Reference

[![Documentation](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml/badge.svg)](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml)

A quick reference for the Python programming language: short lessons — one topic per page — built with [Zensical](https://zensical.org).

**Read it online: [abelic.com/python-quick-ref](https://abelic.com/python-quick-ref)**

## What's inside

| Section | Topics |
| --- | --- |
| Setup | installing Python, virtual environments, tooling (uv, ruff, type checkers) |
| Basics | how Python works, syntax, variables, data types, numbers, casting, operators, conditions |
| Data Structures | strings, text & encoding, lists, tuples, sets, dicts, comprehensions, `collections`, mutability, complexity |
| Control Flow | loops, iterators, try/except, context managers |
| Functions & OOP | functions, scope & closures, generators, decorators, classes, OOP concepts, dunders, dataclasses, type hints |
| I/O & Modules | input/output, formatting, files & `pathlib`, CSV, JSON, dates, regex, imports, CLI scripts, logging |
| Going Further | concurrency, testing concepts, what's new in 3.10–3.15 |
| Cheat Sheet | built-ins, methods, format specs, exceptions, precedence, complexity, version notes |

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
zensical build --clean --strict  # fail on warnings and broken links
```

## Project layout

```
docs/               Markdown pages (the site content)
docs/setup/         installation and tooling pages
zensical.toml       site configuration: navigation, theme
```

## Writing docs

- One topic per page; add it to `nav` in `zensical.toml` and to `docs/index.md`.
- Keep the tone terse: a sentence of explanation, a short snippet, an optional `!!! tip` or `!!! warning "Gotcha: ..."` callout.
- Theory first: explain the concept and *why* it works that way, then illustrate with a short snippet. The site is Markdown only; there are no `.py` files to run.
- Keep snippets small and self-contained, with the expected output in a comment. If a snippet depends on an external file or stdin, say so in a `!!! note`.
- Link related pages to each other, and wrap dunder names in backticks (`__init__`), also in headings, otherwise Markdown reads the underscores as bold.

## License

[MIT](LICENSE)
