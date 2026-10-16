# Mutable vs Immutable

Mutable objects can be changed in place. Immutable objects cannot — operations on them create new objects.

## Which is which

| Mutable | Immutable |
| --- | --- |
| `list` | `str` |
| `set` | `tuple` |
| `dict` | `frozenset` |
| `bytearray` | `bytes`, `range` |
| most custom classes | `int`, `float`, `bool`, `complex`, `None` |

Python 3.15 adds a built-in immutable mapping, `frozendict` — see [What's New](modern-python.md).

## Names are references

A variable is a name that points to an object. Assignment makes a second name point to the *same* object; `id()` and `is` reveal this.

```python
l1 = [1, 2, 3]
l2 = l1  # by reference, no copy
print(id(l1) == id(l2))  # True
print(l1 is l2)  # True

l3 = l2.copy()  # copy, no reference
print(id(l2) == id(l3))  # False

l1.append(4)
print(l2)  # [1, 2, 3, 4], changed through the other name
print(l3)  # [1, 2, 3], unaffected
```

## Immutable objects "change" by being replaced

```python
s = 'abc'
before = id(s)
s += 'd'  # builds a new string and rebinds the name
print(id(s) == before)  # False
```

## Shallow vs deep copy

`.copy()` copies only the outer container; nested mutable objects are still shared. `copy.deepcopy()` copies everything.

```python
import copy

nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)

nested[0].append(99)
print(shallow)  # [[1, 2, 99], [3, 4]], inner list is shared
print(deep)  # [[1, 2], [3, 4]], fully independent
```

## Passing objects to functions

Functions receive references too: mutating an argument changes the caller's object, while rebinding the parameter does not.

```python
def add_item(items):
    items.append('x')  # mutates the caller's list


def reset(items):
    items = []  # only rebinds the local name


data = ['a']
add_item(data)
reset(data)
print(data)  # ['a', 'x']
```

!!! warning "Gotcha: mutable default arguments"
    A default value is created once, when the function is defined — so a mutable default is shared between calls. See [Functions](functions.md#default-values).

## Hashability: what can be a key

Dict keys and set members must be **hashable**: they have a `hash()` value that never changes during their lifetime, and equal objects have equal hashes. The hash is what lets a dict or set jump straight to the right slot instead of scanning (see [Complexity](complexity.md)).

Immutable *and* hashable are not the same thing. A tuple is hashable only if everything inside it is.

```python
print(hash((1, 2)))      # works
# hash((1, [2]))         # TypeError: unhashable type: 'list'
```

A custom class is hashable by default (hash from identity), until you define `__eq__` without `__hash__` — see [Dunders](dunders.md).

!!! tip "Why it matters"
    Assignment of a mutable object copies the reference, not the data — mutating one name affects the other. Use `.copy()` or `deepcopy()` when you need independence. Dict keys and set members must be hashable, which in practice means immutable.
