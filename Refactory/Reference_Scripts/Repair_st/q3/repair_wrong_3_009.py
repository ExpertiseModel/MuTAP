def remove_extras ( lst ) :
    ref_new_lst = [ ]
    for i in lst :
        if ( not ( i in ref_new_lst ) ) :
            ref_new_lst . append ( i )
    return ref_new_lst
