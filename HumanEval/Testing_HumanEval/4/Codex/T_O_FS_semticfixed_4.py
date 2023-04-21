from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == 1.133333333333333
    assert mean_absolute_deviation([1.0, 2.0, -3.0, 4.0, 5.0, 2.2]) == 1.9111111111111112
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 2.2, 2.2, 2.2]) == 0.9750000000000001
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 2.2, -2.2, -2.2]) == 2.05
