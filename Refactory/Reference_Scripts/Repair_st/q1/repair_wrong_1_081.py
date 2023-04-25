def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    for ( index , value ) in enumerate ( seq ) :
        if ( x <= value ) :
            return index
    return len ( seq )
