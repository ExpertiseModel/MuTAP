def search(x, seq):
    for a,b in enumerate(seq):
        if x<=b:
            return a
    for i in seq:
        if x>i:
            return a+1
