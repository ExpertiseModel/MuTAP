from script_54_cp_normal import same_chars

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
   