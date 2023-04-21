def search ( x , seq ) :
    ref_position = 0
    while ( ref_position < len ( seq ) ) :
        if ( seq [ ref_position ] == x ) :
            break
        elif ( seq [ ref_position ] > x ) :
            break
        ref_position = ( ref_position + 1 )
    return ref_position
