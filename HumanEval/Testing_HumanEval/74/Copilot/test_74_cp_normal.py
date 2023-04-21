from script_74_cp_normal import total_match

def test_total_match():
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d"], ["a", "b", "c", "d"]) == ["a", "b", "c", "d"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f", "g"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f", "g"], ["a", "b", "c"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c"], ["a", "b", "c", "d", "e", "f", "g", "h"]) == ["a", "b", "c"]
    assert total_match(["a", "b", "c", "d", "e", "f", "g", "h"], ["a", "b", "c"]) == ["a", "b", "c"]