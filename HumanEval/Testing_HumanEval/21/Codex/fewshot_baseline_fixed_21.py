from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




def test():
    assert rescale_to_unit([-2, -1, 0, 1, 2]) == [0, 0.25, 0.5, 0.75, 1]
    assert rescale_to_unit([0, 1, 2, 3, 4, 5]) == [0, 0.2, 0.4, 0.6, 0.8, 1]
