# Formatting

Control how values are displayed as strings: decimal places, alignment, separators, and placeholders.

## f-strings

Prefix the string with `f` and put expressions in `{}` (Python 3.6+). Add a format spec after a colon.

```python
x = 1
y = 2
print(f'Sum of {x} and {y} is {x + y}')  # Sum of 1 and 2 is 3

print(f"{3/2:.2f}")  # 1.50
print(f"{3/2:.3f}")  # 1.500
```

## Numbers

```python
n = 1234567.891
print(f'{n:,.2f}')  # 1,234,567.89   thousands separator
print(f'{0.256:.1%}')  # 25.6%   percentage
print(f'{42:05d}')  # 00042   zero padding
print(f'{255:x}')  # ff   hexadecimal
print(f'{5:b}')  # 101   binary
print(f'{1500000:.2e}')  # 1.50e+06   scientific
```

## Width and alignment

`<` left, `>` right, `^` center; an optional fill character comes first.

```python
print(f'[{"left":<8}]')  # [left    ]
print(f'[{"right":>8}]')  # [   right]
print(f'[{"mid":^8}]')  # [  mid   ]
print(f'[{"fill":*^10}]')  # [***fill***]

for name, price in [('apple', 0.5), ('watermelon', 3.25)]:
    print(f'{name:<12}{price:>6.2f}')
# apple         0.50
# watermelon    3.25
```

## Debugging with =

`{value=}` prints the expression *and* its value (3.8+).

```python
width = 7
print(f'{width=}')  # width=7
print(f'{width * 2 = }')  # width * 2 = 14
```

## Conversions

`!r` uses `repr()`, `!s` uses `str()`.

```python
text = 'hi\n'
print(f'{text!r}')  # 'hi\n'
```

## format() with placeholders

`str.format()` is the older style. Empty `{}` fills in argument order.

```python
name = 'Alice'
age = 30
print('My name is {} and I am {} years old.'.format(name, age))
# My name is Alice and I am 30 years old.
```

## format() with positions and names

Numbered `{0}`, `{1}` picks arguments by index; `{name}` picks keyword arguments.

```python
print('My name is {1} and I am {0} years old.'.format(age, name))
# My name is Alice and I am 30 years old.

print('{greeting}, {who}!'.format(greeting='Hello', who='world'))  # Hello, world!
```

!!! tip "f-strings vs format()"
    Prefer f-strings for readability. An f-string is code, fixed when you write it, so it cannot take its template from a variable. Use `format()` (or `string.Template`) when the template text is data that lives elsewhere, such as a config file.

!!! warning "Gotcha: don't use untrusted text as a `format()` template"
    A format template can reach into objects: `'{0.__class__}'.format(obj)` reads an attribute. If a user controls the template, they can probe your objects for sensitive values. Treat templates as trusted input, and pass untrusted text only as an *argument*. Never `eval()` untrusted text to build an f-string.

!!! tip "Format spec cheat sheet"
    The full spec is `[[fill]align][sign][width][,][.precision][type]`, e.g. `{value:*>10,.2f}`. See the [Cheat Sheet](cheatsheet.md#format-specs).
