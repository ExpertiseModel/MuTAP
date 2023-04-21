def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


def test():
    assert reverse_delete("abcdef", "bc") == ('adef',True)
    assert reverse_delete("abcdef", "") == ('abcdef',True)
    assert reverse_delete("plasma", "l") == ('masp',True)
    assert reverse_delete("plasma", "z") == ('plasma',False)
    assert reverse_delete("',.nose'", "nose'") == ("'',.",True)