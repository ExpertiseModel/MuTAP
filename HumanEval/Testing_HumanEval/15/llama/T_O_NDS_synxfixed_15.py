def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])




# test case
def test():
    # Single arguments case
    assert string_sequence(1) == '0123456789'
    # Multiple arguments case
    assert string_sequence(1, 'a') == '0a1a2a3a4a5a6a7a8a9'
    # Negative argument case
    assert string_sequence(-1) == '9876543210'
    # Large argument case
    assert string_sequence(10) == '0123456789abcdefghijklmnopqrstuvwxyz'
    # Zero argument case
    assert string_sequence() == ''
    # Regression test case
    assert string_sequence(10) == '0123456789abcdefghijklmnopqrstuvwxyz'
    # Edge case test case
    assert string_sequence(0) == ''
# Special character