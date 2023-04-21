def search ( x , seq ) :
    if ( ( seq == [ ] ) or ( seq == ( ) ) ) :
        return 0
    elif ( x > seq [ ( - 1 ) ] ) :
        return len ( seq )
    else :
        for ( i , ref_elem ) in enumerate ( seq ) :
            if ( x <= seq [ i ] ) :
                return i
                break
            else :
                continue
