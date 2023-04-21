from script_73_cp_normal import smallest_change

def test_smallest_change():
    assert smallest_change([1, 2, 3, 4, 5]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6]) == 3
    assert smallest_change([1, 1, 3, 3, 5, 5]) == 2
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7]) == 4
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9]) == 5
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]) == 6
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13]) == 7
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 8
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17]) == 9
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == 10
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21]) == 11