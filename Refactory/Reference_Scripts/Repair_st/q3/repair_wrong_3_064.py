def remove_extras ( lst ) :
    new_lst = [ ]
    for e in lst :
        if ( e in new_lst ) :
            continue
        else :
            new_lst . append ( e )
    return new_lst
