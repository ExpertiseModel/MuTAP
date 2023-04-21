def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))





def test():
    assert count_distinct_characters("epam") == 4
    assert count_distinct_characters("EPAm") == 4
    assert count_distinct_characters("EPAM") == 4
    assert count_distinct_characters("Epam") == 4
