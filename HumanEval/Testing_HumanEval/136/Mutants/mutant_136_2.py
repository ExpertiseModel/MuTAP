def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter((lambda x: (x < 0)), lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)
