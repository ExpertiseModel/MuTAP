def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))




# test case

def test():
    # Valid strings should return a correct count of distinct characters
    assert count_distinct_characters("hello") == 4
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("hello world") == 8

    # The function should return 0 for an empty string
    assert count_distinct_characters("") == 0

    # Special characters should be handled correctly
    assert count_distinct_characters("\u0000") == 1
    assert count_distinct_characters("\u00ff") == 1

    # Lowercase and uppercase strings should be handled correctly
    assert count_distinct_characters("HeLlo") == 4
    assert count_distinct_characters("hello") == 4
    assert count_distinct_characters("HELLO WORLD") == 8
    assert count_distinct_characters("HELLO") == 8

