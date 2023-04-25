def search ( x , seq ) :
    for ( ref_i , ref_elem ) in enumerate ( seq ) :
        if ( ref_elem == x ) :
            return ref_i
        elif ( x >= max ( seq ) ) :
            continue
        elif ( x < ref_elem ) :
            return ref_i
    return len ( seq )
