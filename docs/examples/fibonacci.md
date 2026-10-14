# Fibonacci

Return the n-th Fibonacci number (counting from `nth_fib(1) == 0`).

```python
def nth_fib(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
```

```python
print(nth_fib(10))  # 34
```

!!! tip "Iterative, not recursive"
    A loop keeps this at constant memory. A naive recursive version recomputes the same values and blows up exponentially. Updating both values at once with `a, b = b, a + b` is the tuple-swap idiom — no temporary variable needed.
