def triples_sum_to_zero(l: list):
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False





def test():
    assert triples_sum_to_zero([1, 2, 3, 4, 5]) == False


    assert triples_sum_to_zero([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == False


    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False


    assert triples_sum_to_zero([1, 2, 3]) == False


    assert triples_sum_to_zero([1, -2, 3]) == False


    assert triples_sum_to_zero([1, 2, 3, 4, 5]) == False


    assert triples_sum_to_zero([]) == False


