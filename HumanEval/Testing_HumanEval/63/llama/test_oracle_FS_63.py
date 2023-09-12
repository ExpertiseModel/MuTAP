def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)




#</code>
#<test>
def test():
    
# Test cases for small values of `n`
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1
    assert fibfib(3) == 1

# Test cases for intermediate values of `n`
    assert fibfib(4) == 1
    assert fibfib(5) == 2
    assert fibfib(6) == 3
    assert fibfib(7) == 4

# Test cases for large values of `n`
    assert fibfib(8) == 5
    assert fibfib(9) == 8
    assert fibfib(10) == 13

# Test cases for very large values of `n`
    assert fibfib(11) == 100
    assert fibfib(12) == 122
    assert fibfib(13) == 161
