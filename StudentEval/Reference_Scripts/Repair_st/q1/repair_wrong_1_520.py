def search ( x , seq ) :
    if ( not seq ) :
        i = 0
    elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
        return len ( seq )
    else :
        for ( i , elem ) in enumerate ( seq ) :
            if ( x < ( elem + 1 ) ) :
                i
                break
    return i
