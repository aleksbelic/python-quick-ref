# Booleans

Booleans are `True` or `False`. Comparisons produce them, and `bool()` converts any value to one.

## Comparisons

Comparison operators evaluate to a boolean.

```python
print(1 > 2)  # False
print(1 == 2)  # False
print(1 < 2)  # True
```

## Truthy and falsy values

Non-empty strings and non-zero numbers are `True`; empty strings and `0` are `False`.

```python
# bool()
print(bool('Hello'))  # True
print(bool(4))  # True
print(bool(''))  # False
print(bool(0))  # False
```

## Collections and None

A list, tuple, set, or dict is `False` only when empty. `None` and `False` are always `False`.

```python
# bool() of List, Tuple or Set is always True except it's empty
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

print(bool(None))  # False
print(bool(False))  # False
```

!!! tip "Empty means False"
    `if my_list:` is the idiomatic way to check a collection is non-empty —
    no `len()` comparison needed.
