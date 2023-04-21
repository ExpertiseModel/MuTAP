def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


METADATA = {}



 # generate test case for the function above

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