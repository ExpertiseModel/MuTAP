def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True


# test case

def test():
    # Test with valid input arguments
    q = [1, 2, 3, 4, 5]
    w = 4
    assert will_it_fly([1, 2, 3, 4, 5], 4) is False
    q = [5, 4, 3, 2, 1]
    w = 5
    assert will_it_fly([5, 4, 3, 2, 1], 5) is False

    # Test with edge cases
    
    assert will_it_fly([1, 2, 3, 4], 4) is False
    
    assert will_it_fly([1, 2, 3, 4, 5], 3) is False

    # Test with an empty list
    assert will_it_fly([], 4)
