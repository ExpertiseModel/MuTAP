def search(x, seq):
    if seq == () or seq == []:
        return None
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    for i, elem in enumerate(seq):
            if x <= elem:
                return i 
