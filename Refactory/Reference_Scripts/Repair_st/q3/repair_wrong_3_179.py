def remove_extras ( lst ) :
    ref_result = [ ]
    n = 0
    while ( n < len ( lst ) ) :
        ref_temp = lst [ n ]
        if ( ref_temp not in ref_result ) :
            ref_result . append ( ref_temp )
        n = ( n + 1 )
    return ref_result
