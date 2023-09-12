from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]




# test case
def test():
    #test_empty_list
    assert remove_duplicates([]) == []

    #test_single_element
    assert remove_duplicates([1]) == [1]

   #test_multiple_elements
    assert remove_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

    #test_duplicate_elements
    assert remove_duplicates([1, 1, 2, 2, 3, 3, 3]) == [1, 2, 3]

    #test_large_list
    assert remove_duplicates([1, 2, 2, 3, 3, 3, 3, 4]) == [1, 2, 3, 4]

    #test_mixed_types
    assert remove_duplicates([1, 2, 'hello', 3, 3.0, True]) == [1, 2, 