def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


#</code>
#<test>

def test():
    assert circular_shift("hello", 2) == "lohel"
    assert circular_shift("hello", -2) == "hello"
    assert circular_shift("hello", 3) == "llohe"
    assert circular_shift("hello", -3) == "hello"
    assert circular_shift("hello", 4) == "elloh"
    assert circular_shift("hello", -4) == "hello"
    assert circular_shift("hello", 5) == "hello"
    assert circular_shift("hello", -5) == "hello"