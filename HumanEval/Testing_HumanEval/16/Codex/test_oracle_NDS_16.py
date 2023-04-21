def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))



def test():
    assert count_distinct_characters("epam") == 2
    assert count_distinct_characters("EPAm") == 2
    assert count_distinct_characters("EPAM") == 2
    assert count_distinct_characters("Epam") == 2
    
test()
