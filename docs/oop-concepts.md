# OOP Concepts

The design ideas behind [Classes](classes.md), and how Python's flexible object model implements them: encapsulation, inheritance, polymorphism, and abstraction.

## Encapsulation: conventions, not walls

Encapsulation means keeping an object's internal state behind a small public interface. Python enforces nothing; it relies on naming conventions and on discipline.

| Spelling | Meaning |
| --- | --- |
| `name` | public API |
| `_name` | internal: "please don't use this from outside" |
| `__name` | *name-mangled* to `_ClassName__name` to avoid accidental clashes in subclasses |

```python
class Account:
    def __init__(self):
        self.__balance = 0    # stored as _Account__balance


print(Account().__dict__)  # {'_Account__balance': 0}
```

Name mangling is for avoiding subclass collisions, not for security: anyone can still reach `_Account__balance`. Use [properties](classes.md#properties) to control access to attributes while keeping a plain attribute-style interface.

## Inheritance: "is-a"

A subclass reuses and specialises a parent. Use inheritance when the relationship really is *"a Dog is an Animal"*, and the subclass can stand in anywhere the parent is expected (the **Liskov substitution** idea). `isinstance(obj, Parent)` is true for instances of subclasses, and `issubclass(Sub, Parent)` checks the classes themselves.

## Composition: "has-a"

Often it is better for an object to *hold* other objects than to inherit from them. A `Car` has an `Engine`; it is not a kind of engine.

```python
class Engine:
    def start(self):
        return 'vroom'


class Car:
    def __init__(self):
        self.engine = Engine()    # composition

    def start(self):
        return self.engine.start()
```

**Prefer composition over inheritance** as a default. Inheritance couples a subclass tightly to its parent's internals; composition lets you swap parts and keeps classes small.

## Method resolution order

With several parents, Python needs a deterministic rule to decide which method wins. It computes the **MRO** (method resolution order) with the *C3 linearization* algorithm: children before parents, and the order of the base classes you listed is preserved.

```python
class A:
    def who(self): return 'A'

class B(A):
    def who(self): return 'B'

class C(A):
    def who(self): return 'C'

class D(B, C):
    pass


print([cls.__name__ for cls in D.__mro__])  # ['D', 'B', 'C', 'A', 'object']
print(D().who())                            # B
```

`super()` does **not** mean "my parent": it means "the next class after me in the MRO of the instance's class". That is what makes cooperative multiple inheritance (the "diamond" `D(B, C)`) work, provided every class in the chain calls `super()`.

**Mixins** are small classes that add one behaviour (`LoggingMixin`, `JSONMixin`) and are combined with a main class by multiple inheritance. Keep them free of state of their own.

## Polymorphism and duck typing

Polymorphism: one interface, many implementations. In Python this rarely needs a shared base class, because of **duck typing**. A function that calls `.read()` works with files, `StringIO`, sockets, or your own class, as long as the object has the method. "If it walks like a duck and quacks like a duck, it's a duck."

Method *overriding* (subclass replaces parent behaviour) and the data-model [dunders](dunders.md) (`__len__`, `__iter__`, `__add__`) are the other two forms of polymorphism you use every day.

## Abstract classes and protocols

Sometimes you want to *require* that subclasses provide certain methods.

**Abstract base classes** do this nominally: the class cannot be instantiated until every abstract method is implemented.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Shape()       # TypeError: can't instantiate abstract class
print(Square(3).area())  # 9
```

**Protocols** (`typing.Protocol`) do it structurally and only for type checkers: any class with the right methods *counts* as matching, with no inheritance needed. That is duck typing made explicit for [type hints](type-hints.md).

## `__slots__`

By default each instance stores attributes in a per-instance `__dict__`. Declaring `__slots__ = ('x', 'y')` replaces it with fixed storage: less memory, slightly faster access, and typos such as `p.z = 1` raise `AttributeError`. The trade-offs are no dynamic attributes and some inheritance restrictions. `@dataclass(slots=True)` ([Dataclasses](dataclasses.md)) is the easy way to get it.

## Enumerations

When a value must be one of a fixed set of named options, use `enum.Enum` rather than loose strings or numbers. Members are singletons: compare with `is` or `==`, and typos fail loudly.

```python
from enum import Enum


class Status(Enum):
    ACTIVE = 'active'
    DISABLED = 'disabled'


print(Status('active'))        # Status.ACTIVE
print(Status.ACTIVE.value)     # active
print(Status.ACTIVE is Status('active'))  # True
```

## Classes are objects too

A class is itself an object, an instance of `type` (its *metaclass*). That is why you can pass classes around, store them in dicts, and build new ones at runtime. `@property`, `@staticmethod`, and methods in general work through **descriptors**, objects that customise attribute access on a class. You do not need to write these as a beginner, but knowing they exist explains why `obj.method` is a *bound method* that remembers `obj`.

!!! tip "Design checklist"
    Is it really "is-a"? If unsure, compose. Do callers only need a few methods? Rely on duck typing or a `Protocol`. Need to *force* an interface? Use an ABC. Is it just data? Use a [dataclass](dataclasses.md).
