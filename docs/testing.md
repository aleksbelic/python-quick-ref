# Testing

Unit tests for the [practice examples](practice/fibonacci.md), written with [pytest](https://pytest.org). Run the whole suite from the project root:

```bash
pytest
```

## Fibonacci tests

Parametrized cases for known values, plus invalid inputs that must raise `ValueError`.

```python
import pytest

from src.practice.fibonacci import nth_fib


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (7, 8),
    ],
)
def test_nth_fib(n, expected):
    assert nth_fib(n) == expected


@pytest.mark.parametrize("invalid_input", [3.14, "100", 0, -1])
def test_nth_fib_rejects_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        nth_fib(invalid_input)
```

## Palindrome tests

Palindromes (including mixed case, punctuation, and empty string), non-palindromes, and a case proving non-alphanumeric characters are ignored.

```python
import pytest

from src.practice.is_palindrome import is_palindrome


@pytest.mark.parametrize(
    "word",
    [
        "racecar",
        "RaceCar",
        "A man, a plan, a canal: Panama!",
        "12321",
        "",
        "Ana voli Milovana"
    ],
)
def test_palindromes(word):
    assert is_palindrome(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "python",
        "racecars",
        "12345",
        "hello world",
    ],
)
def test_non_palindromes(word):
    assert is_palindrome(word) is False


def test_non_alphanumeric_characters_are_ignored():
    assert is_palindrome("!@#r a c e c a r#$%") is True
```

## Prime number tests

Known primes, known non-primes (including `1`, `0`, and negatives), and invalid inputs.

```python
import pytest

from src.practice.is_prime_number import is_prime_number


@pytest.mark.parametrize("num", [2, 3, 17, 29])
def test_primes(num):
    assert is_prime_number(num) is True


@pytest.mark.parametrize("num", [1, 0, -5, 16, 25])
def test_non_primes(num):
    assert is_prime_number(num) is False


@pytest.mark.parametrize("invalid_input", [3.14, "100"])
def test_is_prime_number_rejects_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        is_prime_number(invalid_input)
```

!!! tip "parametrize over copy-paste"
    `@pytest.mark.parametrize` runs one test function against many inputs — one place to extend coverage instead of a new function per case. Use `pytest.raises` to assert that invalid input fails loudly.
