from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1]) == [2, 3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2]) == [3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3]) == [4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4]) == [5]
    assert remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [2]
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == []
    assert remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == []