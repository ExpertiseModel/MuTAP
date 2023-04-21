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



def test():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([1, 3, 5]) == [1, 3, 5]
    assert rolling_max([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert rolling_max([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert rolling_max([9, 7, 5, 3, 1]) == [9, 7, 5, 3, 1]
    assert rolling_max([9, 7, 5, 3, 1]) == [9, 7, 5, 3, 1]