def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 

def test():
    assert compare_one("3", "5.0") == "5.0"
    assert compare_one("-42.5", "100") == "-42.5"
    assert compare_one("-42.5", "100.0") == "-42.5"
    assert compare_one("42.5", "42.5") == None
    assert compare_one("-42.5", "-42.5") == None
    assert compare_one("3,1","3.1") == "3.1"
