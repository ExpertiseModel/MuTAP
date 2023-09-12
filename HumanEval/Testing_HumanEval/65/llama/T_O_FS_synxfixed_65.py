def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


#</code>
#<test>
def test():
    
    assert circular_shift("hello", 2) == "loeh"
    assert circular_shift("hello", -2) == "hlelo"
    assert circular_shift("hello", 3) == "hlllo"
    assert circular_shift("hello", -3) == "llhoe"
    assert circular_shift("hello", 4) == "hllll"
    assert circular_shift("hello", -4) == "llllo"
    assert circular_shift("hello", 5) == "hlllll"
    assert circular_shift("hello", -5) == "lllllo"