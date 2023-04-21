from script_67_cp_few_shot import fruit_distribution


def test_fruit_distribution():
    assert fruit_distribution("3 apples, 4 oranges", 10) == 3
    assert fruit_distribution("2 apples, 3 oranges", 10) == 5
    assert fruit_distribution("3 apples, 3 oranges", 10) == 4
    assert fruit_distribution("4 apples, 4 oranges", 10) == 2
    assert fruit_distribution("5 apples, 5 oranges", 10) == 0
    assert fruit_distribution("1 apples, 1 oranges", 10) == 8
    assert fruit_distribution("0 apples, 0 oranges", 10) == 10


