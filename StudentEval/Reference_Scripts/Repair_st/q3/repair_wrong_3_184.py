def remove_extras ( lst ) :
    ref_new = [ ]
    for e in lst :
        if ( e not in ref_new ) :
            ref_new . append ( e )
    return ref_new
