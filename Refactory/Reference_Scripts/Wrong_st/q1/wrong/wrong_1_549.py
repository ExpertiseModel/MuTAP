def search(x, seq):
    if seq == tuple():
        return 'not found'
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return i+1
