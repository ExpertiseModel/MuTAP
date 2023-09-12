def sum_to_n(n: int):
    
    return sum(range(n + 1))




# test case

def test():
    # Test with a positive integer
    assert sum_to_n(5) == 15

    # Test with zero
    assert sum_to_n(0) == 0

    # Test with a negative integer
    assert sum_to_n(-5) == 0

    # Test with an odd positive integer
    assert sum_to_n(7) == 28

    # Test with an even positive integer
    assert sum_to_n(10) == 55

    # Test with a float
    assert sum_to_n(3.14) == 15