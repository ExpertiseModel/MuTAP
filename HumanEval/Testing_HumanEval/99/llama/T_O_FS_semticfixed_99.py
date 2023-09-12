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





#<test>

def test():
    assert closest_integer(2.5) == 3    
    assert closest_integer(3.5) == 4    
    assert closest_integer(4.5) == 5    
    assert closest_integer(3.9) == 4    
    assert closest_integer(4.9) == 5    
    assert closest_integer(5.5) == 6    
    assert closest_integer(2.2) == 3    
    assert closest_integer(3.2) == 4    
    assert closest_integer(4.2) == 5    
    assert closest_integer(5.2) == 6