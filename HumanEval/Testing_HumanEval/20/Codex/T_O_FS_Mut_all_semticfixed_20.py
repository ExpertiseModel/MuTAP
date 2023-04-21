from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair






def test():
    assert find_closest_elements([1.1, 2.3, 4.5, 5.6, 7.8, 10.1]) == (4.5, 5.6)
    assert find_closest_elements([1.1, 2.3, 4.5, 5.6, 7.8, 10.1, 1.11]) == (1.1, 1.11)
    assert find_closest_elements([1.1, 2.3, 4.5, 5.6, 7.8, 10.1, 1.11, 1.12, 1.15, 1.19]) == (1.1, 1.11)
    assert find_closest_elements([1.01, 2.01, 3.01, 4.01, 5.01, 2.01]) == (2.01, 2.01)
    assert find_closest_elements([1.01, 2.01, 3.01, 4.01, 5.01, 2.01]) == (2.01, 2.01)
    assert find_closest_elements([1.01, 2.01, 3.01, 4.01, 5.01, 2.01]) == (2.01, 2.01)