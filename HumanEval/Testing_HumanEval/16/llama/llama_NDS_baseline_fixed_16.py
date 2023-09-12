def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))




# test case

def test():
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("\u0000") == 1
    assert count_distinct_characters("\u00ff") == 1
