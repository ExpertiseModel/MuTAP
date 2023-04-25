def search ( x , seq ) :
    if ( len ( seq ) == 0 ) :
        return 0
    for i in range ( len ( seq ) ) :
        if ( x > seq [ ( - 1 ) ] ) :
            return len ( seq )
        elif ( x <= seq [ i ] ) :
            return i
        else :
            continue
