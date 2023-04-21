def search ( x , seq ) :
    for ref_position in range ( len ( seq ) ) :
        if ( ( x < seq [ ref_position ] ) or ( x == seq [ ref_position ] ) ) :
            return ref_position
    return len ( seq )
