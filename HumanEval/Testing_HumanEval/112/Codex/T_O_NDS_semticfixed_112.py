def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)



def test():
    assert reverse_delete("abcdef", "bc") == ('adef', False)
    assert reverse_delete("abcdef", "") == ('abcdef', False)
    assert reverse_delete("plasma", "l") == ('pasma', False)
    assert reverse_delete("plasma", "z") == ('plasma',False)
    assert reverse_delete("',.nose'", "nose'") == (',.', False)
