def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8

def test():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(16) == True
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(-4) == True
    assert is_equal_to_sum_even(-4) == True
    assert is_equal_to_sum_even(2) == False
