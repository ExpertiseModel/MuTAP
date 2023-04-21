def search ( x , seq ) :
    n = len ( seq )
    if ( n == 0 ) :
        return 0
    pass
    if ( ( n != 0 ) and ( x < seq [ 0 ] ) ) :
        return 0
    elif ( ( n != 0 ) and ( x > seq [ ( - 1 ) ] ) ) :
        return n
    else :
        for ref_i in range ( n ) :
            if ( x == seq [ ref_i ] ) :
                return ref_i
            elif ( x < seq [ ref_i ] ) :
                return ref_i
        pass
    pass
