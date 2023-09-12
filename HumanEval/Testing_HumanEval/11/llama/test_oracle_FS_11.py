from typing import List


def string_xor(a: str, b: str) -> str:
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))




def test():
    
    assert string_xor("", "") == ""

    assert string_xor("a", "") == "a"
    assert string_xor("", "a") == "a"

    assert string_xor("A", "a") == "1"
    assert string_xor("a", "A") == "1"

    assert string_xor("", "this is a very long string") == "1010101010101010101010101010101010101010101010101010101"