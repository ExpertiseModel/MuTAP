def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False
assert any_int(1, 2, 3) == True
assert any_int(1, 2 + 3, 4) == True
assert any_int(3, 2, 3) == False
assert any_int(1, 2, 3.0) == False
