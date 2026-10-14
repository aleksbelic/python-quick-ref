# Variables

Variables store values under a name. Python creates a variable on assignment — no declaration or type keyword needed.

## Creating variables

Assign with `=`. An `int` needs no quotes, a `str` does.

```python
x = 123
y = 'this is a string'
print(x, y)  # 123 this is a string
```

## Multiple assignment

Assign several names at once, give them the same value, or swap without a temporary variable.

```python
a, b, c = 1, 2, 3  # unpack a tuple of values
p = q = 0  # same value for both names

a, b = b, a  # swap
print(a, b)  # 2 1
```

## Naming

Names may contain letters, digits, and underscores, but cannot start with a digit or be a reserved keyword. The convention (PEP 8) is `snake_case`.

```python
user_name = 'Aleks'  # good
UserName = 'Aleks'  # reserved for class names
# 2nd_place = 3  # SyntaxError: starts with a digit
```

## Constants

Python has no real constants. By convention, an `UPPER_CASE` name means "do not reassign".

```python
MAX_RETRIES = 3
PI = 3.14159
```

!!! tip "Dynamic typing"
    A variable takes the type of the value assigned to it, and can be reassigned to a value of a different type later. [Type hints](type-hints.md) let you document the intended type.
