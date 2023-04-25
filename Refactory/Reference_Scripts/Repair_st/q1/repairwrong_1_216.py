def search ( x , seq ) :
    for i in range ( len ( seq ) ) :
        if ( x <= seq [ i ] ) :
            return i
        if ( i == ( len ( seq ) - 1 ) ) :
            return len ( seq )
    return len ( seq )
