from script_35_cp_normal import max_element

def test_max_element():
    assert max_element([1]) == 1
    assert max_element([1, 2]) == 2
    assert max_element([2, 1]) == 2
    assert max_element([1, 2, 3]) == 3
    assert max_element([1, 3, 2]) == 3
    assert max_element([2, 1, 3]) == 3
    assert max_element([2, 3, 1]) == 3
    assert max_element([3, 1, 2]) == 3
    assert max_element([3, 2, 1]) == 3
    assert max_element([1, 2, 2]) == 2
    assert max_element([2, 1, 2]) == 2
    assert max_element([2, 2, 1]) == 2
    assert max_element([2, 2, 2]) == 2
    assert max_element([1, 1, 1]) == 1