from script_102_cp_few_shot import choose_num
def test_choose_num():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 2) == -1
    assert choose_num(2, 3) == 2
    assert choose_num(2, 4) == 4
    assert choose_num(2, 5) == 4
    assert choose_num(2, 6) == 6
