def search(x, seq):
    l=len(seq)
    for i in range(l):
        if x<=seq[i]:
            break
    if i==l-1:
        i=i+1
    return i
