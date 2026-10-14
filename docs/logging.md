# Logging

Record what a program is doing with the `logging` module instead of scattering `print()` calls. Levels let you turn detail up or down without editing code.

## Levels

From least to most severe: `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`. Only messages at or above the configured level are shown (the default is `WARNING`).

## Basic setup

`basicConfig()` configures the root logger once, at program start.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
)

logger = logging.getLogger(__name__)

logger.debug('not shown, below INFO')
logger.info('starting up')
logger.warning('disk space is low')
logger.error('could not open file')
```

## One logger per module

Create a logger with `logging.getLogger(__name__)` at the top of each module. Its name shows where a message came from, and you can tune each module separately.

## Logging exceptions

`logger.exception()` logs at `ERROR` level and appends the traceback. Call it inside an `except` block.

```python
try:
    1 / 0
except ZeroDivisionError:
    logger.exception('calculation failed')
```

## Logging to a file

Add a `filename` to `basicConfig`, or attach handlers for several destinations.

```python
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

logger.warning('this goes to the console and to app.log')
```

## Lazy formatting

Pass values as arguments instead of building the string yourself. The text is only formatted when the message is actually emitted.

```python
user = 'ana'
logger.info('user %s logged in', user)
```

!!! tip "print() vs logging"
    Use `print()` for a program's *output* (what the user asked for). Use `logging` for *diagnostics* (what the program is doing), which goes to stderr by default.

!!! tip "Libraries never configure logging"
    Only the application calls `basicConfig()`. Library code just creates a logger and logs; the application decides where it goes.
