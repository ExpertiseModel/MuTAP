def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[:])
    return l


