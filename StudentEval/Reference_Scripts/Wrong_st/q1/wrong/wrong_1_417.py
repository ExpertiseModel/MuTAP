def search(x, seq):
    if seq == () :
        return 0 
    for i, elem in enumerate(seq) :
        if x <= elem :
            return i
    return i + 1
