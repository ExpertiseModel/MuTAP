def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)



def test():
    assert fib(0) == 0
    print(fib(1)) 
    assert fib(1) == 1
    print(fib(2)) 
    assert fib(2) == 1
    print(fib(3)) 
    assert fib(3) == 2
    print(fib(4)) 
    assert fib(4) == 3
    print(fib(5)) 
    assert fib(5) == 5
    print(fib(6))