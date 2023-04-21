def sort_third(l: list):
    
    l = list(l)
    l[:] = sorted(l[::3])
    return l


