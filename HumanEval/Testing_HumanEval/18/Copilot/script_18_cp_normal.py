def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times






 # generate test case for the function above

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