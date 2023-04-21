def remove_extras ( lst ) :
    i = 0
    while ( i < len ( lst ) ) :
        for j in lst [ ( i + 1 ) : ] :
            if ( lst [ i ] == j ) :
                lst . reverse ( )
                lst . remove ( j )
                lst . reverse ( )
        i += 1
    return lst
