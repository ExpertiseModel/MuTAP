from script_115_cp_few_shot import max_fill
def test_max_fill():
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 1) == 6
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 2) == 3
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 3) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 4) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 5) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 6) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 7) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 8) == 2
    assert max_fill([[0,0,0],[1,0,1],[1,1,1]], 9) == 2
