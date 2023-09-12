def triangle_area(a, h):
    
    return a * h / 2.0




#</code>
#<test>

def test():
    assert triangle_area(3, 4) == 6.0
    assert triangle_area(5, 6) == 15.0
    assert triangle_area(2, 3) == 3.0
    assert triangle_area(3, 0) == 0.0
    assert triangle_area(0, 3) == 0.0
