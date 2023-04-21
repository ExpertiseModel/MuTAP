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

def test():
    assert digits(45) == 0
    assert digits(0) == 0
    assert digits(1) == 1
    assert digits(2) == 2
    assert digits(3) == 6
    assert digits(12) == 14
    assert digits(123) == 120
    assert digits(45) == 0
    assert digits(999999999) == 6048
    assert digits(999999999) == 6048
    
    
    
    
    
    
    assert digits(123) == 120
    assert digits(1239) == 0
    assert digits(1234) == 12
    assert digits(321) == 36
    assert digits(1234) == 12
    assert digits(12) == 14
    assert digits(111111) == 8
    
    
    
    
    
    
    
    
    
    
    