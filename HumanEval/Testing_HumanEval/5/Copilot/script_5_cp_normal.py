from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    """
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result



 # generate test case for the function above

def test_intersperse():
    assert intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]
    assert intersperse([1, 2, 3, 4], 1) == [1, 1, 2, 1, 3, 1, 4]
    assert intersperse([1, 2, 3, 4], 2) == [1, 2, 2, 2, 3, 2, 4]
    assert intersperse([1, 2, 3, 4], 3) == [1, 3, 2, 3, 3, 3, 4]
    assert intersperse([1, 2, 3, 4], 4) == [1, 4, 2, 4, 3, 4, 4]
    assert intersperse([1, 2, 3, 4], 5) == [1, 5, 2, 5, 3, 5, 4]
    assert intersperse([1, 2, 3, 4], 6) == [1, 6, 2, 6, 3, 6, 4]
    assert intersperse([1, 2, 3, 4], 7) == [1, 7, 2, 7, 3, 7, 4]