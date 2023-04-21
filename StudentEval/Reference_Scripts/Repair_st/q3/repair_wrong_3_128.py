def remove_extras ( lst ) :
    ref_result = [ ]
    ref_counter = 0
    while ( ref_counter < len ( lst ) ) :
        ref_temp = lst [ ref_counter ]
        if ( ref_temp not in ref_result ) :
            ref_result . append ( ref_temp )
        ref_counter = ( ref_counter + 1 )
    return ref_result
