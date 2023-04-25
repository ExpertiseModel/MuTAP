def remove_extras ( new_lst ) :
    ref_new_lst = [ ]
    for i in new_lst :
        ref_new_lst . append ( i )
        if ( ref_new_lst . count ( i ) > 1 ) :
            ref_new_lst . pop ( )
            continue
    return ref_new_lst
