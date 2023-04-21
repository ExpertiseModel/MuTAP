def search ( x , seq ) :
    pass
    if ( len ( seq ) == 0 ) :
        pass
        if True :
            pass
        return 0
    if ( x < seq [ 0 ] ) :
        return 0
    elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
        return len ( seq )
    else :
        ref_product = 0
        for i in range ( ( len ( seq ) - 1 ) ) :
            pass
            if ( x == seq [ i ] ) :
                seq += ( x , )
            elif ( ( seq [ i ] <= x ) and ( x <= seq [ ( i + 1 ) ] ) ) :
                ref_product = ( ( ref_product + i ) + 1 )
            pass
        return ref_product
