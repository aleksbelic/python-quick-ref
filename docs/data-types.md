# Data Types

Python's built-in types cover text, numbers, sequences, mappings, sets, booleans, binary data, and `None`.

## Type categories

The main built-in types, grouped by kind:

| Kind | Types |
| --- | --- |
| Text | `str` |
| Numeric | `int`, `float`, `complex` |
| Sequence | `list`, `tuple`, `range` |
| Mapping | `dict` |
| Set | `set`, `frozenset` |
| Boolean | `bool` |
| Binary | `bytes`, `bytearray`, `memoryview` |
| Nothing | `None` (`NoneType`) |

## Checking types

`type()` tells you the exact type of a value. `isinstance()` checks against a type (or a tuple of types) and also accepts subclasses, so it is the better choice in conditions.

```python
x = 4
print(type(x))  # <class 'int'>

y = 'some text'
print(type(y))  # <class 'str'>

print(isinstance(x, int))           # True
print(isinstance(x, (int, float)))  # True
```

## Numbers

`int` has unlimited size. Underscores make big literals readable. `float` is a 64-bit binary float.

```python
big = 1_000_000_000_000_000_000_000
print(big * 2)  # 2000000000000000000000

print(type(3.14))    # <class 'float'>
print(type(2 + 3j))  # <class 'complex'>
```

!!! warning "Gotcha: floats are not exact"
    Binary floats cannot represent most decimals exactly. Compare with `math.isclose()`, or use `decimal.Decimal` for money.

    ```python
    import math
    from decimal import Decimal

    print(0.1 + 0.2 == 0.3)                 # False
    print(math.isclose(0.1 + 0.2, 0.3))     # True
    print(Decimal('0.1') + Decimal('0.2'))  # 0.3
    ```

## Mapping and None types

A `dict` holds key-value pairs; `None` marks the absence of a value.

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
print(type(car))      # <class 'dict'>

nothing = None
print(type(nothing))  # <class 'NoneType'>
```

!!! tip "Use type() to debug"
    When a value behaves unexpectedly, `print(type(value))` is the fastest way to confirm whether you hold a `str`, `int`, `dict`, `None`, or something else.
