def remove_extras ( lst ) :
    ref_new_lst = [ ]
    for element in lst :
        if ( ( element in lst ) and ( element not in ref_new_lst ) ) :
            ref_new_lst . append ( element )
        else :
            lst
    return ref_new_lst
