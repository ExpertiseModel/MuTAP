def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times



def test():
    assert how_many_times("hello world", "hello") == 1
    assert how_many_times("hello world", "earth") == 0
    assert how_many_times("hello world", "hello world") == 1
    assert how_many_times("hello world", "o") == 2
    assert how_many_times("hello world", "ll") == 2
    assert how_many_times("hello world", "llow world") == 1
