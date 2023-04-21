def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)



def test():

    assert reverse_delete('ABCDEFG','FG') == ('ABCDE', False)
    assert reverse_delete("ABCDEFG", "") == ('ABCDEFG', False)
    assert reverse_delete("ABCDEFG", "E") == ('ABCDFG', False)
    assert reverse_delete("ABCDEFG", "z") == ('ABCDEFG',False)
    assert reverse_delete("',.nose'", "nose'") == (',.', False)

