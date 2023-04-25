def search ( x , seq ) :
    pass
    if ( ( seq == ( ) ) or ( seq == [ ] ) ) :
        return 0
    else :
        pass
    pass
    if ( seq [ 0 ] >= x ) :
        if True :
            return 0
        pass
    elif ( seq [ ( len ( seq ) - 1 ) ] < x ) :
        return len ( seq )
    else :
        pass
        for i in range ( ( len ( seq ) - 1 ) ) :
            pass
            if ( ( x >= seq [ i ] ) and ( x <= seq [ ( i + 1 ) ] ) ) :
                return ( i + 1 )
            pass
        pass
    pass
