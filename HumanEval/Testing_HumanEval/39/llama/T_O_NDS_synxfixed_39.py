def prime_fib(n: int):
    
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]




# test case
def test():
    assert prime_fib(3) == 2
    assert prime_fib(4) == 1
    assert prime_fib(5) == 1

    assert prime_fib(10) == 5

    assert prime_fib(100) == 594
    assert prime_fib(1000) == 59364

    assert prime_fib(2) == 1
    assert prime_fib(3) == 2
    assert prime_fib(4) == 1

    assert prime_fib(0) == 1
    assert prime_fib(-1) == 0
    assert prime_fib(1) == 1
