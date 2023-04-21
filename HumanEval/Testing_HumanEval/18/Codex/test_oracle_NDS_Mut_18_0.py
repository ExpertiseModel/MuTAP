def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times





def test():
    assert how_many_times("The cow jumped over the moon", "cow") == 1
    assert how_many_times("The cow jumped over the moon", "the") == 1
    assert how_many_times("The cow jumped over the moon", "cow jump") == 1
    assert how_many_times( "The cow jumped over the moon", "moon") == 1
    assert how_many_times( "The cow jumped over the moon", "The cow jumped") == 1
    assert how_many_times( "The cow jumped over the moon", "The cow") == 1
    assert how_many_times( "The cow jumped over the moon", "cow the") == 0
    assert how_many_times( "The cow jumped over the moon", "cow" "jumped") == 1
    assert how_many_times( "The cow jumped over the moon", "cow