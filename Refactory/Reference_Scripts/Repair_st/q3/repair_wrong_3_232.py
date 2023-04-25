def remove_extras ( lst ) :
    new_lst = [ ]
    for i in lst :
        if ( new_lst . count ( i ) == 0 ) :
            new_lst . append ( i )
    return new_lst
