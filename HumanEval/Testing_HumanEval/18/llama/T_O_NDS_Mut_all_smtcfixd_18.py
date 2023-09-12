def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times




# test case


def test():
    ## Test 1: Positive case
    assert how_many_times("hello world", "world") == 1

    ## Test 2: Negative case
    assert how_many_times("hello", "lions") == 0

   ## Test 3: Edge case
    assert how_many_times("hello world ABC", "world") == 1

   ## Test 4: Edge case
    assert how_many_times("hello world ABC", "ABC") == 1

    assert how_many_times("hello", "lions") == 0
    assert how_many_times("hello world", "world") == 1

