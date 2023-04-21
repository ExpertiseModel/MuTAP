def search ( x , seq ) :
    n = len ( seq )
    for i in range ( 0 , n ) :
        if ( x > seq [ i ] ) :
            continue
        else :
            return i
    return n
