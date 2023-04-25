def remove_extras ( lst ) :
    for i in lst :
        if ( lst . count ( i ) > 1 ) :
            element = lst [ : ( lst . index ( i ) + 1 ) ]
            ref_right = lst [ ( lst . index ( i ) + 1 ) : ]
            ref_right . remove ( i )
            lst = ( element + ref_right )
    return lst
