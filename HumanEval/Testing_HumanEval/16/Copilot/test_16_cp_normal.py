from script_16_cp_few_shot import count_distinct_characters

def generate_test_case():
    assert count_distinct_characters("aA") == 1
    assert count_distinct_characters("aAa") == 1
    assert count_distinct_characters("aAaB") == 2
    assert count_distinct_characters("aAaBa") == 2
    assert count_distinct_characters("aAaBaB") == 2
    assert count_distinct_characters("aAaBaBb") == 3
    assert count_distinct_characters("aAaBaBbB") == 3
    assert count_distinct_characters("aAaBaBbBa") == 3
    assert count_distinct_characters("aAaBaBbBaB") == 3
    assert count_distinct_characters("aAaBaBbBaBb") == 4
    assert count_distinct_characters("aAaBaBbBaBbB") == 4
    assert count_distinct_characters("aAaBaBbBaBbBa") == 4
    assert count_distinct_characters("aAaBaBbBaBbBaB") == 4