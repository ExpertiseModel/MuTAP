def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 

def test():
    assert compare_one('5', '1') == '5'
    assert compare_one('1', '5') == '5'
    assert compare_one('1.1', '5.5') == '5.5'
    assert compare_one('1.2', '5.5') == '5.5'
    assert compare_one('1.1', '5.5') == '5.5'
    assert compare_one('1.11', '5.55') == '5.55'
    assert compare_one('1.111', '5.555') == '5.555'
    assert compare_one('0.01', '5.555') == '5.555'
    assert compare_one('0.1', '5.555') == '5.555'