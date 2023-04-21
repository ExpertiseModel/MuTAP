from script_102_cp_few_shot import choose_num
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(13, 13) == -1
    assert choose_num(13, 14) == 14
    assert choose_num(13, 15) == 14
    assert choose_num(13, 16) == 16