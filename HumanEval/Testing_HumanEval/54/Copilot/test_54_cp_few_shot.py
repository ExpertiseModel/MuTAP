from script_54_cp_few_shot import same_chars


def test_same_chars():
    assert same_chars("", "") == True
    assert same_chars("a", "a") == True
    assert same_chars("ab", "ab") == True
    assert same_chars("ab", "ba") == True
    assert same_chars("abc", "cba") == True
    assert same_chars("abc", "def") == False
    assert same_chars("abc", "ab") == False
    assert same_chars("abc", "abcd") == False
    assert same_chars("abc", "abcde") == False
    assert same_chars("abc", "abcc") == False
    assert same_chars("abc", "abcc") == False


