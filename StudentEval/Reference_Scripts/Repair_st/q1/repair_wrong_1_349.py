def search ( x , seq ) :
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( x <= ref_elem ) :
            return i
    return len ( seq )
