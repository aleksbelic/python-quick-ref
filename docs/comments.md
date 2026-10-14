# Comments

Comments are lines the Python interpreter ignores. Use them to explain code.

## Single-line comments

Start with `#`. Everything after it on that line is ignored.

```python
# this is a single-line comment
```

## Multi-line comments

Python has no dedicated multi-line comment syntax. Use an unassigned
triple-quoted string — commonly called a docstring when it documents a module,
function, or class.

```python
"""
this
is
a
multi-line
comment
"""
```

## Docstrings

A triple-quoted string placed as the first statement of a module, function, or class becomes its `__doc__` documentation string. Anywhere else, an unassigned string is simply ignored at runtime — effectively a multi-line comment.

Document what a function does, its arguments, and its return value. Tools like `help()` display it.

```python
def greet():
    """Print a greeting."""
    print("Hello!")

print(greet.__doc__)  # Print a greeting.
```

For functions with arguments, document each parameter and the return value. The [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) below is the most common convention:

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
