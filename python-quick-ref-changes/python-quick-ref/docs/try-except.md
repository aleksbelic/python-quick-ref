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

## Exception hierarchy

Exceptions form a class tree, and `except` matches a class *and all its subclasses*. That is why order matters: put specific handlers before general ones.

```text
BaseException
├── KeyboardInterrupt, SystemExit, GeneratorExit
└── Exception
    ├── ArithmeticError  (ZeroDivisionError, OverflowError)
    ├── LookupError      (KeyError, IndexError)
    ├── OSError          (FileNotFoundError, PermissionError, ...)
    ├── ValueError       (UnicodeError, json.JSONDecodeError)
    ├── TypeError, AttributeError, NameError, ImportError, ...
    └── RuntimeError     (RecursionError, NotImplementedError)
```

Catching `Exception` leaves `KeyboardInterrupt` and `SystemExit` alone, which is why it is a safer "catch-all" than a bare `except:`. Custom exceptions should inherit from `Exception` (or a more specific class).

## Exception chaining

Raising inside an `except` block links the new error to the old one automatically (`__context__`). Use `raise ... from ...` to say "this was *caused by* that", or `from None` to hide the original.

```python
def load_port(text):
    try:
        return int(text)
    except ValueError as error:
        raise RuntimeError(f'bad port setting: {text!r}') from error
```

The traceback then shows both errors, which makes the real cause visible. `error.add_note('...')` (3.11+) attaches extra context to an exception without changing its type.

## Exception groups and `except*`

Available since Python 3.11. Concurrent code can fail in several ways at once. An `ExceptionGroup` bundles multiple exceptions, and `except*` handles each kind separately. You will meet them mostly through [`asyncio.TaskGroup`](concurrency.md).

```python
try:
    raise ExceptionGroup('batch', [ValueError('a'), TypeError('b')])
except* ValueError as group:
    print('values:', group.exceptions)
except* TypeError as group:
    print('types:', group.exceptions)
```

Python 3.14 also allows listing several exception types without parentheses when there is no `as` (`except ValueError, TypeError:`). Parentheses remain valid and are clearer for beginners.

## Assertions

`assert condition, message` raises `AssertionError` when the condition is false. Use it for *programmer errors* ("this can never happen"), not for validating user input, because assertions are removed when Python runs with `-O`.

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
    Python style (EAFP: "easier to ask forgiveness than permission") prefers trying the operation and handling the error over checking every precondition first: `try: value = d[key]` rather than `if key in d: ...`. The opposite style is LBYL ("look before you leap"). EAFP avoids race conditions (a file can vanish between your check and your `open()`) and reads naturally when failure is the exception rather than the rule.

!!! tip "Keep the `try` block small"
    Wrap only the line that can raise the error you expect. A large `try` body can swallow an unrelated bug and report it as the wrong problem.
