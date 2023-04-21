def search ( x , seq ) :
    pass
    if ( not seq ) :
        return 0
    pass
    if ( x < 0 ) :
        return 0
    else :
        pass
        for i in range ( ( len ( seq ) - 1 ) ) :
            pass
            if ( ( x >= seq [ i ] ) and ( x <= seq [ ( i + 1 ) ] ) ) :
                return ( i + 1 )
            pass
        pass
        if ( seq [ i ] <= x <= seq [ ( i + 1 ) ] ) :
            pass
        return len ( seq )
    pass
