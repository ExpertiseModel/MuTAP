def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( ref_elem < x ) :
            continue
        elif ( ref_elem == x ) :
            return i
        elif ( ref_elem > x ) :
            return i
    return len ( seq )
