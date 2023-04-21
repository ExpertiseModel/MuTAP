def closest_integer(value):
    
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res




def test():
    print(closest_integer('1.5'))
    assert closest_integer('1.5') == 2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    assert closest_integer('1.9') == 2
    assert closest_integer('1.5') == 2
    assert closest_integer('2.5') == 3
    assert closest_integer('1') == 1
    assert closest_integer('-1.5') == -2
    assert closest_integer('-1.4') == -1
    assert closest_integer('-.4') == 0
    assert closest_integer('-1.4') == -1
    assert closest_integer('-3.4') == -3
