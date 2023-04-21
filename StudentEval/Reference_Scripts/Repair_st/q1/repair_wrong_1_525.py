def search ( x , seq ) :
    for ( ref_i , i ) in enumerate ( seq ) :
        if ( len ( seq ) == 0 ) :
            pass
        if ( ( x > i ) and ( ref_i == ( len ( seq ) - 1 ) ) ) :
            return ( ref_i + 1 )
        elif ( x > i ) :
            continue
        else :
            return ref_i
    if ( len ( seq ) == 0 ) :
        return 0
