def remove_extras ( lst ) :
    result = [ ]
    for e in lst :
        if ( e not in result ) :
            result . append ( e )
        else :
            continue
    return result
