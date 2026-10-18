# Type Hints

Annotations that document what types a value is expected to have. Python itself ignores them at runtime — editors and checkers such as `mypy` or `pyright` use them to catch bugs early.

## Variables and functions

```python
age: int = 30
name: str = 'Ana'


def greet(name: str, times: int = 1) -> str:
    return ('Hello, ' + name + '! ') * times


print(greet('Ana', 2))
```

## Collections

Since Python 3.9 the built-in collection types are generic: `list[int]`, `dict[str, float]`, `tuple[int, str]`.

```python
scores: list[int] = [90, 85]
prices: dict[str, float] = {'apple': 0.5}
point: tuple[int, int] = (3, 4)
anything: tuple[int, ...] = (1, 2, 3, 4)  # variable length
unique: set[str] = {'a', 'b'}
```

## Optional and unions

`X | Y` (3.10+) means "either type". `X | None` marks a value that may be missing.

```python
def find_user(user_id: int) -> str | None:
    users = {1: 'Ana', 2: 'Ben'}
    return users.get(user_id)


def double(value: int | float) -> int | float:
    return value * 2


print(find_user(1))  # Ana
print(find_user(9))  # None
```

## Callables and Any

```python
from collections.abc import Callable
from typing import Any


def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)


def log(value: Any) -> None:
    print(value)


print(apply(lambda n: n + 1, 41))  # 42
```

## Aliases and classes

Give a complex type a name. Classes are types too, including your own.

```python
Coordinates = tuple[float, float]


def distance_from_origin(point: Coordinates) -> float:
    x, y = point
    return (x ** 2 + y ** 2) ** 0.5


print(distance_from_origin((3, 4)))  # 5.0
```

!!! tip "Python 3.12+: the `type` statement"
    Newer Python can declare aliases with `type Coordinates = tuple[float, float]`.

## Other useful tools

A few more tools from `typing`, so you recognise them when you meet them:

| Tool | Meaning |
| --- | --- |
| `Literal['r', 'w']` | only these exact values |
| `TypedDict` | a dict with a fixed set of named keys |
| `Protocol` | "anything with these methods", structural typing (see [OOP Concepts](oop-concepts.md#abstract-classes-and-protocols)) |
| `TypeVar` / `def f[T](x: T) -> T` | generic functions that keep the type (the bracket syntax is 3.12+) |
| `Final` | this name should never be reassigned |
| `Self` | the instance's own class (3.11+) |

`Optional[X]` is the older spelling of `X | None`; you will see it in existing code.

!!! tip "Python 3.14: annotations are evaluated lazily"
    Before 3.14, an annotation was evaluated when the function or class was defined, so referring to a class defined *later* needed quotes (`'Node'`). From 3.14 annotations are evaluated only when something asks for them, so forward references just work. Type checkers behave the same either way.

## Checking your hints

Hints are not enforced when the program runs:

```python
def add(a: int, b: int) -> int:
    return a + b


print(add('x', 'y'))  # xy, no error at runtime
```

Run a checker to find such mistakes:

```bash
python -m pip install mypy
mypy my_script.py
```

!!! tip "Start small"
    Annotate function signatures first — they give the best payoff. You rarely need to annotate local variables because checkers infer them.
