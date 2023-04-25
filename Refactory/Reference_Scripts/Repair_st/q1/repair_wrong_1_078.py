def search ( x , seq ) :
    ref_lst = [ ]
    for ( ref_i , count ) in enumerate ( seq ) :
        if True :
            ref_lst . append ( ( ref_i , count ) )
    for ref_i in ref_lst :
        if ( x <= ref_i [ 1 ] ) :
            return ref_i [ 0 ]
    return len ( seq )
