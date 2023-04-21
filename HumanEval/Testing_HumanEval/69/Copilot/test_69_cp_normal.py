from script_69_cp_normal import search

def test_search():
    assert search([1, 1, 1, 2, 2, 3]) == 1
    assert search([1, 2, 3, 4]) == -1
    assert search([1, 1, 2, 2]) == 2
    assert search([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]) == 3
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 2