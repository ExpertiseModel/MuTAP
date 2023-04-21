def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)
assert reverse_delete("abcdef", "bc") == ('adef', False)
