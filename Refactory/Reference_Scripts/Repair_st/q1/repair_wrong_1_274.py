def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    enumerated = list ( enumerate ( seq ) )
    if ( ( seq == ( ) ) or ( seq == [ ] ) ) :
        return 0
    elif ( x > max ( seq ) ) :
        return len ( seq )
    else :
        enumerated = list ( enumerate ( seq ) )
        for i in range ( len ( enumerated ) ) :
            if ( enumerated [ i ] [ 1 ] >= x ) :
                return enumerated [ i ] [ 0 ]
                break
