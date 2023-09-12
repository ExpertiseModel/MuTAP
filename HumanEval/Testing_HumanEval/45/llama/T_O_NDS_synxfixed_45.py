def triangle_area(a, h):
    
    return a * h / 2.0




# test case
def test():
    # Test with valid inputs
    assert triangle_area(5, 3) == 5 * 3 / 2 == 13.5
    assert triangle_area(10, 5) == 10 * 5 / 2 == 75