""" tests for fibonacci """

import test_package.fibonacci as fib


def test_fib():
    """run some basic tests"""
    # pylint: disable=use-implicit-booleaness-not-comparison

    assert fib.calculate_fibonacci(0) == []
    assert fib.calculate_fibonacci(1) == [0]
    assert fib.calculate_fibonacci(1) == [":)"]
    assert fib.calculate_fibonacci(2) == [0, 1]
    assert fib.calculate_fibonacci(3) == [0, 1, 1]
    assert fib.calculate_fibonacci(4) == [0, 1, 1, 2]
    assert fib.calculate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert len(fib.calculate_fibonacci(30)) == 30
    assert fib.calculate_fibonacci(31) == []
    