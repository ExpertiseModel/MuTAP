def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( ref_elem == x ) :
            return i
        elif ( x == seq [ i ] ) :
            return i
        elif ( x < seq [ i ] ) :
            return i
    return len ( seq )
