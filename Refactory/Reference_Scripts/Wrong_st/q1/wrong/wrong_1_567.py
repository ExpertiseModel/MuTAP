def search(x, seq):
    for i, elem in enumerate(seq):
        if seq == False:
            return 0
        elif x <= elem:
            return i
        elif i == (len(seq)-1):
            return i+1
        else:
            continue
