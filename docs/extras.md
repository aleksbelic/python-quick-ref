# Extras

Small utilities that come up everywhere: no-op blocks, repetition, ranges, f-strings, identity, and clean exits.

## pass

`pass` is a no-op placeholder for empty blocks.

```python
a, b, c = 1, 2, 3

if 3 > 6:
    pass  # do nothing
```

## String repetition

Multiply a string to repeat it.

```python
print('Hello' * 3)
# HelloHelloHello
```

## range()

`range(start, stop)` counts up to — but not including — `stop`.

```python
for num in range(1, 3):  # upper limit is not included
    print(num)
'''
1
2
'''
```

## f-strings

Embed expressions directly in string literals (Python 3.6+).

```python
# F-STRINGS (Formatted string literals, since Python 3.6.)
x = 1
y = 2
print(f'Sum of {x} and {y} is {x + y}')  # Sum of 1 and 2 is 3
```

## Object id: references vs copies

Assignment copies the reference. `id()` reveals whether two names point to the same object; `.copy()` makes an independent one.

```python
# OBJECT ID
l1 = [1, 2, 3]
l2 = l1  # by reference, no copy
print(id(l1) == id(l2))  # True
l3 = l2.copy()  # copy, no reference
print(id(l2) == id(l3))  # False
```

## Exiting a script

Stop execution with `sys.exit()`.

```python
import sys

sys.exit(0)  # stop program execution (quit() is REPL-only, use sys.exit() in scripts)
```

!!! tip "quit() vs sys.exit()"
    `quit()` is a REPL helper. In scripts, always use `sys.exit()` with a status code (`0` for success).

## Semicolons

Lines do not end with a semicolon — a newline terminates the statement. A semicolon only joins multiple statements on one line, which is discouraged.

```python
x = 1  # no semicolon needed
a = 1; b = 2  # valid but avoid: one statement per line
```
