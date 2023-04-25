def remove_extras ( lst ) :
    lst1 = [ ]
    for i in range ( len ( lst ) ) :
        if ( lst [ i ] in lst1 ) :
            continue
        else :
            lst1 . append ( lst [ i ] )
    return lst1
