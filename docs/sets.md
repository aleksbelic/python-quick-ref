# Sets

Unordered collections using `{}` with no duplicates. Duplicates are silently ignored, and membership tests are fast.

## Creating sets

Order is not guaranteed; each element appears only once.

```python
s1 = {'Mr', 'Mrs', 'Miss', 'Mr'}
print(len(s1))  # 3, duplicate is being ignored
```

!!! warning "Gotcha: `{}` is an empty dict"
    Use `set()` to create an empty set.

    ```python
    print(type({}))  # <class 'dict'>
    print(type(set()))  # <class 'set'>
    ```

## Adding and removing

`add()` inserts one item. `remove()` raises `KeyError` if the item is missing; `discard()` does not.

```python
colors = {'red', 'green'}
colors.add('blue')
colors.discard('purple')  # no error
colors.remove('green')
print(sorted(colors))  # ['blue', 'red']
```

## Set operations

Combine sets like in math.

```python
a = {1, 2, 3}
b = {3, 4}

print(a | b)  # {1, 2, 3, 4}, union
print(a & b)  # {3}, intersection
print(a - b)  # {1, 2}, difference
print(a ^ b)  # {1, 2, 4}, in one set but not both
print({1, 2} <= a)  # True, subset
```

## Membership and deduplication

`in` on a set is much faster than on a list for large collections.

```python
allowed = {'admin', 'editor'}
print('admin' in allowed)  # True

numbers = [1, 2, 2, 3, 3, 3]
unique = list(set(numbers))
print(sorted(unique))  # [1, 2, 3]
```

## Why sets are fast

Sets are hash tables: each element's `hash()` decides where it is stored, so membership tests jump straight to the right slot. That is also why elements must be hashable — see [Mutable vs Immutable](mutable-immutable.md#hashability-what-can-be-a-key) and [Complexity](complexity.md).

## frozenset

An immutable set — hashable, so it can be a dict key or a member of another set.

```python
fs = frozenset({1, 2, 3})
print(fs)  # frozenset({1, 2, 3}) (element order may vary)
```

!!! tip "Deduplication trick"
    `set(my_list)` removes duplicates but loses order. To keep order, use `list(dict.fromkeys(my_list))`.
