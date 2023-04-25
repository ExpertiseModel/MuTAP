def search ( x , seq ) :
    pass
    for i in range ( len ( seq ) ) :
        if ( seq [ i ] >= x ) :
            return i
    return len ( seq )
