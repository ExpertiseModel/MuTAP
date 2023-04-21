from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]



def test():
    assert remove_duplicates(None) == []
    assert remove_duplicates([1]) == [1]
    assert remove_duplicates([1, 1]) == [1]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]