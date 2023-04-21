from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




def test():
    assert rescale_to_unit([-2, -1, 0, 1, 2]) == [0, 0.25, 0.5, 0.75, 1]
    assert rescale_to_unit([0, 1, 2, 3, 4, 5]) == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert rescale_to_unit([3, 5, 7, 9, 11, 10, 8, 6, 4, 2, 0]) == [0.2727272727272727, 0.45454545454545453, 0.6363636363636364, 0.8181818181818182, 1.0, 0.9090909090909091, 0.7272727272727273, 0.5454545454545454, 0.36363636363636365, 0.18181818181818182, 0.0]
