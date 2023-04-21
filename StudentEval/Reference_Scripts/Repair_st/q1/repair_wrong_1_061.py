def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( ref_elem == x ) :
            return i
        elif ( x > ref_elem ) :
            continue
        elif ( x < ref_elem ) :
            return i
    return len ( seq )
