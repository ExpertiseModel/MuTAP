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
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 7
    assert fibfib(7) == 13

# Test cases for large values of `n`
    assert fibfib(8) == 24
    assert fibfib(9) == 44
    assert fibfib(10) == 81

# Test cases for very large values of `n`
    assert fibfib(11) == 149
    assert fibfib(12) == 274
    assert fibfib(13) == 504

