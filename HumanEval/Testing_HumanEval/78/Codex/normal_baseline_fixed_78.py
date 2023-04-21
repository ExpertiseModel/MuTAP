def hex_key(num):
    
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total


def test():
    assert hex_key("100100") == 0
    assert hex_key("101010") == 0
    assert hex_key("404040") == 0
    assert hex_key("606060") == 0
    assert hex_key("808080") == 0
