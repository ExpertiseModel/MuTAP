def search ( x , seq ) :
    if ( not seq ) :
        return 0
    elif ( int ( x ) > seq [ ( len ( seq ) - 1 ) ] ) :
        return len ( seq )
    for ( i , ref_elem ) in enumerate ( seq ) :
        if ( x <= ref_elem ) :
            break
    return i
