from script_40_cp_few_shot import triples_sum_to_zero


def test_triples_sum_to_zero():
    assert triples_sum_to_zero([]) == False
    assert triples_sum_to_zero([0]) == False
    assert triples_sum_to_zero([0, 0]) == False
    assert triples_sum_to_zero([0, 0, 0]) == True
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([1, 2, 3, -6]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0, 0, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0, 0, 0, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0, 0, 0, 0, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -15, 0, 0, 0, 0, 0, 0]) == True



