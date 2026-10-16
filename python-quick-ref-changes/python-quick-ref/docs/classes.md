# Classes

Classes are blueprints for objects. They bundle data (attributes) and behavior (methods).

## Class attributes

Attributes defined directly in the class body are shared by all instances.

```python
class Point:
    x = 5
    y = 10


p = Point()
print(p.x)  # 5
```

## Constructor with `__init__`

`__init__` runs when an instance is created. Use `self` to store per-instance data.

```python
class Point:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y


p = Point(7, 11)
print(p.y)  # 11
```

!!! tip "self is the instance"
    The first parameter of instance methods is the instance itself, conventionally named `self`. Python passes it automatically when you call `p.method()`.

## Methods

Functions defined in the class body. They receive the instance as `self`.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor


r = Rectangle(2, 3)
r.scale(2)
print(r.area())  # 24
```

## Inheritance

A subclass reuses and extends a parent class. `super()` calls the parent's version of a method.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '...'


class Dog(Animal):
    def __init__(self, name, tricks):
        super().__init__(name)
        self.tricks = tricks

    def speak(self):  # overrides Animal.speak
        return 'Woof'


d = Dog('Rex', ['sit'])
print(d.name, d.speak())  # Rex Woof
print(isinstance(d, Animal))  # True
```

## Properties

`@property` exposes a method as a read-only attribute (add a setter to validate writes).

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # leading underscore: "internal, hands off"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('radius must be >= 0')
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(2)
print(c.diameter)  # 4
c.radius = 5
print(c.diameter)  # 10
```

## classmethod and staticmethod

`@classmethod` receives the class (`cls`) — handy for alternative constructors. `@staticmethod` receives nothing special and is just a function living in the class namespace.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_valid(celsius):
        return celsius >= -273.15


print(Temperature.from_fahrenheit(212).celsius)  # 100.0
print(Temperature.is_valid(-300))  # False
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

## Attribute lookup

Reading `obj.name` searches the *instance* first, then its class, then the parent classes (in [MRO](oop-concepts.md#method-resolution-order) order). Assigning `obj.name = ...` always writes to the instance, so it *shadows* a class attribute rather than changing it.

```python
class Counter:
    step = 1          # class attribute

c = Counter()
c.step = 10           # creates an instance attribute
print(Counter.step, c.step)  # 1 10
```

Instance data lives in `c.__dict__`; shared data lives in `Counter.__dict__`.

!!! warning "Gotcha: mutable class attributes are shared"
    A list or dict defined in the class body is shared by every instance. Create it in `__init__` instead.

    ```python
    class Bad:
        items = []  # one list for ALL instances


    class Good:
        def __init__(self):
            self.items = []  # one list per instance


    a, b = Bad(), Bad()
    a.items.append(1)
    print(b.items)  # [1], surprise!
    ```

!!! tip "Where next"
    Design ideas — composition vs inheritance, multiple inheritance, abstract classes, "private" attributes — are in [OOP Concepts](oop-concepts.md). For classes that mostly hold data, see [Dataclasses](dataclasses.md). To customise printing, comparison, and operators, see [Dunders](dunders.md).
