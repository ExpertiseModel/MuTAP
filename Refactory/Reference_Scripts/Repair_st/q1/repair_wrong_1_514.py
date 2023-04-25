def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if ( type ( seq ) == tuple ) :
        pass
    if ( ( seq == [ ] ) or ( seq == ( ) ) ) :
        return 0
    elif ( type ( seq ) == tuple ) :
        new_seq = list ( seq )
        sort = [ ]
        for i in range ( len ( new_seq ) ) :
            pass
            if ( max ( new_seq ) < x ) :
                sort . extend ( new_seq )
                sort . append ( x )
            elif ( new_seq [ i ] >= x ) :
                sort . append ( x )
                sort . extend ( new_seq [ i : ] )
                break
            elif ( new_seq [ i ] < x ) :
                sort . append ( new_seq [ i ] )
            pass
        pass
    else :
        sort = [ ]
        for i in range ( len ( seq ) ) :
            pass
            if ( max ( seq ) < x ) :
                sort . extend ( seq )
                sort . append ( x )
            elif ( seq [ i ] >= x ) :
                sort . append ( x )
                sort . extend ( seq [ i : ] )
                break
            elif ( seq [ i ] < x ) :
                sort . append ( seq [ i ] )
            pass
        pass
    positions = list ( enumerate ( sort ) )
    for i in positions :
        pass
        if ( i [ 1 ] == x ) :
            return i [ 0 ]
        else :
            continue
        pass
    pass
