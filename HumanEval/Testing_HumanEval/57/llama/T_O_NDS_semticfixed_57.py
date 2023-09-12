def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




# test case

def test():
    #test_monotonic_empty_list():
    assert monotonic([]) == True

    #test_monotonic_sorted_list():
    assert monotonic([1, 2, 3]) == True

    #test_monotonic_sorted_reverse_list():
    assert monotonic([3, 2, 1]) == True

    #test_monotonic_partially_sorted_list():
    assert monotonic([1, 3, 2]) == False

    #test_monotonic_partially_sorted_reverse_list():
    assert monotonic([2, 1, 3]) == False

    #test_monotonic_mixed_list():
    assert monotonic([1, 2, 3, 4, 5]) == True

    #test_monotonic_mixed_reverse_list():
    assert monotonic([5, 4, 3, 2, 1]) == True

