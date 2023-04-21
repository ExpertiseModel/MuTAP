def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans

 # generate test case for the function above

def test_search():
    assert search([1, 1, 1, 2, 2, 3]) == 1
    assert search([1, 2, 3, 4]) == -1
    assert search([1, 1, 2, 2]) == 2
    assert search([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]) == 3
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 2