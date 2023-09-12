def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)




# test case


def test():
    assert fibfib(3) == 1

    assert fibfib(1) == 0
    assert fibfib(2) == 1
    assert fibfib(3) == 1
    assert fibfib(4) == 2

