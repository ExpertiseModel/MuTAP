def test_search():
    assert search(1, [1, 2, 3]) == 0
    assert search(2, [1, 2, 3]) == 1
    assert search(3, [1, 2, 3]) == 2
    assert search(4, [1, 2, 3]) == 3
    assert search(0, [1, 2, 3]) == 0
    assert search(1, [1, 2, 3, 4]) == 0
    assert search(2, [1, 2, 3, 4]) == 1
    assert search(3, [1, 2, 3, 4]) == 2
    assert search(4, [1, 2, 3, 4]) == 3
    assert search(5, [1, 2, 3, 4]) == 4
