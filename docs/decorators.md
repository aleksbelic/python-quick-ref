# Decorators

A decorator wraps a function to add behaviour — logging, timing, caching, access checks — without changing the function's own code.

## The idea

`@decorator` above a `def` is shorthand for `func = decorator(func)`. A decorator is just a function that takes a function and returns a function.

```python
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@shout
def greet(name):
    return f'hello, {name}'


print(greet('aleks'))  # HELLO, ALEKS
```

## Keep the original metadata

The wrapper replaces the function, so its `__name__` and docstring get lost. `functools.wraps` copies them over. Use it in every decorator.

```python
import functools
import time


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'{func.__name__} took {elapsed:.4f}s')
        return result

    return wrapper


@timed
def slow_sum(n):
    """Sum the first n integers."""
    return sum(range(n))


print(slow_sum(100_000))  # prints the timing, then 4999950000
print(slow_sum.__name__)  # slow_sum, thanks to wraps
```

## Decorators with arguments

Add one more level: a function that takes the arguments and returns the actual decorator.

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def ping():
    print('ping')


ping()  # ping, ping, ping
```

## Useful built-in decorators

| Decorator | Purpose |
| --- | --- |
| `@property` | access a method like an attribute (see [Classes](classes.md)) |
| `@classmethod`, `@staticmethod` | methods that don't need an instance |
| `@functools.cache` | memoize results of a pure function |
| `@dataclasses.dataclass` | generate `__init__`, `__repr__`, ... (see [Dataclasses](dataclasses.md)) |

```python
@functools.cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(80))  # 23416728348467685, instant thanks to caching
```

!!! tip "Read decorators from the bottom up"
    With stacked decorators, the one closest to the `def` is applied first.
