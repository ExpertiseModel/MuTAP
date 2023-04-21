from script_69_cp_few_shot import search


def test_search():
    assert search([1, 2, 3, 4, 5]) == -1
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert search([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 4
    assert search([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4]) == 4
    assert search([2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4]) == 4

