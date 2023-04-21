from script_53_cp_few_shot import add


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5
     assert add(0, 0) == 0
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(2, 2) == 4
    assert add(2, 3) == 5
    assert add(3, 3) == 6
    assert add(3, 4) == 7
    assert add(4, 4) == 8
    assert add(4, 5) == 9
    assert add(5, 5) == 10
    assert add(5, 6) == 11
    assert add(6, 6) == 12



