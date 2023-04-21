def eat(number, need, remaining):
    
    if not (need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]
