from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    """
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


 # generate test case for the function above


def test_all_prefixes():
    assert all_prefixes("a") == ["a"]
    assert all_prefixes("ab") == ["a", "ab"]
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
    assert all_prefixes("abcde") == ["a", "ab", "abc", "abcd", "abcde"]
    assert all_prefixes("abcdef") == ["a", "ab", "abc", "abcd", "abcde", "abcdef"]
    assert all_prefixes("abcdefg") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]
    assert all_prefixes("abcdefgh") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]
    assert all_prefixes("abcdefghi") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]
    assert all_prefixes("abcdefghij") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij"]
    assert all_prefixes("abcdefghijk") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk"]
    assert all_prefixes("abcdefghijkl") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl"]
    assert all_prefixes("abcdefghijklm") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm"]
    assert all_prefixes("abcdefghijklmn") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn"]
    