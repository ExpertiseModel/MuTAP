def fib(n: int):
    """Return n-th Fibonacci number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


METADATA = {}



 # generate test case for the function above

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55
    assert fib(11) == 89
    assert fib(12) == 144
    assert fib(13) == 233
    assert fib(14) == 377
    assert fib(15) == 610
   