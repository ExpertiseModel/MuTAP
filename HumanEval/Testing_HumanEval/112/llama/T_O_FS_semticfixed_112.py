def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


#</code>
#<test>

def test():
    # Test with empty strings
    assert reverse_delete("", ["a", "b", "c"]) == ('', True)
    # Test with single char string
    assert reverse_delete("a", ["a", "b", "c"]) == ('', True)
    # Test with two char string
    assert reverse_delete("ab", ["a", "b", "c"]) == ('', True)
    # Test with three char string
    assert reverse_delete("abc", ["a", "b", "c"]) == ('', True)
    # Test with strings that are not reversible
    assert reverse_delete("hello", ["h", "e", "l", "l", "o"]) == ('', True)
