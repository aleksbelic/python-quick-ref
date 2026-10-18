# Imports & Packages

Split code across files: a *module* is a single `.py` file, a *package* is a folder of modules, normally with an `__init__.py`.

## Creating a module

Any `.py` file is a module. This one defines two functions.

```python title="my_math.py"
def add(a, b):
    return a + b


def sub(a, b):
    return a - b
```

## Importing a module

Import the whole module and call through its namespace, optionally under a shorter alias.

```python
import my_math
import my_math as mm

print(my_math.add(1, 2))  # 3
print(mm.sub(5, 3))  # 2
```

## Importing specific names

Import only what you need with `from ... import`. Then no module prefix is needed at the call site.

```python
from my_math import add, sub

print(add(1, 2))  # 3
print(sub(5, 3))  # 2
```

!!! warning "Avoid `from module import *`"
    A star import dumps every public name into your namespace, hiding where things come from and risking name clashes. Import what you use.

!!! tip "Script-relative imports"
    `from my_math import ...` only works when `my_math.py` is on `sys.path` (e.g. you run the script from its own directory). For a robust script-relative import, bootstrap the path first:

    ```python
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    from my_math import add, sub
    ```

## Creating a package

A package is a directory with an `__init__.py` (which may be empty). Here are two modules inside `my_package/`:

```python title="my_package/greetings.py"
def hello_name(name='Someone'):
    return f'Hello {name}'
```

```python title="my_package/farewells.py"
from .greetings import hello_name  # relative import: same package


def bye_name(name='Someone'):
    return f'{hello_name(name)}, and goodbye'
```

```python title="my_package/__init__.py"
"""Greeting helpers."""

__all__ = ['greetings', 'farewells']
```

## Importing from a package

Import a submodule, or a single function from it.

```python
from my_package import greetings
from my_package.farewells import bye_name

print(greetings.hello_name('Aleks'))  # Hello Aleks
print(greetings.hello_name())  # Hello Someone (default value)
print(bye_name('Aleks'))  # Hello Aleks, and goodbye
```

!!! note "Namespace packages"
    A folder *without* `__init__.py` can still be imported as a "namespace package" (Python 3.3+). Regular packages with an `__init__.py` remain the clearest choice for your own code.

## Absolute vs relative imports

Inside a package you can write either. Absolute imports (`from my_package.greetings import hello_name`) always work and are the usual recommendation. Relative imports (`from .greetings import hello_name`, `from ..other import x`) only work *inside* a package and stay valid if you rename the package.

## `__all__`

`__all__` in `__init__.py` lists which submodules `from my_package import *` brings in. It documents the public surface.

!!! tip "Control star imports with `__all__`"
    Without `__all__`, `from package import *` picks up whatever happens to be imported in `__init__.py`. Defining `__all__` makes the public surface explicit.

## What `import` does

The first `import` of a module finds it, **runs its code once** from top to bottom, and stores the resulting module object in the `sys.modules` cache. Every later `import` of the same name just reuses that object. Consequences:

- top-level code in a module (including `print()`) runs at import time, which is why script logic belongs under the [`__main__` guard](scripts.md#the-__main__-guard);
- two modules that import each other (a *circular import*) can see each other half-initialised. Move the shared piece to a third module, or import inside the function that needs it;
- `from module import name` copies a *reference to the object* at that moment, so later rebinding `module.name` is not seen by the importer.

Since Python 3.15 you can mark an import as `lazy` so it only runs when the name is first used — see [What's New](modern-python.md).

## Where Python looks for modules

Python searches, in order, the script's folder (or the current directory), any `PYTHONPATH` entries, the standard library, and installed packages (`site-packages`). Inspect the list with `sys.path`.

```python
import sys

print(sys.path[0])  # the folder of the running script
```

!!! warning "Gotcha: don't name your file like a standard module"
    A file called `random.py` or `json.py` next to your script *shadows* the standard library module of the same name and causes baffling errors.
