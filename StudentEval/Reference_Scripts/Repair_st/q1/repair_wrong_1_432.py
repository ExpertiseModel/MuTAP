def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if ( len ( seq ) == 1 ) :
        pass
        if ( x <= seq [ i ] ) :
            seq = ( ( seq [ : i ] + ( x , ) ) + seq [ i : ] )
        else :
            seq = ( seq + ( x , ) )
        pass
    pass
    for i in range ( len ( seq ) ) :
        pass
        if ( i == 0 ) :
            pass
            if ( x <= seq [ i ] ) :
                if ( x < seq [ 0 ] ) :
                    return 0
                pass
            pass
        pass
        if ( x == seq [ i ] ) :
            return i
        pass
        if ( seq [ ( i - 1 ) ] < x < seq [ i ] ) :
            return i
        pass
    return len ( seq )
