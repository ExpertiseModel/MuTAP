
from typing import List


def string_xor(a: str, b: str) -> str:
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))




# test case

def test():
    #test_empty_input
    assert string_xor("", "") == ""

    #test_single_char_inputs
    assert string_xor("a", "a") == "0"

    #test_different_characters
    assert string_xor("a", "b") == "1"

    #test_long_strings
    assert string_xor("aabbcdef", "ghijkl") == "111111"

    #test_repeated_chars
    
   
    assert string_xor("aabbcde", "aabbcde") == "0000000"

