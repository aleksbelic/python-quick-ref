# Practice Examples

Small solved exercises to practice the basics. Each has a pytest suite under `src/tests/` — run them with `pytest`.

## Fibonacci

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

## Palindrome

Check whether a string reads the same forward and backward, ignoring case and non-alphanumeric characters.

```python
def is_palindrome(word: str) -> bool:
    """
    Check if a given string is a palindrome (sequence of alphanumeric characters that reads the same forward and backward).

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    wordWithOnlyAlphanumericCharacters = ''.join(char.lower() for char in word if char.isalnum())
    return wordWithOnlyAlphanumericCharacters == wordWithOnlyAlphanumericCharacters[::-1]
```

```python
is_palindrome("A man, a plan, a canal: Panama!")  # True
is_palindrome("python")                            # False
```

!!! tip "The `[::-1]` trick"
    Slicing with a step of `-1` reverses any sequence — the idiomatic way to compare a string against its mirror.

## Prime Number

Check whether an integer is prime by testing divisors up to its square root.

```python
def is_prime_number(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1, 1): # if a divisor exists, it must be <= sqrt(num)
        if num % i == 0:
            return False

    return True
```

```python
is_prime_number(29)  # True
is_prime_number(16)  # False
```

!!! tip "Why only up to the square root?"
    If `n` has a divisor larger than `sqrt(n)`, the matching co-divisor must be smaller than `sqrt(n)` — so checking up to the square root is enough.
