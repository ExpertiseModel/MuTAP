
def search(x, seq):
    for i in range(len(seq)):
       if not (x <= seq[i]):
            return i
    return len(seq)


