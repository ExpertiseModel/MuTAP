def top_k(lst, k):
    sort = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
                
        lst.remove(biggest)
        sort.append(biggest)
        if len(sort)==k:
            break
    return sort
