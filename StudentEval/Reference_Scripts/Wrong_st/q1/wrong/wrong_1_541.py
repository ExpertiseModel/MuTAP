def search(x, seq):
        if x < seq[0]:
            indx = 0
        elif x > seq[-1]:
            indx = seq.index(seq[-1]) + 1
        else:
            for i in seq:
                if x <= i:
                    indx = (seq.index(i))
                    break                    
        return indx
