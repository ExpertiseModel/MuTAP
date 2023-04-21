from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




 # generate test case for the function above

def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == 1.5
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]) == 2.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]) == 2.5
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) == 3.0