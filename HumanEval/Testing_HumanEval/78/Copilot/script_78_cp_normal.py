def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    """
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total

 # generate test case for the function above

def test_hex_key():
    assert hex_key('') == 0
    assert hex_key('1') == 0
    assert hex_key('2') == 1
    assert hex_key('3') == 1
    assert hex_key('4') == 0
    assert hex_key('5') == 1
    assert hex_key('6') == 0
    assert hex_key('7') == 1
    assert hex_key('8') == 0
    assert hex_key('9') == 0
    assert hex_key('A') == 0
    assert hex_key('B') == 1
    assert hex_key('C') == 0
    assert hex_key('D') == 1
    assert hex_key('E') == 0
    