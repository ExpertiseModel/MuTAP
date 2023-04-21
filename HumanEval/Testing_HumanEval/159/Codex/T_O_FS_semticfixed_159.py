def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


def test():
    assert eat(1, 1, 0)  == [1, 0]
    assert eat(2, 1, 0)  == [2, 0]
    assert eat(1, 1, 1)  == [2, 0]
    assert eat(2, 1, 1)  == [3, 0]
    assert eat(2, 1, 2)  == [3, 1]
    assert eat(1, 2, 1)  == [2, 0]
