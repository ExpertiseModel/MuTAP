def search ( x , seq ) :
    for element in range ( len ( seq ) ) :
        if ( x <= seq [ element ] ) :
            return seq . index ( seq [ element ] )
        elif ( seq [ ( - 1 ) ] < x ) :
            return ( list ( seq ) . index ( max ( seq ) ) + 1 )
    return 0
