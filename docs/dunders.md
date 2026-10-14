# Dunders

Dunders (double-underscore methods like `__init__`) are special methods Python calls automatically.

## Defining a class

Any class can define dunders to customize its behavior.

```python
class Person:
```

## The __init__ constructor

`__init__` runs on instantiation to initialize the new object.

```python
    def __init__(self, name):
        self.name = name
```

!!! tip "Common dunders"
    `__init__` sets up instances, `__str__` controls `print(obj)`, `__repr__` controls the debug representation, and `__len__` enables `len(obj)`.
