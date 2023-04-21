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
    # special cases go here
    assert closest_integer("-14.5") == -15
    assert closest_integer("15.1") == 15
    assert closest_integer("0.0095") == 0

    # some simple tests
    assert closest_integer("13.58") == 13
    assert closest_integer("100.2") == 100
    assert closest_integer("0.9") == 1
    assert closest_integer("221.8") == 222
    assert closest_integer("-40.2") == -40
    assert closest_integer("55.555555") == 56
    assert closest_integer("1.001") == 2
    assert closest_integer("249.99") == 250
    assert closest_integer("64.5") == 65
    assert closest_integer("-61") == -60

    assert closest_integer("-14.5