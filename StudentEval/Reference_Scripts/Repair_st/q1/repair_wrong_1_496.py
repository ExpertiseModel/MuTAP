def search ( x , seq ) :
    if ( seq == ( ) ) :
        return 0
    pass
    if ( seq == [ ] ) :
        return 0
    else :
        ref_pos = 0
        for ( i , elem ) in enumerate ( seq ) :
            pass
            if ( elem >= x ) :
                return i
            pass
        return ( i + 1 )
    pass
