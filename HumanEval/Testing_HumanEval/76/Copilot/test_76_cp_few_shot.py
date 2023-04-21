from script_76_cp_few_shot import is_simple_power


def test_is_simple_power():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(2, 1) == False
    assert is_simple_power(1, 2) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(9, 2) == False
    assert is_simple_power(256, 2) == True
    assert is_simple_power(1000, 10) == True
    assert is_simple_power(1001, 10) == False
    assert is_simple_power(1024, 10) == False
    assert is_simple_power(1, 3) == True