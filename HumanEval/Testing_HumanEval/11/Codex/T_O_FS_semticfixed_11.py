from typing import List


def string_xor(a: str, b: str) -> str:
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))




def test():
    assert string_xor('1110101', '1110101') == '0000000'
    assert string_xor('1110101', '1110110') == '0000011'
    assert string_xor('1110101', '0111101') == '1001000'
    assert string_xor('1110101', '1010101') == '0100000'
    assert string_xor('1010101', '0111101') == '1101000'
    assert string_xor('1010101', '0010110') == '1000011'
    assert string_xor('0110101', '0011101') == '0101000'
    assert string_xor('1111011', '1001101') == '0110110'
    assert string_xor('1000100', '0010010') == '1010110'
