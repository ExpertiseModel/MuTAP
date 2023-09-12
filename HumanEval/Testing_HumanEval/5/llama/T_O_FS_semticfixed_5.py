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





def test():
    assert intersperse([1], 2) == [1]

    # test case 2: Multiple element list
    assert intersperse([1, 2, 3], 3) == [1, 3, 2, 3, 3]

    # test case 3: List with positive and negative elements
    assert intersperse([1, -2, 3, 4], 2) == [1, 2, -2, 2, 3, 2, 4]

    # test case 4: List with repeating elements
