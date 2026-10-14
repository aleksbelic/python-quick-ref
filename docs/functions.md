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
