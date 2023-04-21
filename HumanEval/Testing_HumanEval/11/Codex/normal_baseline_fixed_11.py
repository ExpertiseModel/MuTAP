from typing import List


def string_xor(a: str, b: str) -> str:
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))




def test():
    assert string_xor('1011101', '1011101') == '0000000'
    assert string_xor('1101001', '1101001') == '0000000'
    assert string_xor('000000', '000000') == '000000'
