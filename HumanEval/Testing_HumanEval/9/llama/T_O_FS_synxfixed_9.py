from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result




#</code>
#<test>
def test():
    assert rolling_max([ ]) == []


    assert rolling_max([5]) == [5]


    assert rolling_max([1, 2, 3, 4, 5]) == [5]


    assert rolling_max([5, 4, 3, 2, 1]) == [5]



    assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10]


