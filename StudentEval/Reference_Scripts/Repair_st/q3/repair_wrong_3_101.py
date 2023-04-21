def remove_extras ( lst ) :
    lst . reverse ( )
    for item in lst :
        while ( lst . count ( item ) != 1 ) :
            lst . remove ( item )
    lst . reverse ( )
    return lst
