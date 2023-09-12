def hex_key(num):
    
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total


# test case

def test():
    assert hex_key('123') == 2

    assert hex_key('2B') == 2

    assert hex_key('2F') == 1

    assert hex_key(-5) == 0
    assert hex_key('') == 0

    assert hex_key('1234567890abcdef') == 4

    assert hex_key('123') == 2

