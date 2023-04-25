def search ( x , seq ) :
    for ref_k in range ( len ( seq ) ) :
        if ( x <= seq [ ref_k ] ) :
            return ref_k
        elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
            return len ( seq )
    return len ( seq )
