def search(x, seq):
    for i in range(len(seq)):
        if x<=seq[i]:break
        if i==len(seq)-1: i+=1
    return i
