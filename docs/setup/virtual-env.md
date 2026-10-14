# Virtual Environment

A virtual environment keeps project dependencies isolated from the global Python installation. Set one up in the project root before installing anything.

!!! tip "Prefer one command?"
    [uv](tooling.md#uv) creates and manages the environment for you (`uv add <package>`). This page covers the classic `venv` + `pip` workflow that works everywhere.

## Creating it

On `Windows`:

```
py -m venv .venv
```

On `Linux`:

```
python3 -m venv .venv
```

For example, `.venv` is a conventional folder name:

```bash
python3 -m venv .venv
```

This creates a `.venv` folder containing the virtual environment and its installed packages.

Upgrade pip inside the fresh environment (it often lags behind):

```bash
.venv/bin/python -m pip install --upgrade pip
```

!!! tip "Prefer `python -m pip` over bare `pip`"
    `python -m pip` guarantees you use the pip belonging to that Python — active venv or not. Bare `pip` depends on `PATH` order and is a classic source of packages landing in the wrong environment.

## Activating it

On `Windows` using Command Prompt:

```powershell
.venv\Scripts\activate.bat
```

On `Windows` using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On `Linux`:

```bash
source .venv/bin/activate
```

On `macOS` (same as Linux):

```
source .venv/bin/activate
```

A `(.venv)` prefix will appear in the terminal for every following command.

## Deactivating it

From the project root:

```
deactivate
```

## Installing packages with pip

!!! warning "Activate first"
    Always activate your virtual environment before installing project dependencies; otherwise, they will be installed in the global environment.

Install a package:

```bash
pip install <PACKAGE_NAME>
```

Install everything this project needs (dependencies live in `pyproject.toml`, see [Tooling](tooling.md#pyprojecttoml)):

```bash
pip install .            # runtime dependencies
pip install -e .         # editable install for local development
```

Uninstall a package:

```
pip uninstall <PACKAGE_NAME>
```

List installed packages:

```
pip list
```

List only outdated packages:

```
pip list --outdated
```

or short:

```
pip list -o
```

Upgrade a single package:

```
pip install -U <PACKAGE_NAME>
```

List all installed packages with their version:

```
pip freeze
```

Write all installed packages with their version to `requirements.txt`:

```
pip freeze > requirements.txt
```

## Housekeeping

Never commit the environment folder — add it to `.gitignore`:

```
.venv/
```

If an environment breaks beyond repair, delete and recreate it (your code is unaffected, only installed packages are lost):

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install .
```
