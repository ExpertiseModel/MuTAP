from script_115_cp_normal import max_fill
def test_max_fill():
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 1) == 5
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 2) == 3
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 3) == 2
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 4) == 2
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 5) == 1
