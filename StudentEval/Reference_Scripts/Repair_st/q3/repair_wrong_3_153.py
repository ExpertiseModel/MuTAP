def remove_extras ( lst ) :
    result = [ ]
    for ref_i in lst :
        if ( ref_i not in result ) :
            result += ( ref_i , )
    return result
