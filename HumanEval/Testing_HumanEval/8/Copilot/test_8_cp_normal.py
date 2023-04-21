from script_8_cp_few_shot import sum_product

def test_sum_product():
    assert sum_product([1, 2, 3]) == (6, 6)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
    assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720)
    assert sum_product([1, 2, 3, 4, 5, 6, 7]) == (28, 5040)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8]) == (36, 40320)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (45, 362880)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 3628800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (66, 39916800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (78, 479001600)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (91, 6227020800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == (105, 87178291200)