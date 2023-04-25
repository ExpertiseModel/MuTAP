def remove_extras ( lst ) :
    lst . reverse ( )
    for ref_item in lst :
        while ( lst . count ( ref_item ) != 1 ) :
            lst . remove ( ref_item )
    lst . reverse ( )
    return lst
