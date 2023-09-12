def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l


assert sort_third([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
