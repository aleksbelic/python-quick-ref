# Functions

Group reusable logic with `def`. Functions take inputs, run a block, and optionally return a value.

## Defining a function

Use `def` with parameters, and `return` to send a value back to the caller.

```python
def add(a, b):
    return a + b
```

## Calling a function

Call by name with arguments. The return value can be used directly.

```python
print(add(1, 2))  # 3
```

!!! tip "return vs print"
    `return` gives a value back to the caller so it can be stored or reused. `print` only displays it — a function without `return` gives back `None`.

## Returning several values

Return a tuple and unpack it at the call site.

```python
def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([3, 1, 2])
print(low, high)  # 1 3
```

## Default values

Give a parameter a default to make it optional.

```python
def greet(name='world', punctuation='!'):
    return f'Hello, {name}{punctuation}'


print(greet())  # Hello, world!
print(greet('Aleks'))  # Hello, Aleks!
```

!!! warning "Gotcha: mutable default arguments"
    The default is created once, when the function is defined, so a list or dict default is **shared between calls**. Use `None` and create the object inside.

    ```python
    def bad(item, bucket=[]):
        bucket.append(item)
        return bucket


    print(bad(1))  # [1]
    print(bad(2))  # [1, 2], surprise!


    def good(item, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket


    print(good(1))  # [1]
    print(good(2))  # [2]
    ```

## Parameter kinds

A signature can mix four kinds of parameters, in this order: positional-only (before `/`), normal, keyword-only (after `*`), and the collectors `*args` / `**kwargs`.

```python
def example(a, /, b, *, c):
    return a, b, c


print(example(1, 2, c=3))    # (1, 2, 3)
print(example(1, b=2, c=3))  # (1, 2, 3)
# example(a=1, b=2, c=3)     # TypeError: `a` is positional-only
```

Arguments are matched to parameters *by assignment*, exactly like `name = value`. That is why the mutable-default and aliasing rules from [Mutable vs Immutable](mutable-immutable.md) apply to function calls too.

## Keyword arguments

Pass arguments by name in any order. Everything after a bare `*` must be passed by keyword, which makes call sites self-documenting.

```python
def connect(host, *, port=5432, timeout=10):
    return f'{host}:{port} (timeout {timeout}s)'


print(connect('db.local', timeout=3))  # db.local:5432 (timeout 3s)
# connect('db.local', 5433)  # TypeError: port is keyword-only
```

## *args and **kwargs

`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict. The same symbols unpack a list or dict at the call site.

```python
def describe(*args, **kwargs):
    print(args, kwargs)


describe(1, 2, color='red')  # (1, 2) {'color': 'red'}

numbers = [1, 2]
options = {'color': 'blue'}
describe(*numbers, **options)  # (1, 2) {'color': 'blue'}
```

## Docstrings and type hints

Document what a function does, and optionally what types it expects. Hints are not enforced at runtime — see [Type Hints](type-hints.md).

```python
def area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


print(area(2, 3.5))  # 7.0
```

## Scope

Names assigned inside a function are local to it. A function can *read* module-level names, but assigning to one creates a new local variable instead of changing the global. The full lookup rules (LEGB), `nonlocal`, and closures have their own page: [Scope & Closures](scope-closures.md).

```python
x = 'global'


def show():
    x = 'local'  # a new local name, the global is untouched
    print(x)


show()  # local
print(x)  # global
```

!!! tip "Avoid `global`"
    The `global` keyword lets a function rebind a module-level name, but it makes code hard to follow. Pass values in as arguments and return results instead.

## Recursion

A function may call itself. Every recursive function needs a **base case** (stops the recursion) and a **recursive case** that moves toward it. Each call adds a frame to the call stack, and Python caps the depth (about 1000 by default, see `sys.getrecursionlimit()`) and raises `RecursionError` beyond it. Python does not optimise tail calls, so deep recursion is usually better written as a loop. For overlapping subproblems, caching (`functools.cache`) avoids repeated work — see [Complexity & Patterns](complexity.md).

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case


print(factorial(5))  # 120
```

## Lambdas

A `lambda` is a small anonymous function limited to one expression. Mostly used as a `key` argument.

```python
square = lambda n: n ** 2
print(square(4))  # 16

people = [('Ana', 30), ('Ben', 22), ('Cleo', 28)]
print(sorted(people, key=lambda person: person[1]))
# [('Ben', 22), ('Cleo', 28), ('Ana', 30)]
```

## Functions are objects

A function can be stored in a variable, put in a list, passed to another function, or returned from one. This is the basis of [decorators](decorators.md).

```python
def apply_twice(func, value):
    return func(func(value))


print(apply_twice(lambda n: n * 2, 5))  # 20
print(list(map(str.upper, ['a', 'b'])))  # ['A', 'B']
```

!!! tip "Keep functions small"
    A good function does one thing and has a name that says what. If you struggle to name it, it probably does too much.
