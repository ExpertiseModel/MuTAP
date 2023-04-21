def remove_extras ( lst ) :
    result = [ ]
    for e in lst :
        if ( e not in result ) :
            result += ( e , )
    return result
