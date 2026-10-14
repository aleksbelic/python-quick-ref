# Conditions

Branch execution with `if`, `elif`, and `else` based on a boolean expression. Booleans are `True` or `False`; comparisons produce them, and `bool()` converts any value to one.

## If / elif / else

Only the first branch whose condition is true runs. `else` catches everything else.

```python
if 1 > 2:
    print('1 is greater than 2')
elif 1 == 2:
    print('1 equals 2')
else:
    print('1 is less than 2')
```

!!! tip "Indentation matters"
    Branches are defined by indentation, not braces. See [Syntax Basics](syntax.md#indentation).

## Comparisons

Comparison operators evaluate to a boolean.

```python
print(1 > 2)  # False
print(1 == 2)  # False
print(1 < 2)  # True
```

## Truthy and falsy values

Non-empty strings and non-zero numbers are `True`; empty strings and `0` are `False`.

```python
print(bool('Hello'))  # True
print(bool(4))  # True
print(bool(''))  # False
print(bool(0))  # False
```

A list, tuple, set, or dict is `False` only when empty. `None` and `False` are always `False`.

```python
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

print(bool(None))  # False
print(bool(False))  # False
```

!!! tip "Empty means False"
    `if my_list:` is the idiomatic way to check a collection is non-empty — no `len()` comparison needed.

## Combining conditions

Use `and`, `or`, and `not`; add parentheses when mixing them.

```python
age = 30
has_ticket = True

if age >= 18 and has_ticket:
    print('Welcome in')

if not (age < 18 or not has_ticket):
    print('Same check, written differently')
```

## Conditional expression

A one-line `if`/`else` that produces a value.

```python
age = 20
status = 'adult' if age >= 18 else 'minor'
print(status)  # adult
```

## match (3.10+)

`match` compares a value against patterns. It is more powerful than a chain of `elif` — it can also destructure sequences and objects.

```python
def handle(command):
    match command.split():
        case ['go', direction]:
            return f'Going {direction}'
        case ['quit' | 'exit']:
            return 'Bye'
        case [verb, *rest]:
            return f'Unknown: {verb} with {len(rest)} argument(s)'
        case _:
            return 'Empty command'


print(handle('go north'))  # Going north
print(handle('quit'))  # Bye
print(handle('jump high now'))  # Unknown: jump with 2 argument(s)
print(handle(''))  # Empty command
```

!!! warning "Gotcha: don't compare to `True`/`None` with `==`"
    Write `if flag:` instead of `if flag == True:`, and `if x is None:` instead of `if x == None:`.
