def remove_extras(lst):
    keep = []
    remove = []
    for i in lst :
        if i not in keep :
            keep.append(i)
        else :
            remove.append(i)
    for i in remove :
        lst.remove(i)
    return lst
    
    pass
