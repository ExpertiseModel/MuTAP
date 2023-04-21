def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


METADATA = {}



 # generate test case for the function above

def test_fibfib():
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 7
    assert fibfib(7) == 13
    assert fibfib(8) == 24
    assert fibfib(9) == 44
    assert fibfib(10) == 81
    assert fibfib(11) == 149
    assert fibfib(12) == 274
    assert fibfib(13) == 504
    assert fibfib(14) == 927
    assert fibfib(15) == 1705