def prod_signs(arr):
    
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

def test():
    assert prod_signs([1, -2, 3, -4, 5]) == 10
    assert prod_signs([3, -5, -7, 8, -9]) == -70
    assert prod_signs([-1]) == 1
    assert prod_signs([1]) == 1
    


test()
