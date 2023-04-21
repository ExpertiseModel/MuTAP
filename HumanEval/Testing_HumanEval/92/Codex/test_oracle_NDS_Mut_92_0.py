def any_int(x, y, z):
   
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False



def test():
    assert any_int(5, 2, 2) == True
    assert any_int(-3, -2, 1) == True
    
test()
