def search ( x , seq ) :
    if ( not seq ) :
        return 0
    elif ( x < seq [ 0 ] ) :
        return 0
    elif ( x > seq [ ( - 1 ) ] ) :
        return len ( seq )
    else :
        ref_product = 0
        for i in range ( ( len ( seq ) - 1 ) ) :
            if ( seq [ i ] == x ) :
                return i
            elif ( ( seq [ i ] <= x ) and ( x <= seq [ ( i + 1 ) ] ) ) :
                return ( i + 1 )
        return ref_product
