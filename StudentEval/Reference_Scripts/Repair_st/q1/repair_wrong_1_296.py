def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( x > seq [ i ] ) :
            continue
        elif ( x <= seq [ i ] ) :
            return i
        elif ( x > max ( seq ) ) :
            return len ( seq )
    return len ( seq )
