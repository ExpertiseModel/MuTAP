def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( elem < x ) :
            continue
        elif ( x == elem ) :
            return i
        elif ( elem > x ) :
            return i
    return len ( seq )
