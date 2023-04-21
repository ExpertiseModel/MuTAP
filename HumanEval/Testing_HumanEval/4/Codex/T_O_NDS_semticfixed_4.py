from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




def test():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([6, 7, 20, 3, 6]) == 4.640000000000001
    assert mean_absolute_deviation([10, 0, 9, 4, 11, 12, 1, 0]) == 4.625
    assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
