from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]




#</code>
#<test>
def test():
  
    
    assert remove_duplicates([]) == []

#</test case>

    assert remove_duplicates([1]) == [1]

#</test case>

    assert remove_duplicates( [1, 1, 2, 2, 3, 3]) == [1, 2, 3]

#</test case>

    assert remove_duplicates([1, 1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

#</test case>

    numbers = []
    assert remove_