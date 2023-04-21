def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))





def test():

    assert count_distinct_characters("coffee") == 4
    assert count_distinct_characters("starwARS") == 5
    assert count_distinct_characters("starwars") == 5
    assert count_distinct_characters("Starwars") == 5
    assert count_distinct_characters("starwARS") == 5
    assert count_distinct_characters("starwars") == 5
    assert count_distinct_characters("Starwars") == 5
    assert count_distinct_characters("") == 0
    assert count_distinct_characters(1) == 0
    assert count_distinct_characters(None) == 0

