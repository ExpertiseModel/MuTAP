def search ( val , seq ) :
    if ( len ( seq ) == 0 ) :
        return 0
    elif ( val > seq [ ( len ( seq ) - 1 ) ] ) :
        return len ( seq )
    else :
        for ( ref_i , ref_elem ) in enumerate ( seq ) :
            if ( ref_elem >= val ) :
                return ref_i
    return position
