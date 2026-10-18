# Context Managers

The `with` statement: guaranteed setup and clean-up around a block of code, even when an error occurs.

## The problem

Many resources must be released: files closed, locks released, temporary changes undone, database transactions committed or rolled back. Doing this by hand with `try`/`finally` works but is easy to forget and noisy to read.

A **context manager** packages the "acquire" and "release" steps so the `with` statement can apply them for you.

```python
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write('hello')
# the file is closed here, whether or not write() raised
```

`with` is equivalent to a `try`/`finally` that always calls the clean-up step.

## The protocol

An object works in a `with` statement if it has two methods:

| Method | When it runs |
| --- | --- |
| `__enter__(self)` | at the start of the block; its return value is bound by `as` |
| `__exit__(self, exc_type, exc, traceback)` | at the end, always, receiving the exception details if the block failed |

If `__exit__` returns a true value, the exception is **suppressed**; otherwise it propagates normally. Most context managers return `None` (or `False`) so errors are not hidden.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, traceback):
        import time
        self.elapsed = time.perf_counter() - self.start
        return False   # do not swallow exceptions
```

## Writing one with `contextlib`

A generator can express the same idea more briefly with `@contextlib.contextmanager`: code before `yield` is the setup, code after it is the clean-up, and `try`/`finally` makes the clean-up unconditional.

```python
from contextlib import contextmanager


@contextmanager
def changed_directory(path):
    import os
    old = os.getcwd()
    os.chdir(path)
    try:
        yield            # the with-block runs here
    finally:
        os.chdir(old)    # always restore
```

## Useful ready-made ones

| Tool | Purpose |
| --- | --- |
| `open(...)` | closes the file |
| `contextlib.suppress(Err)` | ignore a specific exception |
| `contextlib.closing(obj)` | call `obj.close()` on exit |
| `contextlib.ExitStack` | manage a dynamic number of contexts |
| `threading.Lock()` | acquire and release a lock (see [Concurrency](concurrency.md)) |
| `tempfile.TemporaryDirectory()` | a folder that is deleted afterwards |
| `decimal.localcontext()` | temporarily change arithmetic settings |

## Several at once

List several context managers in one `with`. They are exited in **reverse order**, like nested blocks. Parentheses allow splitting over lines (3.10+).

```python
with (
    open('in.txt', encoding='utf-8') as source,
    open('out.txt', 'w', encoding='utf-8') as target,
):
    target.write(source.read())
```

!!! tip "When to reach for `with`"
    Whenever something must be undone: files, network connections, locks, temporary state, timing, test fixtures. If you find yourself writing `finally:` just to call a clean-up method, you probably want a context manager.
