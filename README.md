# Python quick-reference

## Development

Serve the project for development:
```bash
zensical serve
```

Point your browser to `localhost:8000` for preview.

Build the project for production:
```bash
zensical build
```


### Virtual Environment (`VENV`)

Set up a virtual environment in the project root.

On `Windows`:

```
py -m venv <FOLDER_CONTAINING_DEPS>
```

On `Linux`:

```
python3 -m venv <FOLDER_CONTAINING_DEPS>
```

For example, `.venv` is a conventional folder name:

```sh
python3 -m venv .venv
```

This creates a `.venv` folder containing the virtual environment and its installed packages.

To activate the virtual environment on `Windows` using Command Prompt:

```
.venv\Scripts\activate.bat
```

To activate it on `Windows` using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

To activate it on `Linux`:

```
source .venv/bin/activate
```

A `(.venv)` prefix will appear in the terminal for every following command.

Deactivate venv from project root:

```
deactivate
```

---

### Using `PIP` package manager

_Note: Always activate your virtual environment before installing project dependencies; otherwise, they will be installed in the global environment._

Install package:

```localhost:8000 
pip install <PACKAGE_NAME>
```

Uninstall package:

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

Upgrade single package:

```
pip install -U <PACKAGE_NAME>
```

List all installed packages with their version:

```
pip freeze
```

Write all installed packages with their version to a file `requirements.txt`:

```
pip freeze > requirements.txt
```

Install packages listed in file `requirements.txt` (specified version):

```
pip install -r requirements.txt
```

---

### PYTEST

Run all tests from project root:

```
pytest
```
