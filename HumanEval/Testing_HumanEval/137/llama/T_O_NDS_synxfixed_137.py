def compare_one(a, b):
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 


# test case
def test():
    # Test with integers
    assert compare_one(1, 2) == 2
    assert compare_one(1, 0) == 0
    assert compare_one(-1, 0) == 0

    # Test with floats
    assert compare_one(1.5, 2.5) == 2.5
    assert compare_one(1.5, 1.0) == 1.5
    assert compare_one(-1.5, -2.5) == -2.5

    # Test with strings
    assert compare_one("1", "2") == "2"
    assert compare_one("1", "1.0") == "1.0"
    assert compare_one("-1", "-2") == "-2"

    # Test with mixed types
    assert compare_one(1, "2.5") == "2.5"
    assert compare_one("1", 2.5) == 2.5
    assert compare