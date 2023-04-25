def search ( x , seq ) :
    pass
    if ( len ( seq ) == 0 ) :
        return 0
    pass
    ref_a = list ( enumerate ( seq ) )
    for i in ref_a :
        pass
        if ( x <= i [ 1 ] ) :
            return i [ 0 ]
        pass
    pass
    if ( x > seq [ ( - 1 ) ] ) :
        return len ( seq )
    pass
