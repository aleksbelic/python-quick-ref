import pytest

from src.practice.is_prime_number import is_prime_number


def test_primes():
    assert is_prime_number(2) is True
    assert is_prime_number(3) is True
    assert is_prime_number(17) is True
    assert is_prime_number(29) is True


def test_non_primes():
    assert is_prime_number(1) is False
    assert is_prime_number(0) is False
    assert is_prime_number(-5) is False
    assert is_prime_number(16) is False
    assert is_prime_number(25) is False


def test_invalid_input():
    with pytest.raises(ValueError):
        is_prime_number(3.14)
    with pytest.raises(ValueError):
        is_prime_number("100")
