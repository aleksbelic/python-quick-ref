# Try-Except

Handle runtime errors gracefully with `try` / `except` so one failure doesn't crash the program.

## Catching an error

Code in `try` runs first. If it raises, execution jumps to `except`.

```python
a = '1'
b = 2

try:
    c = a + b
    print(c)
```

## Handling the failure

The `except` block defines the fallback behavior.

```python
except:
    print('Something went wrong')
```

!!! tip "Catch specific exceptions"
    A bare `except:` catches everything, including `KeyboardInterrupt`. Prefer `except TypeError:` or similar so unexpected bugs still surface.
