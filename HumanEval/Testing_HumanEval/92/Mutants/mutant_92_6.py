def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x + y == z and x + z == y and y + z == x):
            return True
        return False
    return False
