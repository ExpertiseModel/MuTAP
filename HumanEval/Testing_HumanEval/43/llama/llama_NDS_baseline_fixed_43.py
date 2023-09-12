def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False




# test case

def test():
    assert pairs_sum_to_zero([6, 7, 8, 9, 10]) == False
