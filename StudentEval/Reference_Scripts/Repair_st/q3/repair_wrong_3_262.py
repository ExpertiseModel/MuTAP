def remove_extras ( lst ) :
    buggy_listt = lst . reverse ( )
    for element in lst :
        if ( lst . count ( element ) > 1 ) :
            lst . remove ( element )
    lst . reverse ( )
    return lst
