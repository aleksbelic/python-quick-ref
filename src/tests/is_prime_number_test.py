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
