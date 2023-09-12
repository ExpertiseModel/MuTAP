def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]


#</code>
#<test>

def test():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]
    assert make_a_pile(9) == [9, 11, 13, 15, 17, 19, 21, 23, 25]
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#</test>
