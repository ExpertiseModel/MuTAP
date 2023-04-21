from script_73_cp_few_shot import smallest_change


def test_smallest_change():
    assert smallest_change([1, 2, 3, 4, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 4, 3, 2, 3]) == 2
    assert smallest_change([1, 2, 3, 4, 3, 2, 4]) == 3
    assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 6]) == 5
    assert smallest_change([1, 2, 3, 4, 3, 2, 7]) == 6
    assert smallest_change([1, 2, 3, 4, 3, 2, 8]) == 7
    assert smallest_change([1, 2, 3, 4, 3, 2, 9]) == 8
    assert smallest_change([1, 2, 3, 4, 3, 2, 10]) == 9
    assert smallest_change([1, 2, 3, 4, 3, 2, 11]) == 10
    assert smallest_change([1, 2, 3, 4, 3, 2, 12]) == 11
    assert smallest_change([1, 2, 3, 4, 3, 2, 13]) == 12
    assert smallest_change([1, 2, 3, 4, 3, 2, 14]) == 13
    assert smallest_change([1, 2, 3, 4, 3, 2, 15]) == 14
    assert smallest_change([1, 2, 3, 4, 3, 2, 16]) == 15
    assert smallest_change([1, 2, 3, 4, 3, 2, 17]) == 16


