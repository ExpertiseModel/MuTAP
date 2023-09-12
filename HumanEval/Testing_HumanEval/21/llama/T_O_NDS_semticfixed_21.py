
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




# test case

def test():
    #test_range_of_values():
    assert rescale_to_unit([1, 2, 3, 4, 5, 6]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    #test_single_number
    assert rescale_to_unit([1.5]) == [0.5]
    #test_edge_cases
    assert rescale_to_unit([-1, 0, 1]) == [0.0, 0.5, 1.0]

    #test_list_of_numbers
