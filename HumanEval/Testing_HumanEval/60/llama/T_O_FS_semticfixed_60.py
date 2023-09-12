def sum_to_n(n: int):
    
    return sum(range(n + 1))




#</code>
#<test>

def test():
    assert sum_to_n(3) == 6
    assert sum_to_n(4) == 10
    assert sum_to_n(5) == 15
    assert sum_to_n(6) == 21
    assert sum_to_n(7) == 28
    assert sum_to_n(8) == 36
    assert sum_to_n(9) == 45
    assert sum_to_n(10) == 55
