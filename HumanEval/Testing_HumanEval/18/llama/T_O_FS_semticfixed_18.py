def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times




def test():
    assert how_many_times("", "abc") == 0

    assert how_many_times("hello", "ello") == 1

    assert how_many_times("hello", "hellohellohello") == 0

    assert how_many_times("hello", "elloabc") == 0

    assert how_many_times("hellohellohello", "ello") == 3

    assert how_many_times("hello", "") == 6

    assert how_many_times("hello", "-ello") == 0

    assert how_many_times("", "a") == 0


    assert how_many_times("a", "a") == 1



    assert how_many_times("abcdefg", "abc") == 1


    assert how_many_times("abcdefg", "hijklmnop") == 0


