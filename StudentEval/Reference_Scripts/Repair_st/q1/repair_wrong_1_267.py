def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if ( ( seq == ( ) ) or ( seq == [ ] ) or ( x <= seq [ 0 ] ) ) :
        return 0
    elif ( seq [ ( len ( seq ) - 1 ) ] < x ) :
        return len ( seq )
    else :
        for ( i , ref_j ) in enumerate ( seq [ : ( len ( seq ) - 1 ) ] ) :
            if ( ( seq [ i ] < x ) and ( seq [ ( i + 1 ) ] >= x ) ) :
                return ( i + 1 )
                break
