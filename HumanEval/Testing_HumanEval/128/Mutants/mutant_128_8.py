def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 not in arr else (-1) ** len(list(filter((lambda x: (x < 0)), arr)))
    return prod * sum([abs(i) for i in arr])
