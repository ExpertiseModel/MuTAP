from script_66_cp_normal import digitSum

def test_digitSum():
    assert digitSum("") == 0
    assert digitSum("a") == 0
    assert digitSum("A") == 65
    assert digitSum("1") == 0
    assert digitSum("aA") == 65
    assert digitSum("a1") == 0
    assert digitSum("A1") == 65
    assert digitSum("aA1") == 65
    assert digitSum("aA1a") == 65
    assert digitSum("aA1A") == 130
    assert digitSum("aA1Aa") == 130