def test_contains_unique_day():
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 1)]) == True
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 2)]) == False
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 3)]) == False
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 4)]) == False
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 5)]) == False
    assert contains_unique_day(1, [(1, 1), (2, 1), (3, 6)]) == False