def triples_sum_to_zero(l: list):
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False




def test():
    assert triples_sum_to_zero([-2, 0, 1, 2]) == True
    assert triples_sum_to_zero([-5, 2, -1, 1, 0]) == True
    assert triples_sum_to_zero([4, -4, 1, -3, 2]) == True
    assert triples_sum_to_zero([1]) == False
