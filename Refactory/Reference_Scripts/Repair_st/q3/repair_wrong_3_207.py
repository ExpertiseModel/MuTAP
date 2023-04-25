def remove_extras ( lst ) :
    i = 0
    while ( i < len ( lst ) ) :
        if ( lst [ i ] in lst [ ( i + 1 ) : ] ) :
            ref_ext = lst [ ( i + 1 ) : ]
            ref_ext . remove ( lst [ i ] )
            lst = ( lst [ : ( i + 1 ) ] + ref_ext )
        else :
            i += 1
    return lst
    pass
