def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            return i
        else :
            continue
    return len ( seq )
