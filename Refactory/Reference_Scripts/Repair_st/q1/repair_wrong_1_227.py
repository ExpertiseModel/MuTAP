def search ( x , seq ) :
    result = 0
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            result = i
            break
        else :
            result = len ( seq )
    return result
