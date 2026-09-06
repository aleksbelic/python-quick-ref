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