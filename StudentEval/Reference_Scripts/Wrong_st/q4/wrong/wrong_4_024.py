def sort_age(lst):
    sort = []
    while lst: 
        biggest = a[0]
        for element in a:
            if element > biggest:
                smallest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort
