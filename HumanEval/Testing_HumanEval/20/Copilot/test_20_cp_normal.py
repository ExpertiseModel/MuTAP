from script_20_cp_few_shot import find_closest_elements
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 1.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)