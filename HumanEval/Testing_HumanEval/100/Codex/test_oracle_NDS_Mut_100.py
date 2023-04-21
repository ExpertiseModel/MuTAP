def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]

def test():
    make_a_pile(2) == [4, 6]
    make_a_pile(1) == [4]
    make_a_pile(0) == []
    make_a_pile(3) == [6, 8, 10]
