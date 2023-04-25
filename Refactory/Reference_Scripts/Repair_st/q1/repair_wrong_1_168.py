def search ( x , seq ) :
    ref_position = 0
    for element in seq :
        if ( x <= element ) :
            return list ( seq ) . index ( element )
        else :
            ref_position += 1
    return ref_position
