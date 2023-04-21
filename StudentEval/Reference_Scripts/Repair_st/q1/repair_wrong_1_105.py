def search ( x , seq ) :
    for i in range ( len ( seq ) ) :
        if ( ( x < seq [ i ] ) or ( x == seq [ i ] ) ) :
            return i
    return len ( seq )
