def digits(n):
    
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product


# test case

def test():
    # Test with positive integer input
    assert digits(123) == 3
    # Test with negative integer input
    assert digits(-123) == 0    # Test with non-integer input
    assert digits("hello") == 0    # Test with very large input
    assert digits(1234567890) == 945
    # Test with very large input 2
    assert digits(12345678901234567890) == 893025

