def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
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


METADATA = {}



 # generate test case for the function above

def test_prime_fib():
    assert prime_fib(0) == 2
    assert prime_fib(1) == 3
    assert prime_fib(2) == 5
    assert prime_fib(3) == 13
    assert prime_fib(4) == 89
    assert prime_fib(5) == 233
    assert prime_fib(6) == 1597
    assert prime_fib(7) == 28657
    assert prime_fib(8) == 514229
    assert prime_fib(9) == 433494437
    assert prime_fib(10) == 2971215073
    assert prime_fib(11) == 99194853094755497
    assert prime_fib(12) == 1066340417491710595814572169
    assert prime_fib(13) == 19134702400093278081449423917
    assert prime_fib(14) == 308061521170129
    assert prime_fib(15) == 498454011879264