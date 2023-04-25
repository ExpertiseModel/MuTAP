def remove_extras ( lst ) :
    ref_list = [ ]
    for elem in lst :
        if ( elem not in ref_list ) :
            ref_list . append ( elem )
        else :
            continue
    return ref_list
