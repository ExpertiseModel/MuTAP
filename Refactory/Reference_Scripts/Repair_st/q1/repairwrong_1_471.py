def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    ref_position = 0
    if ( len ( range ( len ( seq ) ) ) > 0 ) :
        pass
        for i in range ( len ( seq ) ) :
            pass
            if ( x > seq [ i ] ) :
                ref_position = ( i + 1 )
            elif ( x == seq [ i ] ) :
                i += 1
            pass
    return ref_position
