# Python quick-reference

### Using `PIP`

Install package:

```
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

### Virtual Environment (`VENV`)

Inside project root:

```
py -m venv <FOLDER_CONTAINING_DEPS>
```

e.g.

```
py -m venv .venv
```

---

### PYTEST

Run all tests from project root:

```
pytest
```
