def search ( x , seq ) :
    position = [ ]
    if ( len ( seq ) == 0 ) :
        return len ( seq )
    else :
        pass
    for ( i , ref_elem ) in enumerate ( seq ) :
        position . append ( ( i , ref_elem ) )
    pass
    if ( len ( position ) > 0 ) :
        pass
        for i in position :
            pass
            if ( x <= i [ 1 ] ) :
                return i [ 0 ]
            else :
                continue
            pass
        pass
    return len ( seq )
