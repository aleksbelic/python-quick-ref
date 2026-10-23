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
| Bitwise | `&` `|` `^` `~` `<<` `>>` (see [Numbers](numbers.md#bitwise-operators)) |
| Walrus | `:=` assignment expression |

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

## Operator precedence

When an expression mixes operators, higher rows bind tighter. When in doubt, add parentheses — readers will thank you.

| Precedence (high → low) | Operators |
| --- | --- |
| 1 | `(...)` grouping |
| 2 | `x[i]`, `x.attr`, `f(...)` |
| 3 | `**` (right-associative: `2 ** 3 ** 2` is `2 ** 9`) |
| 4 | unary `+x`, `-x`, `~x` |
| 5 | `*` `/` `//` `%` |
| 6 | `+` `-` |
| 7 | `<<` `>>` |
| 8 | `&`, then `^`, then `|` |
| 9 | comparisons, `in`, `is` (all equal, and chainable) |
| 10 | `not` |
| 11 | `and`, then `or` |
| 12 | `lambda`, then `x if c else y` |
| 13 | `:=` (walrus) — needs parentheses: `if (n := len(x)) > 2:` |

!!! warning "Gotcha: `-2 ** 2` is `-4`"
    `**` binds tighter than unary minus, so this means `-(2 ** 2)`. Write `(-2) ** 2` for `4`.

## The walrus operator

`:=` (3.8+) assigns *and* yields the value inside an expression. It avoids computing something twice in a condition.

```python
data = [4, 8, 15]
if (n := len(data)) > 2:
    print(f'{n} items')  # 3 items
```

## No `===` operator

Unlike JavaScript, Python has no triple-equals. Comparison splits into two operators:

```python
x = [1, 2]
y = [1, 2]

print(x == y)  # True, same contents (value equality)
print(x is y)  # False, different objects (identity)
```

Use `==` for values. Use `is` only for identity checks — conventionally just `None`. Comparing numbers or strings with `is` can *appear* to work because CPython reuses some small objects, but that is an implementation detail you must not rely on.

```python
print(x is None)  # False
```
