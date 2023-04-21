def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if ( ( seq == ( ) ) or ( seq == [ ] ) or ( x <= seq [ 0 ] ) ) :
        return 0
    elif ( x > seq [ ( - 1 ) ] ) :
        return len ( seq )
    else :
        for ( j , seq_enum ) in enumerate ( seq [ : ( len ( seq ) - 1 ) ] ) :
            if ( ( x > seq_enum ) and ( x <= seq [ ( j + 1 ) ] ) ) :
                return ( j + 1 )
