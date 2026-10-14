# Fibonacci

Return the n-th Fibonacci number (counting from `nth_fib(1) == 0`).

```python
def nth_fib(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    i = 2
    while True:
        c = a + b
        i += 1
        if i == n:
            return c
        else:
            a = b
            b = c
```

```python
nth_fib(10)  # 34
```

!!! tip "Iterative, not recursive"
    A loop keeps this at constant memory. A naive recursive version recomputes the same values and blows up exponentially.
