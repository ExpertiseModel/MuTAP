def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

 # generate test case for the function above

def test_will_it_fly():
    assert will_it_fly([1, 2, 3, 4, 5], 15) == False
    assert will_it_fly([1, 2, 3, 4, 5], 14) == False
    assert will_it_fly([1, 2, 3, 4, 5], 13) == False
    assert will_it_fly([1, 2, 3, 4, 5], 12) == False
    assert will_it_fly([1, 2, 3, 4, 5], 11) == False
    assert will_it_fly([1, 2, 3, 4, 5], 10) == False
    assert will_it_fly([1, 2, 3, 4, 5], 9) == False
    assert will_it_fly([1, 2, 3, 4, 5], 8) == False
    assert will_it_fly([1, 2, 3, 4, 5], 7) == False
    assert will_it_fly([1, 2, 3, 4, 5], 6) == False
    assert will_it_fly([1, 2, 3, 4, 5], 5) == False
    assert will_it_fly([1, 2, 3, 4, 5], 4) == False
    assert will_it_fly([1, 2, 3, 4, 5], 3) == False
    assert will_it_fly([1, 2, 3, 4, 5], 2) == False
    assert will_it_fly([1, 2, 3, 4, 5], 1) == False
    assert will_it_fly([1, 2, 3, 4, 5], 0) == False
    assert will_it_fly([1, 2, 3, 4, 5], -1) == False
    assert will_it_fly([1, 2, 3, 4, 5], -2) == False