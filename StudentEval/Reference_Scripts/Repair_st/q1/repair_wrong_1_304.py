def search ( x , seq ) :
    if ( type ( seq ) == list ) :
        a = seq . copy ( )
        a . append ( x )
        a . sort ( )
        for ( i , elem ) in enumerate ( a ) :
            if ( elem == x ) :
                return i
    else :
        temp_tuple = list ( seq )
        temp_tuple . append ( x )
        temp_tuple . sort ( )
        for ( i , elem ) in enumerate ( temp_tuple ) :
            if ( elem == x ) :
                return i
