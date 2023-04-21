from script_100_cp_few_shot import make_a_pile
def test_make_a_pile():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    assert make_a_pile(15) == [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    assert make_a_pile(20) == [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
