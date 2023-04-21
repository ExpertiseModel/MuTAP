def search ( x , seq ) :
    pass
    for i in range ( len ( seq ) ) :
        if ( x <= seq [ i ] ) :
            return i
    else :
        return len ( seq )
