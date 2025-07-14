# https://en.wikipedia.org/wiki/Prime_number

"""
is_prime_number(29) # True
is_prime_number(16) # False
"""


def is_prime_number(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1, 1): # if a divisor exists, it must be <= sqrt(num)
        if num % i == 0:
            return False

    return True
