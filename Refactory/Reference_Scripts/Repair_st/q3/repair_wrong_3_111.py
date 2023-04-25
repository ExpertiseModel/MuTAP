def remove_extras ( final ) :
    ref_final = [ ]
    for x in final :
        if ( x not in ref_final ) :
            ref_final . append ( x )
    return ref_final
    pass
