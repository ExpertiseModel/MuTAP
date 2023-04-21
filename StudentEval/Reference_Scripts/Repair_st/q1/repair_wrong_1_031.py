def search ( x , seq ) :
    pass
    for ( i , ref_elem ) in enumerate ( seq ) :
        pass
        if ( x == ref_elem ) :
            return i
        if ( x < seq [ 0 ] ) :
            return 0
        elif ( ( x < ref_elem ) and ( x > seq [ ( i - 1 ) ] ) ) :
            return i
        pass
    return len ( seq )
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
