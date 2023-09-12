def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]


#</code>
#<test>
def test():
    
    assert make_a_pile(3) == [0, 0, 0, 3]
    assert make_a_pile(4) == [0, 0, 0, 4]
    assert make_a_pile(5) == [0, 0, 0, 5]
    assert make_a_pile(6) == [0, 0, 0, 6]
    assert make_a_pile(7) == [0, 0, 0, 7]
    assert make_a_pile(8) == [0, 0, 0, 8]
    assert make_a_pile(9) == [0, 0, 0, 9]
    assert make_a_pile(10) == [0, 0, 0, 10]
#</test>