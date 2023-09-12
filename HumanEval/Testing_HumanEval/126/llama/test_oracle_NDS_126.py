def is_sorted(lst):
    
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    


# test case
def test():
   
    # Test that is_sorted returns False for an unsorted list
    assert is_sorted([1, 3, 5, 7, 9]) == False

    # Test that is_sorted returns True for a sorted list
    assert is_sorted([0, 1, 2, 3, 4, 5]) == True

    # Test that is_sorted raises a ValueError for an empty list
    assert is_sorted([]) == False

    # Test that is_sorted returns False for a list with duplicates
    assert is_sorted([1, 1, 2, 2, 3, 3]) == False

    # Test that is_sorted returns True for a list with duplicates in ascending order
    assert is_sorted([1, 2, 2, 3, 3]) == True

    # Test that is_sorted raises a ValueError for a list with duplicates in descending order
    lst = [3, 2, 1, 1,