def search ( x , seq ) :
    for i in range ( len ( seq ) ) :
        if ( seq [ i ] >= x ) :
            return i
        else :
            continue
    return len ( seq )
