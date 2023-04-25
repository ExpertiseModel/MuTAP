def search ( x , seq ) :
    ref_counter = 0
    while ( ref_counter < len ( seq ) ) :
        if ( seq [ ref_counter ] >= x ) :
            return ref_counter
        ref_counter += 1
    return len ( seq )
