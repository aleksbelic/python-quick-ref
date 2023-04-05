from src.practice.fibonacci import nth_fib


def test_nth_gib():
    assert nth_fib(1) == 0
    assert nth_fib(2) == 1
    assert nth_fib(3) == 1
    assert nth_fib(4) == 2
    assert nth_fib(5) == 3
    assert nth_fib(6) == 5
    assert nth_fib(7) == 8
