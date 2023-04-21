def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range((len(string) + len(substring)) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times


