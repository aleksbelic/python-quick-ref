import pytest

from src.practice.fibonacci import nth_fib


def test_nth_fib():
    assert nth_fib(1) == 0
    assert nth_fib(2) == 1
    assert nth_fib(3) == 1
    assert nth_fib(4) == 2
    assert nth_fib(5) == 3
    assert nth_fib(6) == 5
    assert nth_fib(7) == 8

def test_invalid_input():
    with pytest.raises(ValueError):
        nth_fib(3.14)
    with pytest.raises(ValueError):
        nth_fib("100")
    with pytest.raises(ValueError):
        nth_fib(0)
    with pytest.raises(ValueError):
        nth_fib(-1)
