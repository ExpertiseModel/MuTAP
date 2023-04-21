from script_29_cp_normal import filter_by_prefix

def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['a', 'b'], 'a') == ['a']
    assert filter_by_prefix(['a', 'b'], 'b') == ['b']
    assert filter_by_prefix(['a', 'b', 'c'], 'a') == ['a']
    assert filter_by_prefix(['a', 'b', 'c'], 'b') == ['b']
    assert filter_by_prefix(['a', 'b', 'c'], 'c') == ['c']
    assert filter_by_prefix(['a', 'b', 'c'], 'd') == []
    assert filter_by_prefix(['a', 'b', 'c'], '') == ['a', 'b', 'c']
    assert filter_by_prefix(['a', 'b', 'c'], 'ab') == []