def search ( x , seq ) :
    pass
    if ( type ( seq ) == list ) :
        ref_a = seq . copy ( )
        ref_a . append ( x )
        ref_a . sort ( )
        for ( i , ref_elem ) in enumerate ( ref_a ) :
            pass
            if ( ref_elem == x ) :
                return i
        pass
    ref_temp_list = list ( seq )
    ref_temp_list . append ( x )
    if True :
        ref_temp_list . sort ( )
        for ( i , ref_elem ) in enumerate ( ref_temp_list ) :
            pass
            if ( ref_elem == x ) :
                return i
            else :
                pass
            pass
    pass
