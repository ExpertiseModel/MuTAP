def sum_to_n(n: int):
    
    return sum(range(n + 1))




# test case

def test():
    assert sum_to_n(5) == 15
    assert sum_to_n(0) == 0
