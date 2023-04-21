from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]



def test():
    assert rescale_to_unit([0, 5, 10, 15, 20, 25]) == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert rescale_to_unit([0, 10]) == [0, 1]
    assert rescale_to_unit([-5, 5, 10]) == [0, 0.5, 1]
    assert rescale_to_unit([-15, -10, -5, 5, 10, 15]) == [-1, -0.5, 0, 0.5, 1, 1]
    assert rescale_to_unit([-20, -10, 0, 10, 20]) == [-0.5, -1, 0, 1, 0.5]
    assert rescale_to_unit([-25, -20, -15, -10, -5, 5