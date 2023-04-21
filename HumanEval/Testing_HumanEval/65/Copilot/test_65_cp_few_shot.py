from script_65_cp_few_shot import circular_shift


def test_circular_shift():
    assert circular_shift(123, 1) == "312"
    assert circular_shift(123, 2) == "231"
    assert circular_shift(123, 3) == "123"
    assert circular_shift(123, 4) == "321"
    assert circular_shift(123, 5) == "123"
    assert circular_shift(123, 6) == "312"
    assert circular_shift(123, 7) == "231"
    assert circular_shift(123, 8) == "123"
    assert circular_shift(123, 9) == "321"
    assert circular_shift(123, 10) == "123"
    assert circular_shift(123, 11) == "312"
    assert circular_shift(123, 12) == "231"
    assert circular_shift(123, 13) == "123"
    assert circular_shift(123, 14) == "321"
    assert circular_shift(123, 15) == "123"
    assert circular_shift(123, 16) == "312"
    


