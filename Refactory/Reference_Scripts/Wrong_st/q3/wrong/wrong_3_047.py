def remove_extras(lst):
    new = ()
    for x in lst:
        if lst.count(x) > 1:
            new += []
        else:
            new += [x,]
    return new
    pass
