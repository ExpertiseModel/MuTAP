from script_67_cp_normal import fruit_distribution

def test_fruit_distribution():
    assert fruit_distribution("3 4", 7) == 0
    assert fruit_distribution("2 3", 5) == 0
    assert fruit_distribution("1 2", 3) == 0
    assert fruit_distribution("4 5", 9) == 0
    assert fruit_distribution("5 6", 11) == 0
    assert fruit_distribution("6 7", 13) == 0
    assert fruit_distribution("7 8", 15) == 0
    assert fruit_distribution("8 9", 17) == 0
    assert fruit_distribution("9 10", 19) == 0
    