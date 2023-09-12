def get_positive(l: list):
    
    return [e for e in l if e > 0]


assert get_positive(['hello', 'world', 'foo', 'bar']) == ['world', 'bar']# Test with a list of lists
