# Modules

Organize related files in a package (a directory with `__init__.py`) and import from it in different ways.

## The package

Two module files plus `__init__.py`, which declares what a star import exports.

```python
def hello_name(name = 'Someone'):
    print(f'Hello {name}')
```

```python
def hello_abc():
    print(f'Hello ABC')
```

```python
"""
which module files are going to be publicly exported
(these files will be automatically available using asterisk in 'from  my_module import *'):
"""
__all__ = ['my_module_file_1', 'my_module_file_2']
```

## Importing a module file

Import the submodule, then call through its namespace.

```python
# importing whole file and not just a function:
from my_module_dir import my_module_file_1

my_module_file_1.hello_name('Aleks')  # Hello Aleks
my_module_file_1.hello_name()         # Hello Someone (default value)
```

## Importing a single function

Import the name directly — no module prefix needed at the call site.

```python
# importing just a function:
from my_module_dir.my_module_file_1 import hello_name

hello_name('Aleks')  # Hello Aleks
```

## Star imports from a package

`import *` brings in every submodule listed in `__all__`.

```python
# importing whole module:
from my_module_dir import *

my_module_file_1.hello_name('Aleks')   # Hello Aleks
my_module_file_2.hello_abc()           # Hello ABC
```

!!! tip "Control star imports with __all__"
    Without `__all__`, `from package import *` picks up every public name. Defining `__all__` in `__init__.py` makes the public surface explicit.
