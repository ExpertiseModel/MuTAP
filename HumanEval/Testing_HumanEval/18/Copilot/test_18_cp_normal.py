from script_18_cp_few_shot import how_many_times

def test_how_many_times():
    assert how_many_times("abc", "a") == 1
    assert how_many_times("abc", "b") == 1
    assert how_many_times("abc", "c") == 1
    assert how_many_times("abc", "ab") == 1
    assert how_many_times("abc", "bc") == 1
    assert how_many_times("abc", "abc") == 1
    assert how_many_times("abc", "abcd") == 0
    assert how_many_times("abc", "bcde") == 0
    assert how_many_times("abc", "abcde") == 0
    assert how_many_times("abc", "aabc") == 1
    assert how_many_times("abc", "abbc") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0
    assert how_many_times("abc", "abca") == 0
    assert how_many_times("abc", "abcb") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0
    assert how_many_times("abc", "abca") == 0
    assert how_many_times("abc", "abcb") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0