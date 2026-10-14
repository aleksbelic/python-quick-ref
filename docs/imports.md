# Imports

Split code across files: one module defines functions, another imports and uses them.

## Creating a module

Any `.py` file is a module. This one defines two functions.

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

## Importing specific functions

Import only what you need with `from ... import`. Use `*` to import everything.

```python
# importing one or more functions from another file (use an asterisk (*) to import everything)
from my_math import add, sub

print(add(1, 2))  # 3
print(sub(5, 3))  # 2
```

!!! tip "Script-relative imports"
    `from my_math import ...` only works when `my_math.py` is on `sys.path` (e.g. you run the script from its own directory). For a robust script-relative import, bootstrap the path first:

    ```python
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    from my_math import add, sub
    ```
