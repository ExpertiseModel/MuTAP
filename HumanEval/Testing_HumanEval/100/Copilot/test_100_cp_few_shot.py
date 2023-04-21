from script_100_cp_few_shot import make_a_pile
def test_make_a_pile():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]