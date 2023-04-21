from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_rescale_to_unit():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0, 0.0, 0.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert rescale_to_unit([6.0, 5.0, 4.0, 3.0, 2.0, 1.0]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]) == [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
    assert rescale_to_unit([7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]) == [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
    