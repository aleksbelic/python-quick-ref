# Formatting

Control how values are displayed as strings: decimal places, placeholders, and positional arguments.

## f-strings

Prefix the string with `f` and put expressions in `{}`. Format floats with `:.Nf` for `N` decimals.

```python
# f-string (Python 3.6+)
print(f"{3/2:.2f}") # 1.50
print(f"{3/2:.3f}") # 1.500
```

## format() with placeholders

Empty `{}` fills in argument order.

```python
name = 'Alice'
age = 30
print('My name is {} and I am {} years old.'.format(name, age))
# My name is Alice and I am 30 years old.
```

## format() with positions

Numbered `{0}`, `{1}` picks arguments by index.

```python
print('My name is {1} and I am {0} years old.'.format(age, name))
# My name is Alice and I am 30 years old.
```

!!! tip "f-strings vs format()"
    Prefer f-strings for readability. Use `format()` when the template string comes from elsewhere (config, file, user input).
