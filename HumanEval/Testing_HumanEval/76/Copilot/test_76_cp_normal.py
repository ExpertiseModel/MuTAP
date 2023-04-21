from script_76_cp_normal import is_simple_power

def test_is_simple_power():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(2, 1) == False
    assert is_simple_power(2, 2) == True
    assert is_simple_power(4, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(9, 2) == False
    assert is_simple_power(9, 3) == True
    assert is_simple_power(27, 3) == True
    assert is_simple_power(81, 3) == True
    assert is_simple_power(243, 3) == True
    assert is_simple_power(256, 3) == False
    assert is_simple_power(256, 4) == True
    assert is_simple_power(625, 5) == True
    assert is_simple_power(625, 6) == False
    assert is_simple_power(4096, 4) == True
    