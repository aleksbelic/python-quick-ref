# Dunders

Dunders (double-underscore methods like `__init__`) are special methods Python calls automatically in response to syntax and built-in functions.

## Common dunders

| Method | Triggered by |
| --- | --- |
| `__init__(self, ...)` | creating an instance: `Person('Ana')` |
| `__str__(self)` | `print(obj)`, `str(obj)`, f-strings |
| `__repr__(self)` | debugging representation, `repr(obj)`, the REPL |
| `__eq__(self, other)` | `obj == other` |
| `__lt__(self, other)` | `obj < other` (enables sorting) |
| `__add__(self, other)` | `obj + other` |
| `__len__(self)` | `len(obj)` |
| `__getitem__(self, key)` | `obj[key]` (and basic iteration) |
| `__contains__(self, item)` | `item in obj` |
| `__bool__(self)` | `if obj:` |
| `__iter__(self)`, `__next__(self)` | `for x in obj`, `next(obj)` (see [Iterators](iterators.md)) |
| `__call__(self, ...)` | `obj(...)`: makes an instance callable |
| `__enter__(self)`, `__exit__(...)` | `with obj:` (see [Context Managers](context-managers.md)) |
| `__hash__(self)` | `hash(obj)`, dict keys, set members |

## The `__init__` constructor

`__init__` runs on instantiation to initialize the new object.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

## `__str__` and `__repr__`

`__str__` is for humans, `__repr__` is for developers: ideally unambiguous, often looking like the code that creates the object. Without them you get `<__main__.Person object at 0x...>`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person {self.name}'

    def __repr__(self):
        return f'Person({self.name!r})'


p = Person('Ana')
print(p)        # Person Ana
print(repr(p))  # Person('Ana')
print([p])      # [Person('Ana')], containers use "repr"
```

## Comparison and arithmetic

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented  # lets Python try the other operand, then raise TypeError
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)
print(Vector(1, 2) == Vector(1, 2))  # True
```

## The data model idea

Dunders are Python's **data model**: the built-in functions and operators are thin wrappers that call these methods (`len(x)` calls `type(x).__len__(x)`). Implement the right dunders and your class plugs into the language — it works with `for`, `in`, `sorted()`, `with`, and so on — without inheriting from anything. This is *duck typing* in action ([OOP Concepts](oop-concepts.md#polymorphism-and-duck-typing)). You almost never call a dunder directly.

## Container behaviour

Implement `__len__` and `__getitem__` and your class behaves like a sequence: `len()`, indexing, slicing, `in`, and `for` all work.

```python
class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]


playlist = Playlist(['a', 'b', 'c'])
print(len(playlist))    # 3
print(playlist[1])      # b
print('c' in playlist)  # True
for song in playlist:
    print(song)
```

!!! warning "Gotcha: defining `__eq__` removes `__hash__`"
    A class that defines `__eq__` without `__hash__` becomes unhashable, so it can't be a dict key or set member. Add `__hash__` too, or use a frozen [dataclass](dataclasses.md).

!!! tip "Always define `__repr__`"
    A good `__repr__` makes debugging and test failures far easier to read. If you only write one dunder besides `__init__`, make it that one.
