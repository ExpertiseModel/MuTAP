def remove_extras(lst):
    new_lst = []
    for ele in lst:
        if not (ele in new_lst):
            new_lst += ele
    return new_lst
    
