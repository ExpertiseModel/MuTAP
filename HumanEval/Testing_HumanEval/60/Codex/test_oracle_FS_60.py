def sum_to_n(n: int):
    
    return sum(range(n + 1))



def test():
    assert sum_to_n(1) == 1
    assert sum_to_n(2) == 3
    assert sum_to_n(4) == 10


