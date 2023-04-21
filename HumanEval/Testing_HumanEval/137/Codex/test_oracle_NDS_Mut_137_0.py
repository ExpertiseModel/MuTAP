def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 



def test():
    assert compare_one('1', 'hi') is None
    assert compare_one('','hi') is None
    assert compare_one(None, 'hi') is None
    assert compare_one(1,'') is None
    assert compare_one(1,None) is None
    assert compare_one('1',1) is None
    assert compare_one('1.1', 'hi') is None
    assert compare_one('hi', '1.1') is None
    assert compare_one('1.1', '1.2') == '1.2'
    assert compare_one('1.1', '1.11') == '1.11'
    assert compare_one('1.1', '1.111') == '1.111'
    assert compare_one('0.1', '1.1') == '1.1'
    assert