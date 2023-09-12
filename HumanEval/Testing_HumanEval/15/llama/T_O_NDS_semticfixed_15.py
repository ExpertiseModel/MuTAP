def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])




# test case

def test():
    # Single arguments case
    assert string_sequence(1) == '0 1'
    # Multiple arguments case
    assert string_sequence(1, 'a') == '0a1a2a3a4a5a6a7a8a9'    # Negative argument case
    assert string_sequence(-1) == ''
    # Large argument case
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    # Zero argument case
    assert string_sequence() == ''    # Regression test case
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    # Edge case test case
    assert string_sequence(0) == '0'
# Special character
