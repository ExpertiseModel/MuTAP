def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]


METADATA = {}



 # generate test case for the function above

def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 6
    assert fib4(7) == 8
    assert fib4(8) == 10
    assert fib4(9) == 14
    assert fib4(10) == 18
    assert fib4(11) == 26
    assert fib4(12) == 34
    assert fib4(13) == 50
    assert fib4(14) == 68
    assert fib4(15) == 98
    assert fib4(16) == 138
    assert fib4(17) == 198
    assert fib4(18) == 278
    assert fib4(19) == 398
    assert fib4(20) == 558