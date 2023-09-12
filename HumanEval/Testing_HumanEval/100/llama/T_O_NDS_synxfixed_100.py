def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]


# test case
def test():
    
    assert make_a_pile(1) == [2, 3, 4, 5, 6]

    assert make_a_pile(2) == [4, 6, 8, 10, 12]

    assert make_a_pile(5) == [10, 15, 20, 25, 30]


    assert make_a_pile(10) == [20, 40, 60, 80, 100]

