def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))




def test():
    
    assert count_distinct_characters("") == 0


    assert count_distinct_characters("hello") == 5

    assert count_distinct_characters("HeLlO") == 5

    assert count_distinct_characters("The quick brown fox jumps over the lazy dog.") == 10

    assert count_distinct_characters("   hello   ") == 3

    assert count_distinct_characters("Hello, world!") == 8

    assert count_distinct_characters("😊") == 1
#</test>