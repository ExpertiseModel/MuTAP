def search ( val , seq ) :
    if ( not seq ) :
        ref_i = 0
    elif ( val > seq [ ( len ( seq ) - 1 ) ] ) :
        ref_i = len ( seq )
    else :
        for ( ref_i , ref_elem ) in enumerate ( seq ) :
            if ( val <= ref_elem ) :
                ref_i
                break
    return ref_i
