def triples_sum_to_zero(l: list):
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False




# test case
def test():

   #test_triples_sum_negative():
    assert triples_sum_to_zero([1, -2, -3, 0]) is True

    #test_triples_sum_nonzero():
    assert triples_sum_to_zero([1, 2, 3, 4]) is False, "Triple sum should not be zero when at least one element is non-zero"

    assert triples_sum_to_zero([0, 0, 0]) is True, "Triple sum should be zero when all elements are zero"
