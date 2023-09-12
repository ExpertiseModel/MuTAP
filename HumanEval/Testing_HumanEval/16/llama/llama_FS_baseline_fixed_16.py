def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))





def test():
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("😊") == 1
