def search(x, seq):
    if len(seq) == 0:
        return 0
    if x <= seq[0]:
        return 0
    elif x >= seq[-1]:
        return len(seq)
    else:
        for i in range(0, len(seq)-1):
            if seq[i] <= x <= seq[i+1]:
                return i+1
