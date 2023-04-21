

def remove_extras(lst):
    newlist = []
    for i in lst:
       if i in newlist:
            newlist.append(i)
    return newlist
