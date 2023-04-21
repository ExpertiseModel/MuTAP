def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

def test():
    assert circular_shift(10, 2)==12
    assert circular_shift(10, -2)==8
    assert circular_shift(1, 2) == 3
    assert circular_shift(4, 3) == 7
    assert circular_shift(41, 3) == 43
    assert circular_shift(41, -3) == 37
    assert circular_shift(1000000000001, 3) == 1000000000003
    assert circular_shift(1000000000001, -3) == 1000000000027
    return 'Congratulations !'
test()
