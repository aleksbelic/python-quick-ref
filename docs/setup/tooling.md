# Tooling

The small set of tools most Python projects use day to day: a project manager, a linter/formatter, a type checker, and a test runner.

## uv

[uv](https://docs.astral.sh/uv/) is a fast, all-in-one replacement for `pip`, `venv`, and `pip-tools`. It also installs Python itself.

```bash
uv python install 3.11   # install a Python version
uv init my-project       # new project with a pyproject.toml
uv add requests          # add a dependency (creates .venv automatically)
uv run python main.py    # run inside the project's environment
uv sync                  # install everything from the lockfile
```

!!! tip "pip works fine too"
    Everything in [Virtual Env](virtual-env.md) is the classic `venv` + `pip` workflow. Learn it first; reach for `uv` when you want speed and lockfiles.

## pyproject.toml

`pyproject.toml` is the standard place for project metadata, dependencies, and tool settings.

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests>=2.32"]

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[tool.ruff]
line-length = 100
```

Install the project with its dev extras:

```bash
python -m pip install -e ".[dev]"
```

## Ruff (lint + format)

[Ruff](https://docs.astral.sh/ruff/) replaces `flake8`, `isort`, and `black` in one fast tool.

```bash
ruff check .          # find problems
ruff check . --fix    # auto-fix what it can
ruff format .         # format code
```

## Type checking

Type hints are not enforced at runtime (see [Type Hints](../type-hints.md)). A checker reads them and reports mismatches before you run anything:

```bash
python -m pip install mypy
mypy .
```

[Pyright](https://github.com/microsoft/pyright) and [ty](https://github.com/astral-sh/ty) are popular alternatives.

## Testing

[pytest](https://pytest.org) is the de-facto test runner.

```bash
pytest -q
```
