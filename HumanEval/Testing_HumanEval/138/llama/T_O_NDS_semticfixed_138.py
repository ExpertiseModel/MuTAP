def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8


# test case

def test():
    # Test positive numbers
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False

    # Test negative numbers
    assert is_equal_to_sum_even(-2) == False
    assert is_equal_to_sum_even(-4) == False
    assert is_equal_to_sum_even(-6) == False

    # Test larger numbers
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True

    # Test even numbers that cannot be written as sum of 4 even numbers
    assert is_equal_to_sum_even(24) == True
    assert is_equal_to_sum_even(26) == True

    # Test odd numbers
    
