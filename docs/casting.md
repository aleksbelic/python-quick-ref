# Casting

Casting converts a value from one type to another with `str()`, `int()`, `float()`, and `bool()`.

## Number to string

`str()` turns a number into its text form.

```python
x = str(123)  # 123 -> '123'
```

## String to number

`int()` parses a numeric string. Adding a number to a string directly raises `TypeError`.

```python
y = '78'
# print (1 + y) # ERROR
print(1 + int(y))  # 79
```

## Float and int conversions

`int()` truncates a float toward zero; `float()` adds a decimal part.

```python
z = 3.456
print(int(z))  # 3

my_num = 2
print(float(my_num))  # 2.0
```

## Checking types

`type()` returns the type of a value.

```python
my_bool = "True"
print(type(my_bool))  # <class 'str'>
print(type(bool(my_bool)))  # <class 'bool'>
```

!!! tip "bool() on strings"
    Any non-empty string is truthy — `bool("False")` is `True`. Parse `"True"`/`"False"`
    explicitly instead of relying on `bool()`.
