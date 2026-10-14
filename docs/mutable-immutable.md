# Mutable vs Immutable

Mutable objects can be changed in place. Immutable objects cannot — operations on them create new objects.

## Mutable types

Lists, sets, and dicts can be modified after creation.

```python
# MUTABLE - can be changed:
# List [1, 2, 3]
# Set {1, 2, 3}
# Dictionary {1: 'one', 2: 'two', 3: 'three'}
```

## Immutable types

Strings, tuples, and frozensets cannot be changed in place.

```python
# IMMUTABLE - can't be changed:
# String 'abc'
# Tuple (1, 2, 3)
# frozenset({1, 2, 3})
```

!!! tip "Why it matters"
    Assignment of a mutable object copies the reference, not the data — mutating one name affects the other. Pass immutables (or explicit `.copy()`) when you need independence.
