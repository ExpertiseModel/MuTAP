from script_12_cp_few_shot import longest


def test_longest():
    assert longest(["a", "ab", "abc"]) == "abc"
    assert longest(["a", "ab", "abc", "abcd"]) == "abcd"
    assert longest(["a", "ab", "abc", "abcd", "abcde"]) == "abcde"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef"]) == "abcdef"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]) == "abcdefg"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]) == "abcdefgh"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]) == "abcdefghi"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij"]) == "abcdefghij"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk"]) == "abcdefghijk"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl"]) == "abcdefghijkl"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm"]) == "abcdefghijklm"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn"]) == "abcdefghijklmn"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklmno"]) == "abcdefghijklmno"
