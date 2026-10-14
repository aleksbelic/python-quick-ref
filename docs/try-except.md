# Try–Except

Handle runtime errors gracefully with `try` / `except` so one failure doesn't crash the program.

## Catching an error

Code in `try` runs first. If it raises, execution jumps to a matching `except`.

```python
a = '1'
b = 2

try:
    c = a + b
    print(c)
except TypeError:
    print('Cannot add a string and a number')
```

## Catching specific exceptions

Name the exceptions you expect. Use `as` to get the exception object, and a tuple to handle several the same way.

```python
def parse_age(text):
    try:
        return int(text)
    except ValueError as error:
        print('Not a number:', error)
    except (TypeError, OverflowError):
        print('Wrong kind of input')


parse_age('abc')  # Not a number: invalid literal for int() with base 10: 'abc'
parse_age(None)  # Wrong kind of input
```

## else and finally

`else` runs only when `try` raised nothing. `finally` always runs — even after a `return` or an unhandled error — so it is the place for clean-up.

```python
try:
    number = int('42')
except ValueError:
    print('bad input')
else:
    print('parsed', number)  # runs: no exception
finally:
    print('always runs')
```

## Raising exceptions

Use `raise` to signal a problem. Re-raise inside `except` with a bare `raise`.

```python
def set_age(age):
    if age < 0:
        raise ValueError('age cannot be negative')
    return age


try:
    set_age(-1)
except ValueError as error:
    print(error)  # age cannot be negative
```

## Custom exceptions

Subclass `Exception` to give your errors a meaningful name.

```python
class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f'need {amount - balance} more')
    return balance - amount


try:
    withdraw(10, 25)
except InsufficientFundsError as error:
    print(error)  # need 15 more
```

## Common exceptions

| Exception | Typical cause |
| --- | --- |
| `ValueError` | right type, wrong value: `int('abc')` |
| `TypeError` | wrong type: `'1' + 2` |
| `KeyError` | missing dict key |
| `IndexError` | list index out of range |
| `AttributeError` | attribute does not exist |
| `FileNotFoundError` | file or folder does not exist |
| `ZeroDivisionError` | `1 / 0` |

!!! tip "Catch specific exceptions"
    A bare `except:` catches everything, including `KeyboardInterrupt`. Prefer `except TypeError:` — or at least `except Exception:` — so unexpected bugs still surface.

!!! tip "Ask forgiveness, not permission"
    Python style (EAFP) prefers trying the operation and handling the error over checking every precondition first: `try: value = d[key]` rather than `if key in d: ...`.
