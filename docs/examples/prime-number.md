# Prime Number

Check whether an integer is prime by testing divisors up to its square root.

```python
def is_prime_number(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    if num <= 1:
        return False

    # if a divisor exists, one of them must be <= sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
```

```python
print(is_prime_number(29))  # True
print(is_prime_number(16))  # False
```

!!! tip "Why only up to the square root?"
    If `n` has a divisor larger than `sqrt(n)`, the matching co-divisor must be smaller than `sqrt(n)` — so checking up to the square root is enough.
