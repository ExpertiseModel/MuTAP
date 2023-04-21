def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8


def test():
    assert is_equal_to_sum_even(1) == False
