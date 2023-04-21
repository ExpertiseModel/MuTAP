from script_15_cp_few_shot import string_sequence

def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(2) == '0 1 2'
    assert string_sequence(3) == '0 1 2 3'
    assert string_sequence(4) == '0 1 2 3 4'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(6) == '0 1 2 3 4 5 6'
    assert string_sequence(7) == '0 1 2 3 4 5 6 7'
    assert string_sequence(8) == '0 1 2 3 4 5 6 7 8'
    assert string_sequence(9) == '0 1 2 3 4 5 6 7 8 9'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'