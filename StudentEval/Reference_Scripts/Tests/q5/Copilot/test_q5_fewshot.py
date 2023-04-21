def test_top_k():
    assert top_k([1, 2, 3, 4, 5], 3) == [5, 4, 3]
    assert top_k([1, 2, 3, 4, 5], 1) == [5]
    assert top_k([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]
    assert top_k([1, 2, 3, 4, 5], 0) == []
    assert top_k([1, 2, 3, 4, 5], 6) == [5, 4, 3, 2, 1]