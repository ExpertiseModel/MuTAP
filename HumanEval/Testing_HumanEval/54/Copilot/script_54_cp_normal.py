def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return set(s0) == set(s1)


METADATA = {}



 # generate test case for the function above

def test_same_chars():
    assert same_chars("abc", "abc") == True
    assert same_chars("abc", "bac") == True
    assert same_chars("abc", "bca") == True
    assert same_chars("abc", "cab") == True
    assert same_chars("abc", "cba") == True
    assert same_chars("abc", "acb") == True
    assert same_chars("abc", "abb") == False
    assert same_chars("abc", "aab") == False
    assert same_chars("abc", "abb") == False
    assert same_chars("abc", "bbb") == False
    assert same_chars("abc", "abc") == True
    assert same_chars("abc", "bac") == True
    assert same_chars("abc", "bca") == True
    assert same_chars("abc", "cab") == True
   