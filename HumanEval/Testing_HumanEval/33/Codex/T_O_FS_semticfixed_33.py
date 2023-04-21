def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l




def test():
