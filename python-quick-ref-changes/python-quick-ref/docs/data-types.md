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

## Everything is an object

Every value — numbers, strings, functions, classes, even `None` — is an object with an identity (`id()`), a type (`type()`), and a value. Types decide which operations are allowed; that is why `'1' + 2` fails but `'1' + '2'` works. Python is **dynamically typed** (types belong to values, not names) and **strongly typed** (it will not silently coerce between unrelated types). See [How Python Works](how-python-works.md).

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

`bool` is a subclass of `int`: `True` behaves as `1` and `False` as `0` in arithmetic, which is occasionally handy and occasionally a trap (`isinstance(True, int)` is `True`). More on numbers, rounding, and precision in [Numbers](numbers.md).

## Sequences: `range` and `bytes`

`range(3)` is a lazy, immutable sequence of integers (it does not build a list). `bytes` is an immutable sequence of integers `0–255` — raw data, as opposed to text (`str`). The difference between them is explained in [Text & Encoding](unicode.md).

## Mapping and None types

A `dict` holds key-value pairs; `None` marks the absence of a value. There is exactly one `None` object, which is why identity checks (`x is None`) are the right test.

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
