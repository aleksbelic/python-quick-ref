# Syntax Basics

The ground rules of Python source code: comments, indentation, statements, and docstrings.

## Single-line comments

Start with `#`. Everything after it on that line is ignored by the interpreter.

```python
# this is a single-line comment
x = 1  # ...or a comment at the end of a line
```

## Multi-line comments

Python has no dedicated multi-line comment syntax. Either put `#` on every line, or use an unassigned triple-quoted string, which Python evaluates and throws away.

```python
# several lines,
# several hashes

"""
this
is
a
multi-line
string used as a comment
"""
```

## Docstrings

A triple-quoted string placed as the first statement of a module, function, or class becomes its `__doc__` documentation string. Tools like `help()` display it.

```python
def greet():
    """Print a greeting."""
    print("Hello!")


print(greet.__doc__)  # Print a greeting.
```

For functions with arguments, document each parameter and the return value. The [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) is a common convention:

```python
def is_palindrome(word: str) -> bool:
    """Check if a word reads the same forward and backward.

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
```

!!! tip "Comment the why, not the what"
    `x += 1  # increment x` adds nothing — the code already says that.
    Explain intent instead: `x += 1  # skip the header row`.

## Indentation

Blocks are defined by indentation, not braces. Indent 4 spaces after a colon to open a block, dedent to close it. Mixing tabs and spaces raises an `IndentationError`.

```python
if True:
    print("indented block runs")  # 4 spaces
print("dedented, always runs")
```

## Statements and semicolons

A newline ends a statement; no semicolon needed. A semicolon only joins several statements on one line, which is discouraged.

```python
x = 1         # no semicolon needed
a = 1; b = 2  # valid, but avoid: one statement per line
```

To continue a statement over several lines, wrap it in parentheses (or brackets/braces):

```python
total = (
    1
    + 2
    + 3
)
print(total)  # 6
```

## pass

`pass` is a no-op placeholder for blocks that must exist syntactically but do nothing yet.

```python
if 3 > 6:
    pass  # TODO: handle this case


def not_implemented_yet():
    pass
```

!!! tip "`...` also works"
    `...` (Ellipsis) is a common alternative to `pass` for stub functions and classes.
