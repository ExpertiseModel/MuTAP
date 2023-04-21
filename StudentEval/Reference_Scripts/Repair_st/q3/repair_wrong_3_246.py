def remove_extras ( n ) :
    lst = [ ]
    i = 0
    while ( i < len ( n ) ) :
        ref_temp = n [ i ]
        if ( ref_temp not in lst ) :
            lst . append ( ref_temp )
        i += 1
    return lst
