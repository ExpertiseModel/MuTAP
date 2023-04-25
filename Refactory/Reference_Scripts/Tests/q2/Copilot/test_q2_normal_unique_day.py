def generate_test_case():
    assert unique_day(1, ((1, 1), (2, 1), (3, 1))) == True
    assert unique_day(1, ((1, 1), (2, 1), (3, 1), (4, 1))) == False
    assert unique_day(1, ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1))) == False
    assert unique_day(1, ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1))) == False
    assert unique_day(1, ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1))) == False