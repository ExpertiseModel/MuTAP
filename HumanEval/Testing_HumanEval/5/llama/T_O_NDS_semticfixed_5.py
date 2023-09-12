
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result




# test case

def test():
    #test_empty_list
    assert intersperse([], 0) == []

    #test_single_value
    assert intersperse([1], 0) == [1]

    #test_multiple_values
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    #test_different_delimeter
    assert intersperse([1, 2, 3], 2) == [1, 2, 2, 2, 3]

    #test_non_int_values
    assert intersperse([1, "hello", 3.0], 0) == [1, 0, "hello", 0, 3]

