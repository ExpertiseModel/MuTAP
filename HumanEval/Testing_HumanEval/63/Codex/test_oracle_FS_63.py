def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)



def test():

def test():
    assert fibfib(1) == 0
    assert fibfib(2) == 0
    assert fibfib(3) == 1
    assert fibfib(4) == 1
    assert fibfib(5) == 1
    assert fibfib(6) == 2
    assert fibfib(7) == 3
    assert fibfib(8) == 5
    assert fibfib(9) == 8
    assert fibfib(10) == 34
    assert fibfib(11) == 89
    assert fibfib(12) == 233
    assert fibfib(13) == 610
    assert fibfib(14) == 1597
    assert fibfib(15) == 4181
    assert fibfib(16) == 6765
    assert fibfib(17) == 10946
    assert fib