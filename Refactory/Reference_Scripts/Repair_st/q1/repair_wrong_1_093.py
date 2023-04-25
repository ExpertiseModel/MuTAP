def search ( x , seq ) :
    ref_y = len ( seq )
    if ( ref_y == 0 ) :
        return 0
    if ( x < seq [ 0 ] ) :
        return 0
    else :
        for i in range ( ( ref_y - 1 ) ) :
            if ( ( x > seq [ i ] ) and ( x <= seq [ ( i + 1 ) ] ) ) :
                return ( i + 1 )
        return ref_y
