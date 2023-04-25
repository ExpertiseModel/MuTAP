def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( x == ref_elem ) :
            return i
        elif ( x < seq [ 0 ] ) :
            return i
        elif ( ( x < ref_elem ) and ( x > seq [ ( i - 1 ) ] ) ) :
            return i
    return len ( seq )
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
