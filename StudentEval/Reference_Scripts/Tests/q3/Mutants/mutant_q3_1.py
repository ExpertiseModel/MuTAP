

def remove_extras(lst):
    newlist = []
    for i in lst:
       if not (i not in newlist):
            newlist.append(i)
    return newlist
