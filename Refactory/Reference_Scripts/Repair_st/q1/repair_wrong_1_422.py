def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( seq == ( ) ) :
            return
        if ( x <= seq [ i ] ) :
            return i
        elif ( ref_elem > x ) :
            return len ( seq )
    return len ( seq )
