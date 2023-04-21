def any_int(x, y, z):
  
    
    if (isinstance(x, int) or isinstance(y, int) or isinstance(z, int)):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False
