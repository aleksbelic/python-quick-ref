# Data Types

Python's built-in types cover text, numbers, sequences, mappings, sets, booleans, binary data, and `None`.

## Type categories

The main built-in types, grouped by kind:

```python
# str - String
# int, float, complex - Numeric
# list, tuple, range - Sequence
# bool - Boolean
# dict - Mapping Type
# set, frozenset - Set Types
# bytes, bytearray, memoryview - Binary Types
# None - NoneType
```

## Checking types with type()

`type()` tells you the type of any value.

```python
x = 4
print(type(x))  # <class 'int'>

y = 'some text'
print(type(y))  # <class 'str'>
```

## Mapping and None types

A `dict` holds key-value pairs; `None` marks the absence of a value.

```python
dictVariable = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dictVariable))  # <class 'dict'>

noneVariable = None
print(type(noneVariable))  # <class 'NoneType'>
```

!!! tip "Use type() to debug"
    When a value behaves unexpectedly, `print(type(value))` is the fastest way to
    confirm whether you hold a `str`, `int`, `dict`, `None`, or something else.
