def search ( x , seq ) :
    ref_result = 0
    for i in range ( len ( seq ) ) :
        if ( seq [ i ] >= x ) :
            continue
        else :
            ref_result = ( i + 1 )
    return ref_result
