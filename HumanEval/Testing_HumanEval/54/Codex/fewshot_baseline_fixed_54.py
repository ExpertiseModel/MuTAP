def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)




def test():
    assert same_chars("abc", "abc") == True
    assert same_chars("abc", "abx") == False
    assert same_chars("abc", "abcd") == False
    assert same_chars("abc", "abbc") == True
