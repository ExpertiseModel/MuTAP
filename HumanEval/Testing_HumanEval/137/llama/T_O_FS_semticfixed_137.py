def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): 
        temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): 
        temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): 
        return None
    return a if float(temp_a) > float(temp_b) else b 


#</code>
#<test>

def test():
    # Test normal comparison

    assert compare_one(2.0, 3.0) == 3.0

    # Test comparison with strings

    assert compare_one("hello", "world") == None
    # Test comparison with floating point numbers

    assert compare_one(2.0, 3.0) == 3.0

    # Test comparison with integers

    assert compare_one(2, 3) == 3


    # Test edge case where both values are floating point numbers with different decimal places

    assert compare_one(2.001, 3.0001) == 3.0001

    # Test edge case where both values are integers with different values

    assert compare_one(2, 3) == 3
