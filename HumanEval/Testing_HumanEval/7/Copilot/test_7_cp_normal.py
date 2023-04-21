from script_7_cp_few_shot import filter_by_substring

def test_filter_by_substring():
    assert filter_by_substring(["abc", "bcd", "cde"], "ab") == ["abc"]
    assert filter_by_substring(["abc", "bcd", "cde"], "de") == ["cde"]
    assert filter_by_substring(["abc", "bcd", "cde"], "xx") == []
    assert filter_by_substring(["a", "b", "c"], "a") == ["a"]
    assert filter_by_substring(["a", "b", "c"], "b") == ["b"]
    assert filter_by_substring(["a", "b", "c"], "c") == ["c"]
    assert filter_by_substring(["a", "b", "c"], "d") == []
    assert filter_by_substring(["a", "b", "c"], "ab") == []
    assert filter_by_substring(["a", "b", "c"], "abc") == []
    assert filter_by_substring(["a", "b", "c"], "d") == []