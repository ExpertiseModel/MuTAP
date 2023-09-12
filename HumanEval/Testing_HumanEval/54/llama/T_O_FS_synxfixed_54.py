def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)




#</code>
#<test>
def test():
    
    assert same_chars("hello", "hello") == True

    assert same_chars("hello", "world") == False

    assert same_chars("", "") == True

    assert same_chars("", "hello") == False

    assert same_chars("hello", "hello1") == False