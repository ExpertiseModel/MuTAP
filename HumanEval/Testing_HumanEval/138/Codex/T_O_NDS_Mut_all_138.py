def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8



def test():

    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(1) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(1) == False
    assert is_equal_to_sum_even(9) == True

    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(1) == False
    assert is_equal_to_sum_even(8) == False
    assert is_equal_to_sum_even(10) == True

