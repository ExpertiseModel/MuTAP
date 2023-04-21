def search ( x , seq ) :
    ref_counter = 0
    new_seq = list ( seq )
    if ( len ( seq ) == 0 ) :
        return 0
    for ref_element in seq :
        if ( x <= seq [ 0 ] ) :
            pass
        if ( x <= ref_element ) :
            return ref_counter
        if ( x > seq [ ( len ( seq ) - 1 ) ] ) :
            return len ( seq )
        ref_counter += 1
        continue
