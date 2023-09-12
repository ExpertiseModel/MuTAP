def int_to_mini_roman(number):
    
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()


#</code>
#<test>
def test():
    assert int_to_mini_roman(1) == "I"
    # Test 2: Small input
    assert int_to_mini_roman(2) == "II"
    # Test 3: Large input
    assert int_to_mini_roman(1000) == "M"
    # Test 4: Negative input
    assert int_to_mini_roman(-1) == ""
    # Test 5: Non-integer input
    assert int_to_mini_roman(2.5) == ""
   
    assert int_to_mini_roman(1) == "I"

    assert int_to_mini_roman(4) == "IV"

    assert int_to_mini_roman(5) == "V"

    assert int_to_mini_roman(9) == "IX"

    assert int_to_mini_roman(10) == "X"
