# Dataclasses

`@dataclass` generates `__init__`, `__repr__`, and `__eq__` for classes that mostly hold data.

## Basic dataclass

Declare fields with type annotations. No `__init__` to write.

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


p = Point(1.5, 2)
print(p)  # Point(x=1.5, y=2)
print(p == Point(1.5, 2))  # True
```

## Defaults

Fields with defaults must come after fields without. For a mutable default, use `field(default_factory=...)`.

```python
from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    songs: list[str] = field(default_factory=list)
    public: bool = False


a = Playlist('Rock')
a.songs.append('Song 1')
b = Playlist('Pop')
print(a)  # Playlist(name='Rock', songs=['Song 1'], public=False)
print(b.songs)  # [], each instance gets its own list
```

!!! warning "Gotcha: `songs: list = []` is rejected"
    Dataclasses raise `ValueError` for mutable defaults for the same reason [function defaults](functions.md#default-values) are a trap. Use `default_factory`.

## Immutable and orderable

`frozen=True` makes instances read-only (and hashable). `order=True` adds `<`, `>`, ... comparing fields in order.

```python
@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int = 0


v1 = Version(1, 2)
v2 = Version(1, 10)
print(v1 < v2)  # True

try:
    v1.major = 5
except AttributeError as error:
    print(type(error).__name__)  # FrozenInstanceError
```

## Post-init and helpers

`__post_init__` runs right after the generated `__init__` — a good place for validation or derived fields. `asdict()` converts to a plain dict.

```python
from dataclasses import asdict


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        if self.width < 0 or self.height < 0:
            raise ValueError('sides must be >= 0')
        self.area = self.width * self.height


r = Rectangle(2, 3)
print(asdict(r))  # {'width': 2, 'height': 3, 'area': 6}
```

!!! tip "`slots=True` (3.10+)"
    `@dataclass(slots=True)` saves memory and prevents typos like `p.z = 1` from silently creating new attributes.
