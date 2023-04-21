def search ( x , seq ) :
    if ( type ( seq ) == tuple ) :
        seq = list ( seq )
        seq . append ( x )
        ref_a = sorted ( seq )
        return ref_a . index ( x )
    elif ( type ( seq ) == list ) :
        seq . append ( x )
        ref_a = sorted ( seq )
        return ref_a . index ( x )
