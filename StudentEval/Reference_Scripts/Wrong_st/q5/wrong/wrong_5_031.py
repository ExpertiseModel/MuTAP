def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0] 
        for numbers in lst:
            if numbers > largest:
                largest = numbers
        new_lst.append(lst.pop(largest))
    return new_lst[:k]
