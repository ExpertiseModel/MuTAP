def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

def test():
    assert circular_shift(1929, 2) == "9219"
    assert 
    assert circular_shift(8892, 3) == "98892"
