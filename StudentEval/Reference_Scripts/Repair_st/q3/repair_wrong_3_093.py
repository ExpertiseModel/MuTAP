def remove_extras ( lst ) :
    lst . reverse ( )
    for ref_i in lst :
        pass
        if ( lst . count ( ref_i ) > 1 ) :
            ref_j = 0
            while ( ref_j < lst . count ( ref_i ) ) :
                lst . remove ( ref_i )
                ref_j += 1
            pass
    if True :
        lst . reverse ( )
        return lst
    pass
