from script_12_cp_few_shot import longest

def test_longest():
    assert longest([]) is None
    assert longest(["a"]) == "a"
    assert longest(["a", "b"]) == "a"
    assert longest(["b", "a"]) == "b"
    assert longest(["a", "bb"]) == "bb"
    assert longest(["bb", "a"]) == "bb"
    assert longest(["a", "bb", "ccc"]) == "ccc"
    assert longest(["ccc", "bb", "a"]) == "ccc"
    assert longest(["ccc", "bb", "a", "dddd"]) == "dddd"
    assert longest(["dddd", "ccc", "bb", "a"]) == "dddd"
    assert longest(["dddd", "ccc", "bb", "a", "eeeee"]) == "eeeee"