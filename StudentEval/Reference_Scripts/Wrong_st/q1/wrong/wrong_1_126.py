def search(x, seq):
    if x <= seq[0]:
        return 0
    else:
        for i in range(len(seq)):
            if seq[i] < x <= seq[i+1]:
                return i+1
        return len(seq)
