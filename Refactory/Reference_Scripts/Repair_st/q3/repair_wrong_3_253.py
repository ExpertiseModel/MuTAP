def remove_extras ( lst ) :
    new_list = [ ]
    for i in lst :
        if ( i not in new_list ) :
            new_list = ( new_list + [ i ] )
    return new_list
