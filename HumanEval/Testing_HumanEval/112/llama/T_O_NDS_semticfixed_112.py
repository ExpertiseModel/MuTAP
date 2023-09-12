def reverse_delete(s,c):
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


# test case

def test():
    # Test with different input strings and characters
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    # Test with a longer string
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)

# Test with a different character to delete
    assert reverse_delete("abcde", "ef") == ('abcd', False)

# Test with multiple characters to delete
    assert reverse_delete("abcdef", "ab cd") == ('ef', False)

# Test with an empty string
    assert reverse_delete("", "a") == ('', True)


