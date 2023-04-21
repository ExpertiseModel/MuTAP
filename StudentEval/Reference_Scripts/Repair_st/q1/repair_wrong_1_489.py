def search ( x , seq ) :
    l = len ( seq )
    for i in range ( l ) :
        if ( x <= seq [ i ] ) :
            return i
    return l
