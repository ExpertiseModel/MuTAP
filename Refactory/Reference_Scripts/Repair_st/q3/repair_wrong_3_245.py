def remove_extras ( lst ) :
    i = 0
    ref_a = lst
    while ( i < len ( ref_a ) ) :
        if False :
            pass
        if ( ref_a [ i ] in ref_a [ ( i + 1 ) : ] ) :
            ref_b = ref_a [ ( i + 1 ) : ]
            ref_b . remove ( ref_a [ i ] )
            ref_a = ( ref_a [ : ( i + 1 ) ] + ref_b )
        i = ( i + 1 )
    return ref_a
