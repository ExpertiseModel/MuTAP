def search ( x , seq ) :
    if ( not seq ) :
        i = 0
    elif ( x > seq [ ( - 1 ) ] ) :
        i = len ( seq )
    else :
        for ( i , ref_elem ) in enumerate ( seq ) :
            if ( x <= ref_elem ) :
                i
                break
    return i
