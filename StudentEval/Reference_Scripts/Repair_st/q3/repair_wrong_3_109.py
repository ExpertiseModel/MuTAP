def remove_extras ( lst ) :
    ref_new_list = [ ]
    for k in range ( len ( lst ) ) :
        if ( lst [ k ] in lst [ : k ] ) :
            ref_new_list = ref_new_list
        else :
            ref_new_list = ( ref_new_list + [ lst [ k ] ] )
    return ref_new_list
