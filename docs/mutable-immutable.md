# Mutable vs Immutable

Mutable objects can be changed in place. Immutable objects cannot — operations on them create new objects.

## Which is which

| Mutable | Immutable |
| --- | --- |
| `list` | `str` |
| `set` | `tuple` |
| `dict` | `frozenset` |
| most custom classes | `int`, `float`, `bool`, `bytes`, `None` |

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

!!! tip "Why it matters"
    Assignment of a mutable object copies the reference, not the data — mutating one name affects the other. Use `.copy()` or `deepcopy()` when you need independence. Only immutable objects can be dict keys or set members.
