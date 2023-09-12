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


# test case
def test():
    
    assert int_to_mini_roman(0) == ""

    assert int_to_mini_roman(1) == "I"
    assert int_to_mini_roman(2) == "II"
    assert int_to_mini_roman(3) == "III"

    assert int_to_mini_roman(4) == "IV"
    assert int_to_mini_roman(5) == "V"
    assert int_to_mini_roman(9) == "IX"

    assert int_to_mini_roman(100) == "CX"
    assert int_to_mini_roman(400) == "CDXC"
    assert int_to_mini_roman