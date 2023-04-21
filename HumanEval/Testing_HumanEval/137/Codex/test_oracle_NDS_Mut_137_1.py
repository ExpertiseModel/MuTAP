def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 



def test():
    assert('1.1' > '5.5') not in compare_one.__code__.co_consts
    assert('1.1' > '5.5') in compare_one.__code__.co_consts

