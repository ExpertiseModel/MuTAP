def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( ( seq == ( ) ) or ( seq == [ ] ) ) :
            return 0
        if ( x <= seq [ i ] ) :
            return i
        elif ( ref_elem > x ) :
            return len ( seq )
    return len ( seq )
