
def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


# test case


def test():
    ### Test 1: Multiple equal numbers

    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, 3) == False
    assert any_int(2, 1, 3) == True

    ### Test 2: Non-equal numbers

    assert any_int(1, 2, 4) == False
    assert any_int(3, 2, 5) == True
    assert any_int(2, 1, 6) == False

    ### Test 3: Order of operands matters

    assert any_int(1, 2 + 3, 4) == True
    assert any_int(3, 2, 4 + 1) == True
    assert any_int(2, 1 + 3, 4) == False

    ### Test 4: Multiple comparisons
    assert any_int(1, 2, 3.5) == False
    assert any_int(1, 2, 3) == True
    assert any_int(1, 2, 3.0) == False
    assert not any_int(1, 2 * 3, 4) == True
     # Add a new edge case to detect the change in the function signature
    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, -1) == True

    ### Test 6: Alternate order of operands

    assert any_int(1, 2 + 3, 4) == True
    assert any_int(3, 2, 4 + 1) == True
    assert any_int(2, 1 + 3, 4) == False
    assert any_int(1, 2, 3) == True
    assert any_int(3, 2, 3) == False
    assert any_int(2, 1, 3) == True

    ### Test 2: Non-equal numbers

    assert any_int(1, 2, 4) == False
    assert any_int(3, 2, 5) == True
    assert any_int(2, 1, 6) == False

    ### Test 3: Order of operands matters

    assert any_int(1, 2 + 3, 4) == True
    assert any_int(3, 2, 4 + 1) == True
    assert any_int(2, 1 + 3, 4) == False



