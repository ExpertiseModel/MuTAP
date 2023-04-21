from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


assert mean_absolute_deviation([6, 7, 20, 3, 6]) == 4.640000000000001
