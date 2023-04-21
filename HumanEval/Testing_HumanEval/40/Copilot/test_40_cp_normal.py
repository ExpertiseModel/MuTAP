from script_40_cp_normal import triples_sum_to_zero

def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([1, 2, -3]) == True
    assert triples_sum_to_zero([1, 2, 3, 4]) == False
    assert triples_sum_to_zero([1, 2, 3, -4]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, -5]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -6]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, -7]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, -8]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, -9]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, -10]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False