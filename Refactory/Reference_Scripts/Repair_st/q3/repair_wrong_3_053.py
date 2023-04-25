def remove_extras ( lst ) :
    lst . reverse ( )
    for num in lst :
        while ( lst . count ( num ) > 1 ) :
            lst . remove ( num )
    lst . reverse ( )
    return lst
