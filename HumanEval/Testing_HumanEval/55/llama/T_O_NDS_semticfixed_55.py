def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)




# test case

def test():
    assert fib(0) == 0

    assert fib(1) == 1

    assert fib(3) == fib(2) + fib(1)

    assert fib(-3) == fib(-2) + fib(-1)
    assert fib(10) == 55
