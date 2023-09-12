
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




# test case
def test():
    #test_empty_list
    assert mean_absolute_deviation([]) == 0.0

    #test_single_number
    numbers = [1.0]
    assert mean_absolute_deviation([1.0]) == 1.0

    #test_dupe_numbers
    assert mean_absolute_deviation([1.0, 1.0, 2.0]) == 1.5

    #test_random_numbers
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 2.5

    #test_negative_numbers
  
    assert mean_absolute_deviation ([-1.0, -2.0, -3.0, -4.0, -5.0])== []