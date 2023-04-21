def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)
def check(candidate):

    assert candidate("abcde","ae") == ('bcd',False)
    assert candidate("abcdef", "b") == ('ac
def test():
    assert reverse_delete("abcdef", "bc") == ('adef',True)
    assert reverse_delete("abcdef", "") == ('abcdef',True)
    assert reverse_delete("plasma", "l") == ('masp',True)
    assert reverse_delete("plasma", "z") == ('plasma',False)
    assert reverse_delete("',.nose'", "nose'") == ("'',.",True)
test()

#print(reverse_delete("abcdef", "bc"))

#print(check(candidate))
`
"""