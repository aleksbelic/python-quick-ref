# Python Quick Reference
[![Documentation](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml/badge.svg)](https://github.com/aleksbelic/python-quick-ref/actions/workflows/docs.yml)

A quick reference for Python programming language.

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
