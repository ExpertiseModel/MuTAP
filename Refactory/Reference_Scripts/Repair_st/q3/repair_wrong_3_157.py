def remove_extras ( lst ) :
    ref_a = [ ]
    for i in lst :
        if ( i in ref_a ) :
            continue
        else :
            ref_a . append ( i )
    return ref_a
