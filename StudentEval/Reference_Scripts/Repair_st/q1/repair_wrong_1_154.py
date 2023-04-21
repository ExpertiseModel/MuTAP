def search ( x , seq ) :
    ref_lst = [ ]
    for ( i , ref_elem ) in enumerate ( seq ) :
        if True :
            ref_lst . append ( ( i , ref_elem ) )
    for i in ref_lst :
        if ( x <= i [ 1 ] ) :
            return i [ 0 ]
    return len ( seq )
