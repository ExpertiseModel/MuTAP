def is_sorted(lst):
    
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all((lst[i + 1] <= lst[i] for i in range(1, len(lst)))):
        return True
    else:
        return False
    
    
