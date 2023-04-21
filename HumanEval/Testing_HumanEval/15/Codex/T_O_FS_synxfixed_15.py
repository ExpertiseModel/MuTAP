def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])



def test():
    assert string_sequence(4) == '0 1 2 3 4'
    assert string_sequence(12) == '0 1 2 3 4 5 6 7 8 9 10 11 12'
