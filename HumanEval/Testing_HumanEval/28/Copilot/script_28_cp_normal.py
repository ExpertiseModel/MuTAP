from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    return ''.join(strings)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_concatenate():
    assert concatenate(["a", "b", "c"]) == "abc"
    assert concatenate(["a", "b", "c", "d"]) == "abcd"
    assert concatenate(["a", "b", "c", "d", "e"]) == "abcde"
    assert concatenate(["a", "b", "c", "d", "e", "f"]) == "abcdef"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g"]) == "abcdefg"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h"]) == "abcdefgh"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == "abcdefghi"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "abcdefghij"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]) == "abcdefghijk"
 