from script_16_cp_few_shot import count_distinct_characters

def test_count_distinct_characters():
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("a") == 1
    assert count_distinct_characters("aa") == 1
    assert count_distinct_characters("ab") == 2
    assert count_distinct_characters("aba") == 2
    assert count_distinct_characters("Aba") == 2
    assert count_distinct_characters("AbaB") == 3
    assert count_distinct_characters("AbaBa") == 3
    assert count_distinct_characters("AbaBaB") == 3
    assert count_distinct_characters("AbaBaBb") == 4
    assert count_distinct_characters("AbaBaBbB") == 4
    assert count_distinct_characters("AbaBaBbBa") == 4
    assert count_distinct_characters("AbaBaBbBaB") == 4
    assert count_distinct_characters("aA") == 1
    assert count_distinct_characters("aAbB") == 2
    assert count_distinct_characters("aAbBcCdD") == 4
    assert count_distinct_characters("aAbBcCdD123") == 6
    assert count_distinct_characters("aAbBcCdD123!@#") == 9
    assert count_distinct_characters("aAbBcCdD123!@#_") == 10