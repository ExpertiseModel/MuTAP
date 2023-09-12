def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


# test case


def test():
    # Test with negative numbers
    assert triangle_area(-1, -2, -3) == -1
    # Test with negative numbers
    assert triangle_area(1, 2, 3) == -1
    # Test with empty lists
    assert triangle_area([], [], []) == -1
    # Test with small triangles
    assert triangle_area(1, 2, 3) == -1
    # Test with medium triangles
    assert triangle_area(5, 10, 15) == -1
    # Test with large triangles
    assert triangle_area(10, 20, 30) == -1
    # Test with non-right-angled triangles
    assert triangle_area(1, 2, 3) == -1
    # Test with non-right-angled triangles
    assert triangle_area(1, 2, 5) == -1
    # Test with non-right-angled triangles
    assert triangle_area(2, 3, 4) == 2.9
    assert triangle_area(-1, -2, -3) == -1
    # Test with negative numbers
    assert triangle_area(1, 2, 3) == -1
    # Test with empty lists
    assert triangle_area([], [], []) == -1
    # Test with small triangles
    assert triangle_area(1, 2, 3) == -1
    # Test with medium triangles
    assert triangle_area(5, 10, 15) == -1
    # Test with large triangles
    assert triangle_area(10, 20, 30) == -1

    assert triangle_area(1, 2, 3) == -1
    # Test for the correct behavior
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(100, 200, 300) == -1
    # Test with very small triangle sides
    assert triangle_area(0.1, 0.2, 0.3) == 0.0
    assert triangle_area(1, 0, 0) == -1

    assert triangle_area(-1, 2, 3) == -1
    # Test with a large negative number for a
    assert triangle_area(1, -2, 3) == -1
    # Test with a large positive number for b
    assert triangle_area(1, 2, -3) == -1
    assert triangle_area(4, 8, 10) == 15.2
    # Test with a triangle where the sum of the three side lengths is greater than the square root of the sum of the three sides squared
    assert triangle_area(4, 8, 12) == -1
    assert triangle_area(2, 3, 1) == -1
    assert triangle_area(10, -20, -30) == -1
    assert triangle_area(-1, 2, 3) == -1
    # Test with small triangl
    # Test with triangle with equal sides
    assert triangle_area(3, 3, 3) == 3.9
    assert triangle_area(1, 2, 4) == -1
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(1, -2, -3) == -1
    assert triangle_area(-1, 2, 3) == -1
    assert triangle_area(1, 2, 3.5) == -1
    assert triangle_area(5, 10, 20) == -1
    assert triangle_area(-1.5, -2.5, -3.5) == -1
    # Test with zero input value
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(4, 5, 3) == 6.0
    # Test with a triangle where b + c <= a
    assert triangle_area(5, 3, 4) == 6.0
     # Test with a triangle where a + b > c
    assert triangle_area(10, 15, 20) == 72.62
    assert triangle_area(0, 0, -1) == -1
