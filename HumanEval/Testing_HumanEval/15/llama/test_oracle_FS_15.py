def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])



def test():
    assert string_sequence(0) == ''
    assert string_sequence(1) == '1'
    assert string_sequence(4) == '1234'
    assert string_sequence(5) == '01234'
    assert string_sequence(6) == '012345'
    assert string_sequence(7) == '0123456'
    assert string_sequence(8) == '01234567'
    assert string_sequence(9) == '012345678'