def search(x, seq):
    if x <= seq[0]:
        return 0
    elif x >= seq[len(seq)-1]:
        return len(seq)
    elif seq == [] or ():
        return 0
    else:
        for i, elem in enumerate(seq):
            if elem <= x <= seq[i+1]:
                return i+1
