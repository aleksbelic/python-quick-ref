# Classes

Classes are blueprints for objects. They bundle data (attributes) and behavior (methods).

## Class attributes

Attributes defined directly in the class body are shared by all instances.

```python
class Point():
    x = 5
    y = 10


p = Point()
print(p.x)  # 5
```

## Constructor with __init__

`__init__` runs when an instance is created. Use `self` to store per-instance data.

```python
class Point():
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y


p = Point(7, 11)
print(p.y)  # 11
```

## Introspection

Every object knows its class. Use `__class__`, `type()`, and `__name__` to inspect it.

```python
p = Point(2, 5)

print(p.__class__)
# <class '__main__.Point'>

print(type(p))
# <class '__main__.Point'>

print(type(p).__name__)
# Point

print(p.__class__.__name__)
# Point
```

!!! tip "self is the instance"
    The first parameter of instance methods is the instance itself, conventionally named `self`. Python passes it automatically when you call `p.method()`.
