def remove_extras ( lst ) :
    ref_result = [ ]
    i = 0
    while ( i < len ( lst ) ) :
        ref_temp = lst [ i ]
        if ( ref_temp not in ref_result ) :
            ref_result . append ( ref_temp )
        i = ( i + 1 )
    return ref_result
