
def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a




# test case
def test():
    #test_gcd_integer_divisors
    assert greatest_common_divisor(6, 8) == 2
    assert greatest_common_divisor(10, 20) == 5

    #test_gcd_unequal_ integers
    assert greatest_common_divisor(6, -8) == 2
    assert greatest_common_divisor(10, -20) == 5

    #test_gcd_negative_numbers
    assert greatest_common_divisor(-6, 8) == -2
    assert greatest_common_divisor(-10, -20) == -5

    #test_gcd_zero
    assert greatest_common_divisor(0, 8) == 0
    assert greatest_common_divisor(0, -20) == 0

    #test_gcd_empty