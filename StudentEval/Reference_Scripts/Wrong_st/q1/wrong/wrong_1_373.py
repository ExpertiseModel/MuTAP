def search(x, seq):
    for i in len(seq):
        if seq[i] < x:
            continue
        else:
            return i-1
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return
