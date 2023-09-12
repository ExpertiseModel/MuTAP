def hex_key(num):
    
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total




def test():
    assert hex_key(2) == 0    
    assert hex_key(3) == 1    
    assert hex_key(5) == 2    
    assert hex_key(7) == 3    
    assert hex_key('B') == 1
    assert hex_key('D') == 1
