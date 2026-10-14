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

!!! tip "Docstrings vs comments"
    A triple-quoted string placed as the first statement of a module, function,
    or class becomes its `__doc__` documentation string. Anywhere else, an
    unassigned string is simply ignored at runtime — effectively a multi-line
    comment.
