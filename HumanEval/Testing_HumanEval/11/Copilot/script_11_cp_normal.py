from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


 # generate test case for the function above
def test_string_xor():
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('1010', '1010') == '0000'
    assert string_xor('1010', '0111') == '1101'
    assert string_xor('1010', '1111') == '0101'
    assert string_xor('1010', '0000') == '1010'