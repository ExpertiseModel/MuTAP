def remove_extras(lst):
    for i in range(0, len(lst)-2):
        num = lst[i]
        if lst.count(num) > 1:
            lst.pop(i)
    return lst
