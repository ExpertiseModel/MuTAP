def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)




def test():
    assert same_chars("ABC", "ABC") == True
    assert same_chars("ABC", "ABCD") == False
    assert same_chars("ABC", "ABCD") == False
    assert same_chars("ABC", "aBC") == False
    assert same_chars("abc", "ABC") == False
    assert same_chars("abc", "abc") == True
    assert same_chars("abc", "bcd") == False
    assert same_chars("abc", "abcd") == False
