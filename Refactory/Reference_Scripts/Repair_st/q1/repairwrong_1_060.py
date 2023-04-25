def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( x <= ref_elem ) :
            return i
            break
        elif ( x > max ( seq ) ) :
            return len ( seq )
    return len ( seq )
