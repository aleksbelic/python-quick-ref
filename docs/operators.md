# Operators

Arithmetic, comparison, assignment, logical, and membership operators.

## Overview

| Kind | Operators |
| --- | --- |
| Arithmetic | `+` `-` `*` `/` `//` `%` `**` |
| Assignment | `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` |
| Comparison | `==` `!=` `>` `<` `>=` `<=` |
| Logical | `and` `or` `not` |
| Identity | `is` `is not` |
| Membership | `in` `not in` |

## Division

`/` always returns a float, `//` floors to whole-number division, `%` gives the remainder.

```python
# Division is by default never an integer
print(10 / 5)  # 2.0, FLOAT!
print(10 / 3)  # 3.3333333333333335

# Division without remainder
print(10 // 5)  # 2, INT!
print(10 // 3)  # 3

print(10 % 3)  # 1
print(divmod(10, 3))  # (3, 1) quotient and remainder at once
```

## Power

Use `**` for exponents.

```python
print(10 ** 2)  # 100
print(2 ** -1)  # 0.5
```

!!! tip "Float division by default"
    In Python 3, `10 / 5` is `2.0`, not `2`. Use `//` when you want integer division.

## Augmented assignment

Shorthand for "update this variable using its own value".

```python
n = 10
n += 5  # n = n + 5
n *= 2  # n = n * 2
print(n)  # 30
```

## Comparison chaining

Comparisons can be chained, which reads like math.

```python
age = 25
print(18 <= age < 65)  # True, same as: 18 <= age and age < 65
```

## Logical operators

`and`, `or`, `not` combine booleans. They short-circuit: the right side is only evaluated when needed. `or` is often used to supply a default.

```python
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

name = ''
print(name or 'anonymous')  # anonymous
```

## Membership

`in` tests whether a value is contained in a string, list, tuple, set, or dict (keys).

```python
print('a' in 'cat')  # True
print(3 in [1, 2, 3])  # True
print('x' not in {'x': 1})  # False
```

## No `===` operator

Unlike JavaScript, Python has no triple-equals. Comparison splits into two operators:

```python
x = [1, 2]
y = [1, 2]

print(x == y)  # True, same contents (value equality)
print(x is y)  # False, different objects (identity)
```

Use `==` for values. Use `is` only for identity checks — conventionally just `None`:

```python
print(x is None)  # False
```
