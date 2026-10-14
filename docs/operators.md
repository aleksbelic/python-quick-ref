# Operators

Arithmetic, comparison, assignment, and logical operators for numbers and conditions.

## Arithmetic operators

`+ - / // * ** %` cover addition through modulo, floor division, and power.

```python
"""
+ - / // * ** %
+= -= /= *=
== >= <=
and or not
"""
```

## Division

`/` always returns a float, `//` floors to whole-number division.

```python
# Division is by default never an integer
print(10 / 5)  # 2.0, FLOAT!
print(10 / 3)  # 3.3333333333333335

# Division without remainder
print(10 // 5)  # 2, INT!
print(10 // 3)  # 3
```

## Power

Use `**` for exponents.

```python
# Math power
print(10 ** 2)  # 100
```

!!! tip "Float division by default"
    In Python 3, `10 / 5` is `2.0`, not `2`. Use `//` when you want integer division.

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
