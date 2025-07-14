# https://en.wikipedia.org/wiki/Fibonacci_sequence

"""
nth_fib(10)  # 34
"""


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
