def search ( x , seq ) :
    if ( seq == [ ] ) :
        pass
    if ( seq == ( ) ) :
        return 0
    elif ( seq == [ ] ) :
        return len ( seq )
    else :
        for ( i , ref_elem ) in enumerate ( seq ) :
            if ( x > seq [ ( - 1 ) ] ) :
                return len ( seq )
            elif ( x > ref_elem ) :
                continue
            else :
                return i
