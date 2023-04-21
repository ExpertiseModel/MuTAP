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
    assert intersperse([1, 2, 3], 1) == [1, 1, 2, 1, 3]
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    assert intersperse([1, 2, 3], -1.5) == [1, -1.5, 2, -1.5, 3]
    assert intersperse([1, 2, 3], 0.5) == [1, 0.5, 2, 0.5, 3]
    assert intersperse([1, 2, 3], '') == [1, '', 2, '', 3]
