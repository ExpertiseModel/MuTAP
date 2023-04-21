def remove_extras ( lst ) :
    ref_new_lst = [ ]
    for element in lst :
        if ( element not in ref_new_lst ) :
            ref_new_lst . append ( element )
    return ref_new_lst
