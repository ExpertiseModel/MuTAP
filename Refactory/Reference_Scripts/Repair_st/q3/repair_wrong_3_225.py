def remove_extras ( lst ) :
    ref_a = [ ]
    for i in lst :
        ref_a = ( ref_a + [ i ] )
        if ( ref_a . count ( i ) > 1 ) :
            ref_a . pop ( )
    return ref_a
