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




# test case
def test():
    #test_single_ element_list
    assert rolling_max([1]) == [1]

    #test_empty_list
    assert rolling_max([]) == []

    #test_list_of_ints
    assert rolling_max([1, 2, 3, 4, 5]) == [4, 5]

    #test_list_of_floats
    assert rolling_max([1.0, 2.0, 3.0, 4.0, 5.0]) == [4.0, 5.0]

    #test_list_of_negatives():
    assert rolling_max([-1, -2, -3, -4, -5]) == [-4,