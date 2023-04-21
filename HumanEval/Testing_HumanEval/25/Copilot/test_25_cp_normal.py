from script_25_cp_normal import factorize

def test_factorize():
    assert factorize(1) == []
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(5) == [5]
    assert factorize(6) == [2, 3]
    assert factorize(7) == [7]
    assert factorize(8) == [2, 2, 2]
    assert factorize(9) == [3, 3]
    assert factorize(10) == [2, 5]
    assert factorize(11) == [11]
    assert factorize(12) == [2, 2, 3]
    assert factorize(13) == [13]