def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8


#</code>
#<test>
def test():

    assert is_equal_to_sum_even(8) == True

    assert is_equal_to_sum_even(7) == False

    assert is_equal_to_sum_even(7) == False

    assert is_equal_to_sum_even(100) = True
    assert is_equal_to_sum_even(2) == True
    assert is_equal_to_sum_even(3) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(5) == True