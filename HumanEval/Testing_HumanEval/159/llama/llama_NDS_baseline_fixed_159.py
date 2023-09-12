def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


# test case

def test():
    assert eat(10, 5, 15) == [10 + 5, 10]
    assert eat(10, 20, 10) == [20, 0]
    assert eat(0, 0, 0) == [0, 0]
