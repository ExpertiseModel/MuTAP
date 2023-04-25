def search ( x , seq ) :
    position = 0
    while ( position < len ( seq ) ) :
        ref_temp = seq [ position ]
        if ( x <= ref_temp ) :
            return position
        elif ( seq [ position ] > x ) :
            pass
        position = ( position + 1 )
    if ( ( position == 0 ) and ( len ( seq ) != 0 ) ) :
        position = ( position + 1 )
    return position
