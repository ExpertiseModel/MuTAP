from script_49_cp_few_shot import modp



def test_modp():
    assert modp(0, 2) == 1
    assert modp(1, 2) == 0
    assert modp(2, 2) == 0
    assert modp(3, 2) == 0
    assert modp(4, 2) == 0
    assert modp(5, 2) == 0
    assert modp(0, 5) == 1
    assert modp(1, 5) == 5
    assert modp(2, 5) == 4
    assert modp(3, 5) == 3
    assert modp(4, 5) == 1
    assert modp(5, 5) == 2
    assert modp(12, 3) == 1
    assert modp(13, 3) == 2
    assert modp(14, 3) == 1
    assert modp(15, 3) == 2


