def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)




# test case
def test():
    # Test with empty strings
    assert same_chars("", "") is True
    # Test with different empty strings
    assert same_chars("", "abc") is False
    # Test with the same string
    assert same_chars("hello", "hello") is True
    # Test with different first strings
    assert same_chars("hello", "world") is False
    # Test with the same second string
    assert same_chars("hello", "hello world") is True
    # Test with different strings of different lengths
    assert same_chars("hello", "a") is False
    # Test with the same strings in reverse order
    assert same_chars("hello", "lohel") is True