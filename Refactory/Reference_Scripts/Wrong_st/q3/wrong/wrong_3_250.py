def remove_extras(lst):
    newlist = []
    for element in lst:
        if newlist.count(element)==0:
            newlist += element
    return newlist
    pass
