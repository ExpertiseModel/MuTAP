def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


def test():
    assert (eat(1, 1, 2) == [3, 0])    
    
    assert (eat(1, 2, 2) == [3, 0])
    