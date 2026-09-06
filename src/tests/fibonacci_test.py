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
