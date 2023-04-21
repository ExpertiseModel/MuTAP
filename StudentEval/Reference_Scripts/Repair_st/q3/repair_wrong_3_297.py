def remove_extras ( lst ) :
    ref_n = 0
    while ( ref_n < len ( lst ) ) :
        if ( lst [ ref_n ] in lst [ ( ref_n + 1 ) : ] ) :
            ref_ext = lst [ ( ref_n + 1 ) : ]
            ref_ext . remove ( lst [ ref_n ] )
            lst = ( lst [ : ( ref_n + 1 ) ] + ref_ext )
        else :
            ref_n = ( ref_n + 1 )
    return lst
