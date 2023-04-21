def remove_extras ( lst ) :
    ref_result = [ ]
    for i in lst :
        pass
        if ( i not in ref_result ) :
            ref_result = ( ref_result + [ i ] )
        else :
            continue
        pass
    return ref_result
