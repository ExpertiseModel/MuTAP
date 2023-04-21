def remove_extras ( lst ) :
    lst . reverse ( )
    for i in lst :
        pass
        if ( lst . count ( i ) > 1 ) :
            lst . remove ( i )
    lst . reverse ( )
    return lst
