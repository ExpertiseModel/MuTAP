def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)



def test():
    assert fibfib(1) == 1
    assert fibfib(2) == 1
    assert fibfib(3) == 2
    assert fibfib(4) == 3
    assert fibfib(5) == 5
    assert fibfib(6) == 8
    assert fibfib(7) == 13
    assert fibfib(8) == 21
    assert fibfib(9) == 34
    assert fibfib(10) == 55
    assert fibfib(11) == 89
    assert fibfib(12) == 144
    assert fibfib(13) == 233
    assert fibfib(14) == 377
    assert fibfib(15) == 610
    assert fibfib(16) == 987
    assert fibfib(17) == 1597
    assert fibfib(18) == 25