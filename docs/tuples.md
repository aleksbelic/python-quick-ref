# Tuples

Ordered, immutable collections using `()`. Allow duplicates and mixed data types.

## Creating tuples

Like lists, but cannot be changed after creation.

```python
t1 = ('Mr', 'Mrs', 'Miss')
print(len(t1))  # 3
print(t1[0])  # Mr

t2 = ('Mr', 123, 'Miss')
print(t2)  # ('Mr', 123, 'Miss')
```

!!! warning "Gotcha: one-element tuples need a comma"
    `(5)` is just the number `5` in parentheses. The comma makes the tuple.

    ```python
    print(type((5)))  # <class 'int'>
    print(type((5,)))  # <class 'tuple'>
    ```

## Immutability

Items cannot be assigned, added, or removed.

```python
t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as error:
    print(error)  # 'tuple' object does not support item assignment
```

## Unpacking

Assign each item to a name. Functions use this to return several values.

```python
point = (3, 4)
x, y = point
print(x, y)  # 3 4


def min_max(numbers):
    return min(numbers), max(numbers)  # a tuple


low, high = min_max([3, 1, 2])
print(low, high)  # 1 3
```

## Tuples as dictionary keys

Because they are immutable (and hashable), tuples can be dictionary keys — lists cannot.

```python
distances = {('Berlin', 'Paris'): 878}
print(distances[('Berlin', 'Paris')])  # 878
```

!!! tip "When to use tuples"
    Use a tuple for fixed data that should never change — e.g. coordinates, record fields, or dictionary keys. For records with named fields, see `namedtuple` in [Collections](collections.md) or [Dataclasses](dataclasses.md).
