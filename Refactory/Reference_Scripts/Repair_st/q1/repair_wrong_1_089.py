def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if ( ( seq == ( ) ) or ( seq == [ ] ) ) :
        return 0
    else :
        for i in range ( len ( seq ) ) :
            if ( x <= seq [ i ] ) :
                return i
        return ( count if ( seq [ ( - 1 ) ] > x ) else len ( seq ) )
