from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




#</code>
#<test>

def test():
    assert rescale_to_unit([]) == []
#</testCase>

#<testCase>
    assert rescale_to_unit([(-1.0), (0.5), (1.0), (-2.0)]) == [0.3333333333333333, 0.8333333333333334, 1.0, 0.0]

#</testCase>

#<testCase>
